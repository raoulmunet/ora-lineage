# ora-lineage

Lightweight Oracle SQL lineage: trace source database objects into target objects for ETL-style SQL.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Supported for documented SQL patterns |
> | Oracle Database 23ai | ✅ Supported for documented SQL patterns |
> | Oracle AI Database 26ai | ✅ Supported for documented SQL patterns |
>
> Current lineage is static and offline. Version-specific SQL syntax not recognized by the lightweight parser is reported as a limitation rather than silently inferred.

## Features

- table-level lineage for INSERT...SELECT, MERGE and common DML;
- simple column-level lineage for direct SELECT expressions;
- JSON and Mermaid export;
- built on [ora-core](https://github.com/raoulmunet/ora-core);
- no Oracle credentials required.

## Installation

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-lineage.git"
```

## Usage

```bash
ora-lineage examples/customer_dim.sql
ora-lineage examples/customer_dim.sql --format mermaid
```

## Example

```text
CRM.CUSTOMERS.customer_id  -> DWH.CUSTOMER_DIM.customer_id
CRM.CUSTOMERS.customer_name -> DWH.CUSTOMER_DIM.customer_name
```

## Limitations

Column lineage is deliberately conservative. Complex expressions, PL/SQL dynamic SQL, synonyms, view expansion and metadata-dependent resolution are not guessed.

## License

MIT.
