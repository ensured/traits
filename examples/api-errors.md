---
description: "API routes raise errors defined in the shared API error module"
when: "Returning an API error from a route"
paths: src/library_catalog/api/routes/**
---

Translate a domain error to an exception from `library_catalog.api.errors`.
The application error handler renders the same response schema for each route.

## Why

Clients can handle errors from any catalog route with the same decoder.

## Pattern

```python
def add_book(book: BookDraft, books: BranchBooks) -> BookResponse:
    try:
        record = books.add(book)
    except DuplicateISBN as error:
        raise ConflictError("This branch already has a book with that ISBN") from error
    return BookResponse(**record)
```
