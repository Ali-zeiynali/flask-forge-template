# Deployment Guide

## Docker image

```bash
docker build -t flask-forge-template .
docker run --rm -p 8000:8000 --env-file .env flask-forge-template
```

The container starts Gunicorn with `src/wsgi.py` (`wsgi:app`) on port `8000`.

## docker-compose

```bash
docker compose up --build
```

`docker-compose.yml` runs migrations before launching Gunicorn.

## Production notes

1. Set strong `SECRET_KEY` and `JWT_SECRET_KEY`.
2. Use a persistent production database (PostgreSQL/MySQL), not SQLite.
3. Set `APP_ENV=production`.
4. Ensure `FORCE_HTTPS=true` and `ENABLE_HSTS=true` behind TLS.
5. Put the app behind a reverse proxy (Nginx/Caddy/Load Balancer).
