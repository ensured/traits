# Example traits

These traits describe a fictional library catalog service. Its API serves book
records, its CLI offers maintenance commands, and scheduled Airflow jobs refresh
catalog data. The examples illustrate how the trait format captures recurring
patterns across those areas.

Use the [trait specification](../skills/trait-index/SPEC.md) for the file format.
In your own project, take each pattern from the code it describes.

| Trait | Description | When |
|---|---|---|
| [api-errors](api-errors.md) | API routes raise errors defined in the shared API error module | Returning an API error from a route |
| [api-test-clients](api-test-clients.md) | Route tests send requests through the shared api_client fixture | Testing an API route |
| [cli-command-errors](cli-command-errors.md) | CLI commands raise click.ClickException for failures a user can resolve | Handling an expected failure inside a CLI command |
| [cli-command-tests](cli-command-tests.md) | CLI tests invoke commands through Click's CliRunner | Testing a CLI command |
| [cli-console-from-context](cli-console-from-context.md) | CLI commands write through the output streams in the Click context | Writing CLI output |
| [cli-group-module](cli-group-module.md) | Each CLI command group lives in a module with the same name | Adding a command group to the CLI |
| [cli-lazy-generated-client](cli-lazy-generated-client.md) | CLI code imports the generated catalog client inside the function that uses it | Calling the catalog API from a CLI command or helper |
| [collection-module](collection-module.md) | Each MongoDB collection has a module named after it for data access functions | Adding a query or write for a MongoDB collection |
| [dag-identity](dag-identity.md) | An Airflow DAG uses the same name for its file stem, DAG ID, and decorated function | Adding or renaming an Airflow DAG |
| [dag-no-catchup](dag-no-catchup.md) | Scheduled catalog refresh DAGs set catchup=False | Adding or changing a schedule for a catalog refresh DAG |
| [dag-shared-lock](dag-shared-lock.md) | Catalog maintenance DAGs bracket writes with lock setup and teardown tasks | Adding or rewiring an Airflow DAG that makes a bulk catalog change |
| [dag-tasks-are-taskflow](dag-tasks-are-taskflow.md) | Airflow DAGs express catalog transformations as TaskFlow functions | Adding a catalog transformation task |
| [data-source-client](data-source-client.md) | One client module owns HTTP calls to each external data source | Calling an external data source over HTTP |
| [document-ids](document-ids.md) | A MongoDB document ID starts with its collection prefix followed by an underscore and a ULID | Creating a MongoDB document |
| [document-types](document-types.md) | MongoDB document annotations use a TypedDict named for the entity with a Document suffix | Defining or changing the shape of a stored document |
| [indexes](indexes.md) | MongoDB index definitions live in the storage index registry | Adding or changing a MongoDB index |
| [jvm-before-bindings](jvm-before-bindings.md) | An entry point starts the JVM before importing catalog Java bindings | Calling the metadata parser from an entry point |
| [module-logger](module-logger.md) | Modules obtain a module-level logger with logging.getLogger(__name__) | Adding logging to a Python module |
| [route-summary](route-summary.md) | Every catalog route declares a short OpenAPI summary | Adding or changing a FastAPI path operation |
| [scoped-database](scoped-database.md) | Routes that access branch records receive a caller-scoped repository | Adding or changing a route that reads or writes branch records |
| [secrets](secrets.md) | Code loads typed credentials through the shared secret provider | Reading credentials for an integration |
| [task-database](task-database.md) | Tasks open MongoDB through an Airflow connection inside the task body | Writing an Airflow task that needs MongoDB |
| [task-retries](task-retries.md) | Airflow retry policies are declared on individual tasks | Configuring retries for an Airflow task |
| [test-database](test-database.md) | Storage integration tests query a MongoDB instance through an isolated database fixture | Testing MongoDB reads, writes, indexes, or transactions |
| [test-model-factory](test-model-factory.md) | Tests build stored documents with shared fixtures that provide valid defaults | Creating a stored document for a test |
| [unseen-is-not-found](unseen-is-not-found.md) | A missing or out-of-scope catalog record produces the same 404 response | Looking up a branch record requested by a caller |
