# Changelog

All notable changes to this project are documented in this file.

## [1.0.0] - 2026-02-27

### Added

- Added `scripts/bootstrap.sh` and `scripts/bootstrap.ps1` to provide one-command setup on macOS/Linux and Windows.
- Expanded documentation coverage for development, configuration, API, auth, RBAC, testing, security, deployment, and architecture.

### Changed

- Rewrote `README.md` with verified quickstart flows (local + Docker), endpoint verification steps, and practical next steps for template users.
- Updated docs and command examples to use the canonical Flask entrypoint `flaskforge.wsgi:app` where appropriate.
- Updated repository identity links and security contact details across docs and GitHub templates.
- Updated default `GITHUB_URL` values in runtime config and `.env.example`.

### Removed

- Removed empty tracked files: `uv.lock`, `src/migrations/versions/.keep`, and `src/instance/dev.db`.

## [0.1.0] - 2026-02-27

### Added

- Initial project scaffold.
