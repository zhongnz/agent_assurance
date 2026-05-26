# Release Checklist

*Steps to follow when cutting a new tagged release. Designed to keep citation metadata, Zenodo deposits, and the version trail in sync, after several DOI-drift incidents in the v0.8.x cycle.*

## Before the commit

- [ ] Decide whether the change set warrants a version bump. Substantive content, structural additions, and correctness fixes get a bump; purely operational maintenance commits (CI lint config tweaks, follow-up commits to land a deferred edit) typically don't.
- [ ] If bumping: pick the version following semver discipline. Patch for fixes and operational polish; minor for substantive content additions; major for breaking framing or methodology changes (none yet).
- [ ] Update `CITATION.cff` `version` field.
- [ ] Update `CITATION.cff` `date-released` to the actual commit date in `YYYY-MM-DD` UTC.
- [ ] Update README Status section's `vX.Y.Z` reference.
- [ ] Update README Status section's version *range* — the "v0.8.2 through v0.X.Y" sentence — to include the new version. This is the single most-missed update.
- [ ] Add a CHANGELOG entry under the new version heading. Mirror the substantive content into the commit message.
- [ ] If the change set is *not* getting a tag (it's maintenance on top of an existing release), mark the CHANGELOG entry explicitly as "Untagged maintenance, captured in vX.Y.Z's archive" or similar — never leave version entries floating without a corresponding tag.

## Committing

- [ ] Stage all relevant files.
- [ ] Commit with a multi-line message that mirrors the CHANGELOG entry.
- [ ] No `Co-Authored-By:` trailers for AI assistants or automated tools (human co-authorship follows GitHub's normal convention).
- [ ] Push to `main`.

## After the commit

- [ ] Verify the lint CI workflow passes on the new commit (`gh run list --limit 1`).
- [ ] If the commit warrants a tag, create the GitHub release: `gh release create vX.Y.Z --title "vX.Y.Z" --notes "$(...)"` with a notes block describing the release substantively, not just pointing at CHANGELOG.
- [ ] Wait for Zenodo to mint a new DOI for the tag (typically minutes; sometimes hours; check Zenodo's email notification or the GitHub-integration page at `https://zenodo.org/account/settings/github/repository/zhongnz/agent_assurance`).
- [ ] Once the DOI is minted, run the post-tag DOI update — a follow-up commit (no version bump) that updates:
  - [ ] `CITATION.cff` `identifiers` block — add the new DOI as the most recently minted; preserve prior version DOIs as historical identifiers.
  - [ ] `CITATION.cff` `preferred-citation.doi` field.
  - [ ] README badge URL (the `zenodo.org/badge/DOI/` URL).
  - [ ] README Citation section text (the "most recently DOI-minted release is vX.Y.Z" sentence; the prior-releases list).
  - [ ] README BibTeX snippet (`version` and `doi` fields paired with the most-recent DOI).
- [ ] Commit the DOI update as a follow-up with a message like "Update DOI references to vX.Y.Z archive."

## Sanity checks before declaring done

- [ ] Local `git tag -l` includes the new tag (run `git fetch --tags` if not).
- [ ] Remote `gh release view vX.Y.Z` confirms the release exists.
- [ ] CITATION.cff parses as valid YAML (`python3 -c "import yaml; yaml.safe_load(open('CITATION.cff'))"`).
- [ ] README badge URL renders the correct DOI.
- [ ] No stale references to the previous version in the diff (other than in CHANGELOG historical entries, which are expected to be frozen-in-time).
- [ ] The version range in README Status reflects the new version.

## Common pitfalls observed in the v0.8.x cycle

- **DOI lag drift.** Tagging triggers a Zenodo deposit, but the DOI doesn't appear in CITATION/README until the post-tag follow-up commit. Don't forget the second commit. (Caused: v0.8.17, v0.8.19, v0.8.20, v0.8.21, v0.8.22 metadata staleness.)
- **Untagged maintenance commits.** v0.8.13 and v0.8.18 were each committed with a CHANGELOG entry but never separately tagged; their changes were captured in v0.8.14's and v0.8.19's archives respectively. CHANGELOG should mark such entries explicitly (the inline-annotation pattern used in v0.8.13 and v0.8.18 entries works) or the next tag should absorb them.
- **Version-range drift.** README's "v0.8.2 through v0.X.Y" range needs updating *each* release; easy to miss because the lead `vX.Y.Z` reference is the obvious thing to update. The range is the same line, two clauses later.
- **Date drift.** `date-released` should match the actual tag/release date, not when CITATION.cff was last edited. Confirm with `date -u` before committing.
- **CHANGELOG narrative claiming forward-pointing language that isn't in CITATION.cff.** Earlier audits found CHANGELOG entries describing forward-pointing DOI language ("each subsequent tagged release receives its own version-specific DOI") that had been trimmed from CITATION.cff in a later edit. Keep the two in sync.

## When to skip parts of this checklist

- Purely operational follow-up commits (DOI updates, lint-config tweaks, small README typo fixes) often don't get their own version bump or tag. The CHANGELOG entry can be folded into the prior version's entry as a post-tag note, or omitted if the change is truly trivial. The discipline is to not invent versions for non-substantive changes.
- The post-tag DOI update is sometimes batched — wait for multiple Zenodo DOIs to land and update all of them in a single follow-up commit. This is fine; just keep the lag bounded (no more than a few days between DOI minting and CITATION update).

## See also

- `CHANGELOG.md` — the version history this checklist supports
- `CITATION.cff` — the metadata file this checklist's discipline targets
- `paper/control_matrix.md` revision protocol section — the matrix's own revision discipline (analogous shape, smaller scope)
