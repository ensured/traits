---
description: "Every catalog route declares a short OpenAPI summary"
when: "Adding or changing a FastAPI path operation"
paths: src/library_catalog/api/routes/**
---

Set `summary` on the route decorator using a clear verb and object.

## Why

The summary lets readers find an operation quickly in the generated API reference.

## Pattern

```python
@router.get("/books/{book_id}", summary="Get a book by ID")
def get_book(book_id: str, books: BranchBooks) -> BookResponse:
    return BookResponse(**find_book_or_404(books, book_id))
```
