# Ace GitHub Organization Defaults

This public repository provides the organization profile plus centrally
maintained GitHub Actions workflows for Ace repositories.

## Reusable workflows

- `reusable-ruff.yml` runs a pinned Ruff release against caller-selected paths.
- `reusable-shellcheck.yml` runs ShellCheck across caller-selected directories.
- `reusable-gitleaks.yml` scans full Git history with the free gitleaks binary.

Call central workflows with a full commit SHA. Tags and branches are easier to
read, but a SHA ensures a previously reviewed caller cannot silently execute a
different workflow later.

Organization policy allows actions owned by Ace, actions owned by GitHub, and
Marketplace actions from verified creators. The default `GITHUB_TOKEN` remains
read-only and cannot approve pull requests.

Mandatory SHA pinning is a later migration step. Do not enable it at the
organization level until every existing repository workflow has been updated.
