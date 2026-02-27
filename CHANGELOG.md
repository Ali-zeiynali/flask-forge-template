# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added

- Web landing blueprint at `/` with a responsive Tailwind dark UI, inline rocket SVG, runtime status cards, and CTA shortcuts to health/docs/GitHub.
- Security headers integration via `Flask-Talisman` with configurable toggles (`ENABLE_SECURITY_HEADERS`, `FORCE_HTTPS`, `ENABLE_HSTS`).
- Password hashing migrated to `argon2` while preserving compatibility with existing werkzeug `scrypt` hashes.
- New docs pages: frontend, security, auth, RBAC, CLI, and testing guides.
- Security and quality commands for coverage, `bandit`, and `pip-audit` in Makefile/scripts and CI security job.
- Tests for landing page rendering and production security headers behavior.

### Changed

- App factory now registers a dedicated web blueprint and security headers extension without breaking existing `/api` and `/api/v1` routes.
- README rewritten with PowerShell-first onboarding, command catalog, architecture snapshot, and doc references.
- `.env.example` and config expanded with app metadata, docs/GitHub links, CI status, and security header settings.

### Added

- Admin endpoint `POST /api/admin/roles/{id}/permissions` for role-permission assignment/removal.
- New CLI command `forge doctor` for safe runtime diagnostics.

### Changed

- Config now supports `APP_ENV`, `JWT_ACCESS_EXPIRES`, `JWT_REFRESH_EXPIRES`, `RATE_LIMIT_ENABLED`, `SECURITY_HEADERS_ENABLED`, and `ADMIN_SEED_ENABLED` with legacy aliases.
- Authorization now allows regular users to update only their own profile while preserving admin/staff write controls.
- Response helpers expanded to include `ok`, `created`, `no_content`, and `paginated` with backward-compatible aliases.
- Logging now emits request/response summaries with correlation ID propagation via `X-Request-ID`.
- Docs updated for new env vars and admin API coverage.

## [0.1.0] - 2026-02-27

### Added

- Initial project scaffold.
