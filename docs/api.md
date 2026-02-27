# API

## Response contract

Success:

```json
{
    "data": {},
    "meta": {}
}
```

Error:

```json
{
    "error": {
        "code": "validation_error",
        "message": "Request body is required.",
        "details": {}
    }
}
```

## Health

- `GET /api/health`
- `GET /api/v1/health`

Both return envelope data:

```json
{"data": {"status": "ok"}}
```

## Auth

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `POST /api/auth/logout`
- `GET /api/auth/me`

All endpoints are also available under `/api/v1/auth/*`.

## Users

- `POST /api/users`
- `GET /api/users/{id}`
- `GET /api/users?page=1&page_size=10`
- `PATCH /api/users/{id}`
- `DELETE /api/users/{id}`

All endpoints are also available under `/api/v1/users/*`.

Pagination meta:

```json
{
    "page": 1,
    "page_size": 10,
    "total": 120,
    "has_next": true
}
```

## Admin

All endpoints require `admin` role.

- `GET/POST /api/admin/roles`
- `PATCH/DELETE /api/admin/roles/{id}`
- `GET/POST /api/admin/permissions`
- `PATCH/DELETE /api/admin/permissions/{id}`
- `POST /api/admin/users/{id}/roles`
- `POST /api/admin/roles/{id}/permissions`

All endpoints are also available under `/api/v1/admin/*`.
