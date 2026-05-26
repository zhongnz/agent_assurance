#!/usr/bin/env python3
"""Check internal consistency of the citation surface.

The release-checklist post-tag DOI update flow keeps the README badge, the
README citation table, the README BibTeX block, and CITATION.cff's preferred
citation in sync with the most-recently-minted DOI. This check catches drift
between those surfaces — the failure mode the v0.8.x cycle hit multiple times.

It does NOT check tag-vs-Zenodo state. DOI minting has expected lag during
the post-tag follow-up window; the user can tag, push, and update citation
files after the DOI lands. Checking against Zenodo's external state would
produce false positives during that window.

What this script verifies (all must reference the same DOI):
- CITATION.cff first identifier value (most-recently-minted DOI)
- CITATION.cff preferred-citation.doi
- README badge image URL DOI
- README "most recently DOI-minted release" sentence DOI
- README BibTeX block doi field
- README "most recently DOI-minted release" sentence version matches BibTeX version

Exit codes:
- 0: citation surface internally consistent
- 1: drift detected
- 2: parsing or file-read error
"""
from __future__ import annotations

import os
import re
import sys

try:
    import yaml
except ImportError:
    print(
        "PyYAML is required. Install with: pip install PyYAML",
        file=sys.stderr,
    )
    sys.exit(2)


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_citation_cff() -> tuple[str, str, list[dict]]:
    path = os.path.join(ROOT, "CITATION.cff")
    try:
        with open(path) as f:
            cff = yaml.safe_load(f)
    except Exception as exc:
        print(f"Failed to parse {path}: {exc}", file=sys.stderr)
        sys.exit(2)
    return (
        cff.get("version", ""),
        cff.get("preferred-citation", {}).get("doi", ""),
        cff.get("identifiers", []) or [],
    )


def parse_readme() -> dict:
    path = os.path.join(ROOT, "README.md")
    try:
        with open(path) as f:
            readme = f.read()
    except Exception as exc:
        print(f"Failed to read {path}: {exc}", file=sys.stderr)
        sys.exit(2)

    out: dict = {}

    badge_m = re.search(
        r"zenodo\.org/badge/DOI/(10\.5281/zenodo\.\d+)\.svg", readme
    )
    out["badge_doi"] = badge_m.group(1) if badge_m else None

    recent_m = re.search(
        r"most recently DOI-minted release is v([\d.]+)\s*\(\[(10\.5281/zenodo\.\d+)\]",
        readme,
    )
    out["recent_version"] = recent_m.group(1) if recent_m else None
    out["recent_doi"] = recent_m.group(2) if recent_m else None

    bibtex_m = re.search(r"```bibtex\s*\n(.*?)\n```", readme, re.DOTALL)
    out["bibtex_version"] = None
    out["bibtex_doi"] = None
    if bibtex_m:
        block = bibtex_m.group(1)
        v_m = re.search(r"version\s*=\s*\{v?([\d.]+)\}", block)
        d_m = re.search(r"doi\s*=\s*\{(10\.5281/zenodo\.\d+)\}", block)
        if v_m:
            out["bibtex_version"] = v_m.group(1)
        if d_m:
            out["bibtex_doi"] = d_m.group(1)

    return out


def main() -> int:
    cff_version, cff_preferred_doi, cff_identifiers = parse_citation_cff()
    readme = parse_readme()

    cff_latest_id_doi = (
        cff_identifiers[0].get("value", "") if cff_identifiers else ""
    )

    errors: list[str] = []

    if not cff_latest_id_doi:
        errors.append(
            "CITATION.cff identifiers list is empty or missing a first DOI"
        )

    if cff_preferred_doi and cff_latest_id_doi and (
        cff_preferred_doi != cff_latest_id_doi
    ):
        errors.append(
            f"CITATION.cff preferred-citation.doi ({cff_preferred_doi}) "
            f"!= first identifier value ({cff_latest_id_doi}). The preferred "
            f"citation should point to the most-recently-minted DOI."
        )

    def check(label: str, value, expected, expected_label: str) -> None:
        if value is None:
            errors.append(f"{label} not found in README — check parser regex")
            return
        if expected and value != expected:
            errors.append(
                f"{label} ({value}) != {expected_label} ({expected})"
            )

    check(
        "README badge DOI",
        readme["badge_doi"],
        cff_latest_id_doi,
        "CITATION.cff latest identifier",
    )
    check(
        "README 'most recently DOI-minted release' sentence DOI",
        readme["recent_doi"],
        cff_latest_id_doi,
        "CITATION.cff latest identifier",
    )
    check(
        "README BibTeX doi",
        readme["bibtex_doi"],
        cff_latest_id_doi,
        "CITATION.cff latest identifier",
    )

    if (
        readme["recent_version"]
        and readme["bibtex_version"]
        and readme["recent_version"] != readme["bibtex_version"]
    ):
        errors.append(
            f"README 'most recently DOI-minted release' version "
            f"({readme['recent_version']}) != README BibTeX version "
            f"({readme['bibtex_version']})"
        )

    if errors:
        print("Citation drift detected:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        print("", file=sys.stderr)
        print(
            "The release-checklist post-tag DOI update flow keeps these "
            "surfaces in sync; see RELEASE_CHECKLIST.md.",
            file=sys.stderr,
        )
        return 1

    print("Citation surface internally consistent.")
    print(f"  CITATION.cff version:       {cff_version}")
    print(f"  Most-recently-minted DOI:   {cff_latest_id_doi}")
    print(f"  README badge DOI:           {readme['badge_doi']}")
    print(f"  README recent-release DOI:  {readme['recent_doi']}")
    print(f"  README recent-release vers: {readme['recent_version']}")
    print(f"  README BibTeX DOI:          {readme['bibtex_doi']}")
    print(f"  README BibTeX version:      {readme['bibtex_version']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
