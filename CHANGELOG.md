# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added

- JWT authentication module with register/login/refresh/logout/me endpoints.
- RBAC data model (`roles`, `permissions`, `user_roles`, `role_permissions`) and admin management API.
- Authorization decorators for auth, role checks, permission checks, and owner-or-permission checks.
- CLI commands: `flask forge seed` and `flask forge create-admin`.
- Login brute-force protection with in-memory rate limit window.
- Request-id aware structured logging and configurable CORS support.
- New migration `20260227_000002` for auth/RBAC tables and user auth fields.
- Deterministic tests for auth, admin authorization, and permission-protected users CRUD.

### Changed

- Unified response contract to `{data, meta}` for success and `{error}` for failures.
- Users endpoints now require permission-based authorization while preserving `/api/users` compatibility and adding `/api/v1` aliases.
- Configuration and `.env.example` expanded for JWT, CORS, and rate limiting settings.
- Documentation updated with RBAC, seed workflow, migration usage, and PowerShell-first commands.

## [0.1.0] - 2026-02-27

### Added

- Initial project scaffold.
