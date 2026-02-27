from __future__ import annotations


def max_page_size(requested: int) -> int:
    return min(requested, 100)
