---
description: "A MongoDB document ID starts with its collection prefix followed by an underscore and a ULID"
when: "Creating a MongoDB document"
paths: src/library_catalog/storage/**
---

Each collection module defines its own prefix. The rest of the ID is a
lowercase ULID.

## Why

An ID in a log tells you which collection to look in. Within a prefix, IDs
sort by their encoded creation timestamp.

## Pattern

```python
# src/library_catalog/storage/books.py
BOOK_ID_PREFIX = "book"


def new_book_id() -> str:
    return f"{BOOK_ID_PREFIX}_{str(new_ulid()).lower()}"
```
