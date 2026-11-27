---
description: "Code loads typed credentials through the shared secret provider"
when: "Reading credentials for an integration"
paths: src/library_catalog/**
---

Pass the secret name and its schema to `load_secret`. The loader fetches
the value from the configured provider and validates it against the schema.

## Why

The loader gives each integration the same configuration and validation path.

## Pattern

```python
class MetadataCredentials(BaseModel):
    api_token: SecretStr


def metadata_credentials() -> MetadataCredentials:
    return load_secret("metadata-feed", MetadataCredentials)
```
