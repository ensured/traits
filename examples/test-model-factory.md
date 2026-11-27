---
description: "Tests build stored documents with shared fixtures that provide valid defaults"
when: "Creating a stored document for a test"
paths: tests/**
---

Use a factory fixture such as `make_book` and override the fields the test
needs. The fixture returns a fresh document for each call.

## Why

The fixture tracks the document schema, so tests can focus on the field
values that matter to the behaviour under test.

## Pattern

```python
def test_find_book_by_isbn(mongo_db, make_book):
    book = make_book(isbn="9780140449136")
    mongo_db.books.insert_one(book)

    assert find_by_isbn(mongo_db, book["branch_id"], book["isbn"]) == book
```
