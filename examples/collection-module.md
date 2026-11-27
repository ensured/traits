---
description: "Each MongoDB collection has a module named after it for data access functions"
when: "Adding a query or write for a MongoDB collection"
paths: src/library_catalog/storage/**
---

Put queries and writes for `books` in `storage/books.py`. Functions take
the database as their first argument.

## Pattern

```python
# src/library_catalog/storage/books.py
def find_by_isbn(db: Database, branch_id: str, isbn: str) -> BookDocument | None:
    return db.books.find_one({"branch_id": branch_id, "isbn": isbn})
```
