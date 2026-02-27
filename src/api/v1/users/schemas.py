from __future__ import annotations

from typing import TypedDict


class UserCreate(TypedDict):
    email: str
    full_name: str
    password: str
    is_active: bool


class UserUpdate(TypedDict, total=False):
    email: str
    full_name: str
    is_active: bool


class UserOut(TypedDict):
    id: int
    email: str
    full_name: str
    is_active: bool
    roles: list[str]


class UserListMeta(TypedDict):
    page: int
    page_size: int
    total: int
    has_next: bool
