# Repository instructions

## Public code-field compatibility invariant

- Document existing public subject parameters as `symbol`, including index,
  sector, ETF, and other subjects already exposed under that name.
- When an endpoint has a second constituent-security parameter, document it as
  `con_symbol`.
- Do not replace these public fields with `index_code`, `bk_code`, `con_code`,
  `etf_code`, or other type-specific names merely for naming uniformity.
- Internal database or upstream fields such as `ts_code`, `index_code`, and
  `con_code` do not determine the public API or Skill naming.
- Keep generated endpoint references, examples, and research workflows aligned
  with the backward-compatible API contract.

## GitHub account and push safety

The only GitHub destination for this repository is
`https://github.com/QuantSonar/quantsonar-skills.git`, authenticated as the
`QuantSonar` GitHub account.

Before every fetch or push:

- Check `pwd`, the current branch, `git status`, `git worktree list`, and
  `git remote -v`.
- Run `gh auth switch --user QuantSonar` immediately before verification and
  again immediately before pushing. Do not rely on whichever global account
  happened to be active earlier; other tasks may change it.
- Check the active GitHub account and verify the exact target with
  `gh repo view QuantSonar/quantsonar-skills`; the owner, repository name, and
  permission must all match.
- Treat `Repository not found` as an authentication or visibility problem.
  Never infer that a repository moved, and never select a same-named repository
  under another owner merely because it is visible.
- Never change a remote from one GitHub owner to another without the user's
  explicit confirmation. If the configured remote and intended owner differ,
  stop and ask before fetching or pushing.
- Push only the explicit current branch, then verify that local `HEAD`, the
  upstream ref, and the exact target repository's remote branch resolve to the
  same commit.

If a push reaches an unintended repository, stop further writes, report the
exact repositories and commits, push to the intended destination only after it
is verified, and remove the unintended ref only after confirming that it was
created by the mistaken push and that the commit is preserved elsewhere.
