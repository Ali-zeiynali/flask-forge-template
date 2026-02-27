# RBAC and Permissions

## Default roles

- `admin`
- `staff`
- `user`

## Default permissions

- `users:read`
- `users:write`
- `roles:read`
- `roles:write`

## Decorators

- `@require_auth`
- `@require_roles(*roles)`
- `@require_permissions(*permissions)`
- `@require_owner_or_permission(permission, owner_param="user_id")`

## Admin role assignment example

```bash
curl -X POST http://127.0.0.1:5000/api/admin/users/2/roles \
  -H "Authorization: Bearer <ADMIN_ACCESS_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"name":"staff","action":"assign"}'
```
