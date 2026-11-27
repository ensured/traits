---
description: "One client module owns HTTP calls to each external data source"
when: "Calling an external data source over HTTP"
paths: src/library_catalog/sources/**
---

The source module names the endpoints and converts responses into catalog
records. It receives a preconfigured HTTP client with the source's base URL
and the project's timeouts.

## Why

Changes to a provider's URLs or response formats stay local to one module.

## Pattern

```python
# src/library_catalog/sources/metadata.py
class MetadataClient:
    def __init__(self, http: httpx.Client) -> None:
        self.http = http

    def fetch_book(self, isbn: str) -> BookMetadata:
        response = self.http.get("/books", params={"isbn": isbn})
        response.raise_for_status()
        return BookMetadata.model_validate(response.json())
```
