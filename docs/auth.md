# Authentication

## Endpoints

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `POST /api/auth/logout`
- `GET /api/auth/me`

All endpoints are also available under `/api/v1`.

## Login example

```bash
curl -X POST http://127.0.0.1:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@example.com","password":"Password123"}'
```

## Protected endpoint example

```bash
curl http://127.0.0.1:5000/api/auth/me \
  -H "Authorization: Bearer <ACCESS_TOKEN>"
```

## Refresh example

```bash
curl -X POST http://127.0.0.1:5000/api/auth/refresh \
  -H "Authorization: Bearer <REFRESH_TOKEN>"
```
