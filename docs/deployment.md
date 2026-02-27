# Deployment

## Docker

```bash
docker build -t flask-forge-template .
docker run --rm -p 8000:8000 --env-file .env flask-forge-template
```

## Compose

```bash
docker compose up --build
```
