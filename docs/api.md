# API Guide

## Base paths

All implemented endpoints are mounted on both:

- `/api/*`
- `/api/v1/*`

This keeps compatibility while encouraging versioned usage.

## Response envelope

Success responses:

```json
{
    "data": {},
    "meta": {}
}
```

Error responses:

```json
{
    "error": {
        "code": "validation_error",
        "message": "Request body is required.",
        "details": {}
    }
}
```

## Endpoint groups

### Health

- `GET /api/health`
- `GET /api/v1/health`

### Auth

- `POST /api/auth/register`
- `POST /api/auth/login`
- `POST /api/auth/refresh`
- `POST /api/auth/logout`
- `GET /api/auth/me`

### Users

- `POST /api/users`
- `GET /api/users`
- `GET /api/users/{user_id}`
- `PATCH /api/users/{user_id}`
- `DELETE /api/users/{user_id}`

### Admin (role required: `admin`)

- `GET/POST /api/admin/roles`
- `PATCH/DELETE /api/admin/roles/{role_id}`
- `GET/POST /api/admin/permissions`
- `PATCH/DELETE /api/admin/permissions/{permission_id}`
- `POST /api/admin/users/{user_id}/roles`
- `POST /api/admin/roles/{role_id}/permissions`
