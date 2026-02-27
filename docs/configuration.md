# Configuration Guide

Configuration is defined in `src/config.py` and loaded through `get_config`.

## Config classes

- `DevelopmentConfig`
- `TestingConfig`
- `ProductionConfig`

Selection is based on `APP_ENV` (fallback: `FLASK_ENV`).

## Environment setup

1. Copy `.env.example` to `.env`.
2. Update secrets and database URL.
3. Keep `.env` private (already ignored by `.gitignore`).

## Key environment variables

- `APP_NAME`, `APP_VERSION`, `APP_ENV`
- `SECRET_KEY`, `JWT_SECRET_KEY`
- `DATABASE_URL`
- `JWT_ACCESS_EXPIRES`, `JWT_REFRESH_EXPIRES`
- `CORS_ORIGINS`
- `LOG_LEVEL`
- `RATE_LIMIT_ENABLED`, `RATE_LIMIT_LOGIN_PER_MINUTE`
- `SECURITY_HEADERS_ENABLED`, `ENABLE_HSTS`, `FORCE_HTTPS`
- `DOCS_URL`, `GITHUB_URL`, `CI_STATUS`

## Required values before production

At minimum, set these explicitly:

- `SECRET_KEY`
- `JWT_SECRET_KEY`
- `DATABASE_URL`
- `APP_ENV=production`
