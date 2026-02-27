# Deployment

## Docker

```bash
docker build -t flask-forge-template .
docker run --rm -p 8000:8000 --env-file .env flask-forge-template
```

## Docker Compose

```bash
docker compose up --build
```

The image starts Gunicorn on port `8000` and serves `wsgi:app` from `src`.
