---
description: "Route tests send requests through the shared api_client fixture"
when: "Testing an API route"
paths: tests/api/**
---

The `api_client` fixture creates a fresh application with test settings and
returns a FastAPI `TestClient` for the lifetime of the test.

## Why

Requests exercise routing, validation, and error rendering together. The fixture
gives each test an isolated application.

## Pattern

```python
def test_search_rejects_a_negative_limit(api_client):
    response = api_client.get("/books", params={"limit": -1})
    assert response.status_code == 422
```
