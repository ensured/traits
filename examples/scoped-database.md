---
description: "Routes that access branch records receive a caller-scoped repository"
when: "Adding or changing a route that reads or writes branch records"
paths: src/library_catalog/api/routes/**
check:
  test: tests/api/test_route_contracts.py::test_book_routes_use_branch_scope
  covers: "Book routes obtain their repository through the branch scope dependency"
---

The `get_branch_books` dependency resolves the branch using the caller's
authenticated membership. The repository includes that branch in its queries
and writes.

## Why

Reads and writes share the same scope rule across branch routes.

## Pattern

```python
BranchBooks = Annotated[BookRepository, Depends(get_branch_books)]


@router.get("/books/{book_id}", summary="Get a book by ID")
def get_book(book_id: str, books: BranchBooks) -> BookResponse:
    return BookResponse(**find_book_or_404(books, book_id))
```
