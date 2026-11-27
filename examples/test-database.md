---
description: "Storage integration tests query a MongoDB instance through an isolated database fixture"
when: "Testing MongoDB reads, writes, indexes, or transactions"
paths: tests/storage/**
---

The fixture creates a separate database for each test in a disposable
MongoDB instance and removes it at teardown.

## Why

Assertions exercise the actual query engine and its index semantics.

## Pattern

```python
def test_unique_isbn_index_applies_within_branch(mongo_db, make_book):
    apply_indexes(mongo_db)
    isbn = "9780140449136"
    mongo_db.books.insert_one(make_book(branch_id="central", isbn=isbn))
    mongo_db.books.insert_one(make_book(branch_id="west", isbn=isbn))

    with pytest.raises(DuplicateKeyError):
        mongo_db.books.insert_one(make_book(branch_id="central", isbn=isbn))
```
