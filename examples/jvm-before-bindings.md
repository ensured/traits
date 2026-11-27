---
description: "An entry point starts the JVM before importing catalog Java bindings"
when: "Calling the metadata parser from an entry point"
paths: src/library_catalog/**
---

Keep the import after the bootstrap call in the function that first uses the
parser. The bootstrap helper starts JPype once per process.

## Why

The parser module loads Java classes at import time, which requires a
running JVM.

## Pattern

```python
def load_metadata(path: Path) -> BookMetadata:
    ensure_jvm_started()
    from library_catalog.metadata_bindings import parse_record

    return parse_record(path)
```
