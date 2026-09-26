# ora-lineage

[![tests](https://github.com/raoulmunet/ora-lineage/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-lineage/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

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

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
