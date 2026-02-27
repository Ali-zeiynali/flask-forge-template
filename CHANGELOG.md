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

## [0.1.0] - 2026-02-27

### Added

- Initial project scaffold.
