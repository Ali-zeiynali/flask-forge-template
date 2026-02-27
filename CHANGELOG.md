# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added

- Package compatibility entrypoint `src/flaskforge/wsgi.py` so Flask can run with `--app flaskforge.wsgi:app`.
- Versioned admin module under `api/v1/admin` with role/permission management and assignment endpoints.

### Changed

- Completed `api/v1` modules for auth/users with real schema validation, services, repository usage, and runtime RBAC enforcement.
- Preserved `/api/*` endpoints as compatibility aliases while wiring the canonical implementation in `/api/v1/*`.
- Unified health endpoint contract to the same envelope used by the rest of the API.
- Updated `scripts/init_db.sh` to run migrations plus RBAC seed.
- Synced API/auth/RBAC/architecture docs and README command examples with actual runtime behavior.

## [0.1.0] - 2026-02-27

### Added

- Initial project scaffold.
