# Security

## Security headers

`Flask-Talisman` is enabled through `init_security_headers`.

Config flags:

- `ENABLE_SECURITY_HEADERS` (default: `true`)
- `FORCE_HTTPS` (default: `false`, production: `true`)
- `ENABLE_HSTS` (default: `false`, production: `true`)

Default CSP allows local assets plus Tailwind CDN.

## Password hashing

New passwords use `argon2-cffi` (`argon2`) for stronger hashing defaults.

Backward compatibility is preserved for existing `werkzeug` `scrypt:` hashes:

- verify legacy `scrypt` hashes
- hash new passwords with `argon2`

## Rate limiting

Login endpoint has in-memory per-IP limiting via `RATE_LIMIT_LOGIN_PER_MINUTE`.

## Security tooling

Run audits with Python modules:

```bash
python -m bandit -r src
python -m pip_audit
```

CI includes a dedicated `security` job for these checks.
