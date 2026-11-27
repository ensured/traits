---
description: "MongoDB index definitions live in the storage index registry"
when: "Adding or changing a MongoDB index"
paths: src/library_catalog/storage/indexes.py
---

The index migration command reads `INDEXES` and applies the required
changes in a separate migration step.

## Why

Reviewers can see the desired schema in one place. Running migrations
separately keeps index builds out of application startup.

## Pattern

```python
INDEXES = {
    "books": [
        IndexModel(
            [("branch_id", ASCENDING), ("isbn", ASCENDING)],
            name="books_branch_isbn",
            unique=True,
        ),
    ],
}
```
