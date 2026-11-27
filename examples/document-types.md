---
description: "MongoDB document annotations use a TypedDict named for the entity with a Document suffix"
when: "Defining or changing the shape of a stored document"
paths: src/library_catalog/storage/documents.py
---

Annotate functions that read or write the collection with that document type.

## Pattern

```python
class BookDocument(TypedDict):
    _id: str
    branch_id: str
    isbn: str
    title: str
```
