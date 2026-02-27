# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added

- Users CRUD API module with create/get/list/update/delete endpoints under `/api/users`.
- Unified API response and error schema helpers.
- Initial Alembic migration for `users` table.
- CRUD and error-case tests for users.

### Changed

- App factory now registers users blueprint and global error handlers.
- CI workflow now runs tooling via `python -m ...` commands.
- Documentation expanded for architecture, API usage, migrations, and PowerShell quickstart.

## [0.1.0] - 2026-02-27

### Added

- Initial project scaffold.
