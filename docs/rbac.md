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
- `permissions:read`
- `permissions:write`

## Enforcement

- Regular users can only read/update their own user resource.
- Admin users can manage users, roles, and permissions.

## Decorators

- `@require_auth`
- `@require_roles(*roles)`
- `@require_permissions(*permissions)`
- `@require_owner_or_permission(permission, owner_param="user_id")`
