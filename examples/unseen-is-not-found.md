---
description: "A missing or out-of-scope catalog record produces the same 404 response"
when: "Looking up a branch record requested by a caller"
paths: src/library_catalog/api/**
---

Look up the record in the caller's scoped repository and map a missing
result to the API's standard not-found error.

## Why

The response reveals only whether the requested record is visible to the caller.

## Pattern

```python
def find_book_or_404(books: BookRepository, book_id: str) -> BookDocument:
    book = books.find_by_id(book_id)
    if book is None:
        raise NotFoundError("Book not found")
    return book
```
