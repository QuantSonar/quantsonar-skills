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
