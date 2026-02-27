# Security Guide

## Security headers

Headers are configured via `Flask-Talisman` in `src/extensions/security_headers.py`.

Relevant flags:

- `SECURITY_HEADERS_ENABLED`
- `FORCE_HTTPS`
- `ENABLE_HSTS`

## Password handling

- New passwords are hashed with Argon2.
- Legacy `scrypt` hashes remain verifiable for compatibility.

## Authentication and authorization

- JWT access/refresh tokens via `Flask-JWT-Extended`
- Role/permission checks in `src/core/authz.py`

## Login rate limiting

- In-memory per-IP limit on login endpoint.
- Controlled by `RATE_LIMIT_ENABLED` and `RATE_LIMIT_LOGIN_PER_MINUTE`.

## Security checks

```bash
python -m bandit -r src
python -m pip_audit
```

For vulnerability reporting, see [SECURITY.md](../SECURITY.md).
