---
description: "CLI code imports the generated catalog client inside the function that uses it"
when: "Calling the catalog API from a CLI command or helper"
paths: src/library_catalog/cli/**
---

Keep the import local to the command or to the helper that creates the client.

## Why

Local commands and help output can load before the optional API client is installed.

## Pattern

```python
def make_remote_catalog(config: CatalogConfig) -> RemoteCatalog:
    from library_catalog.generated import CatalogClient

    return RemoteCatalog(CatalogClient(base_url=config.catalog_url))
```
