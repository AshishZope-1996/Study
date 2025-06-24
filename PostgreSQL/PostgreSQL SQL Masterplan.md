# PostgreSQL SQL Masterplan

### Audience: Intermediate-level Data Engineer in Finance

### Duration: 30 Days (June 24 to July 23, 2025)

### Goal: Master PostgreSQL from Basics to Advanced + Real-time Scenarios

---

## 📘 1. Core SQL Foundations

### 1.1 SQL Basics

* SELECT, FROM, WHERE
* ORDER BY, LIMIT, OFFSET
* DISTINCT, BETWEEN, IN, LIKE
* Logical operators (AND, OR, NOT)
* Aliases

### 1.2 SQL Data Types

* Numeric: INT, BIGINT, NUMERIC, DECIMAL
* Character: CHAR, VARCHAR, TEXT
* Date/Time: DATE, TIMESTAMP
* Boolean, JSON/JSONB, ARRAY

### 1.3 Data Manipulation Language (DML)

* INSERT INTO
* UPDATE SET
* DELETE FROM
* RETURNING clause
* Transactions: BEGIN, COMMIT, ROLLBACK

### 1.4 Aggregate Functions & Grouping

* COUNT, SUM, AVG, MIN, MAX
* GROUP BY, HAVING
* Filtering aggregates

### 1.5 Joins

* INNER JOIN
* LEFT JOIN, RIGHT JOIN
* FULL OUTER JOIN
* CROSS JOIN
* SELF JOIN

### 1.6 Subqueries

* In SELECT, FROM, WHERE
* Correlated subqueries
* EXISTS, NOT EXISTS

---

## 🧱 2. Database Design

### 2.1 Table Design

* CREATE TABLE
* Column types, defaults
* Constraints: PRIMARY KEY, NOT NULL, UNIQUE
* AUTO\_INCREMENT (SERIAL, IDENTITY)

### 2.2 Relationships & Integrity

* FOREIGN KEY constraints
* ON DELETE / ON UPDATE rules (CASCADE, RESTRICT, SET NULL)

### 2.3 Normalization

* 1NF, 2NF, 3NF
* Identify anomalies
* Denormalization trade-offs

### 2.4 Schema Planning

* Logical vs Physical design
* ERD modeling tools (drawSQL, dbdiagram.io)
* Schema versioning

---

## 🔧 3. Intermediate SQL Techniques

### 3.1 Views

* CREATE VIEW, REPLACE VIEW
* Updatable views
* Materialized views

### 3.2 Common Table Expressions (CTEs)

* WITH clause
* Recursive CTEs

### 3.3 Window Functions

* OVER(), PARTITION BY, ORDER BY
* ROW\_NUMBER(), RANK(), DENSE\_RANK()
* LAG(), LEAD(), FIRST\_VALUE(), LAST\_VALUE()
* Running totals, moving averages

### 3.4 Set Operations

* UNION vs UNION ALL
* INTERSECT
* EXCEPT

### 3.5 CASE Expressions

* Conditional logic inside SELECT
* CASE WHEN THEN ELSE END

---

## ⚙️ 4. PostgreSQL-Specific Features

### 4.1 PostgreSQL Functions

* CREATE FUNCTION (SQL & PL/pgSQL)
* RETURNS VOID/INT/TABLE
* VOLATILE vs STABLE vs IMMUTABLE

### 4.2 Stored Procedures

* CREATE PROCEDURE (Postgres 11+)
* CALL vs SELECT usage

### 4.3 Triggers

* BEFORE/AFTER INSERT/UPDATE/DELETE
* Row vs statement level
* CREATE TRIGGER syntax

### 4.4 Advanced Data Types

* ENUM
* JSONB operations
* ARRAY and unnest()
* HSTORE

### 4.5 Extensions

* PostGIS (geospatial)
* pg\_stat\_statements (performance insights)

---

## 🚀 5. Optimization & Performance

### 5.1 Indexing

* B-tree, Hash, GIN, GiST
* CREATE INDEX, UNIQUE INDEX
* Partial Indexes
* Expression Indexes

### 5.2 Query Tuning

* EXPLAIN / EXPLAIN ANALYZE
* Query plan interpretation
* Optimizer hints

### 5.3 Vacuuming & Analyze

* VACUUM, VACUUM FULL
* ANALYZE
* Autovacuum tuning

### 5.4 Partitioning

* Range Partitioning
* List Partitioning
* Declarative Partitioning

---

## 🔒 6. Security & Access Control

### 6.1 Role Management

* CREATE ROLE / USER
* GRANT / REVOKE permissions
* Role attributes: LOGIN, SUPERUSER, etc.

### 6.2 Row-Level Security (RLS)

* CREATE POLICY
* ENABLE ROW LEVEL SECURITY
* Security barrier views

---

## 🧪 7. Real-time Finance Scenarios

### 7.1 Use Case: Credit Risk Reporting

* Table design: customers, accounts, loans, repayments
* Queries: late payment identification, NPA calculation

### 7.2 Use Case: Investment Portfolio

* Schema for holdings, stocks, transactions
* Queries: portfolio valuation, gain/loss, top performers

### 7.3 Use Case: Transaction Monitoring

* Trigger on suspicious transactions
* Daily/monthly aggregation reports
* Time-window functions for anomaly detection

---

## 📆 30-Day Learning Plan

| Day Range  | Focus Area                                |
| ---------- | ----------------------------------------- |
| Days 1-3   | Core SQL (SELECT, WHERE, JOINs)           |
| Days 4-6   | DML, Aggregate Functions, Subqueries      |
| Days 7-9   | Database Design & Constraints             |
| Days 10-11 | Normalization + Schema Planning           |
| Days 12-13 | Views, CTEs, CASE, Set Ops                |
| Days 14-15 | Window Functions + Hands-on Exercises     |
| Days 16-18 | PostgreSQL Functions, Triggers            |
| Days 19-21 | Indexing + Performance Tuning             |
| Days 22-23 | Security & Access Management              |
| Days 24-27 | Real-world Use Case Projects              |
| Days 28-30 | Final Project, Optimization, Presentation |

---

Let me know if you want this split into separate PDF files, add images/ERDs, or include guided exercises with solutions for each topic.

Here’s a comprehensive **SQL Topic Index** that covers everything from beginner to advanced levels — ideal for learning conceptually and practically with real-world relevance (especially useful for roles like Data Engineer, Analyst, or Developer):

---

## 🔰 **Beginner Level**

### 📘 Basics
### 1. What is SQL? (DDL, DML, DCL, TCL)

**SQL (Structured Query Language)** is the standard language for managing and manipulating relational databases. It is divided into several sub-languages, each serving a specific purpose in the database lifecycle.

---

#### SQL Sub-languages Overview

| Category | Full Form | Purpose | Example Commands |
|----------|-----------|---------|------------------|
| **DDL**  | Data Definition Language | Define and modify database structure (schemas, tables, indexes, etc.) | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML**  | Data Manipulation Language | Manipulate data stored in tables | `SELECT`, `INSERT`, `UPDATE`, `DELETE` |
| **DCL**  | Data Control Language | Control access and permissions to data | `GRANT`, `REVOKE` |
| **TCL**  | Transaction Control Language | Manage transactions and ensure data integrity | `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

---

#### Theoretical Concepts, Syntax, and Examples

##### 1. Data Definition Language (DDL)

- **Purpose:** DDL statements define, alter, or remove database objects such as tables, schemas, and indexes.
- **Common Commands:**
    - `CREATE`: Create new tables, views, indexes, etc.
    - `ALTER`: Modify existing database objects.
    - `DROP`: Remove database objects.
    - `TRUNCATE`: Remove all rows from a table, but keep its structure.

**Example:**
```sql
CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        hire_date DATE DEFAULT CURRENT_DATE
);

ALTER TABLE employees ADD COLUMN department VARCHAR(50);

DROP TABLE employees;
```

**Tips & Notes:**
- DDL statements are auto-committed; changes are permanent and cannot be rolled back in most databases.
- Use DDL with caution, especially in production environments, as changes can affect existing data and application logic.

---

##### 2. Data Manipulation Language (DML)

- **Purpose:** DML statements are used to retrieve and manipulate data within tables.
- **Common Commands:**
    - `SELECT`: Query data from tables.
    - `INSERT`: Add new rows.
    - `UPDATE`: Modify existing rows.
    - `DELETE`: Remove rows.

**Example:**
```sql
INSERT INTO employees (name, department) VALUES ('Alice', 'Finance');

UPDATE employees SET department = 'HR' WHERE name = 'Alice';

DELETE FROM employees WHERE id = 1;

SELECT * FROM employees WHERE department = 'Finance';
```

**Tips & Notes:**
- DML operations can be grouped into transactions, allowing you to commit or roll back changes as a unit.
- Use `RETURNING` in PostgreSQL to get affected rows after `INSERT`, `UPDATE`, or `DELETE`.

---

##### 3. Data Control Language (DCL)

- **Purpose:** DCL statements manage user privileges and access rights to database objects.
- **Common Commands:**
    - `GRANT`: Give privileges to users or roles.
    - `REVOKE`: Remove privileges.

**Example:**
```sql
GRANT SELECT, INSERT ON employees TO analyst;
REVOKE INSERT ON employees FROM analyst;
```

**Tips & Notes:**
- Grant only the minimum required permissions to users (principle of least privilege).
- Use roles to manage permissions for groups of users efficiently.

---

##### 4. Transaction Control Language (TCL)

- **Purpose:** TCL statements manage the changes made by DML statements, ensuring data consistency and integrity.
- **Common Commands:**
    - `BEGIN` or `START TRANSACTION`: Start a new transaction.
    - `COMMIT`: Save all changes made in the transaction.
    - `ROLLBACK`: Undo changes made in the current transaction.
    - `SAVEPOINT`: Set a point within a transaction to which you can roll back.

**Example:**
```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;

-- Using SAVEPOINT
BEGIN;
UPDATE employees SET department = 'IT' WHERE id = 3;
SAVEPOINT before_bonus;
UPDATE employees SET bonus = 1000 WHERE id = 3;
ROLLBACK TO before_bonus;
COMMIT;
```

**Tips & Notes:**
- Transactions ensure **ACID** properties: Atomicity, Consistency, Isolation, Durability.
- Use transactions to group related DML operations, especially in financial or critical systems.
- If an error occurs, use `ROLLBACK` to revert all changes since the last `BEGIN`.

---

#### Key Concepts and Best Practices

- **Transactions**: Group multiple DML statements into a single logical unit. Either all succeed (`COMMIT`) or all fail (`ROLLBACK`).
- **Permissions**: Always grant the least privilege necessary to users and roles.
- **DDL Caution**: Structural changes can impact data integrity and application behavior—test thoroughly before applying to production.
- **Consistency**: Use TCL to maintain data consistency, especially in multi-step operations.

---

#### Summary Table

| Sub-language | Typical Use Case | Example Syntax |
|--------------|-----------------|---------------|
| DDL | Create a new table | `CREATE TABLE ...` |
| DML | Add a new row | `INSERT INTO ...` |
| DCL | Give user access | `GRANT ...` |
| TCL | Confirm changes | `COMMIT;` |

---

**In Practice:**  
A robust SQL workflow involves using DDL to design your schema, DML to manipulate data, DCL to secure your data, and TCL to ensure data integrity through transactions. Mastery of these sub-languages is essential for effective database management and application development.


### 2. Data Types (int, varchar, date, boolean, etc.)

**Data types** define the kind of data a column can store in a PostgreSQL table. Choosing the right data type is crucial for data integrity, performance, and storage efficiency.

---

### Numeric Types

- **INT / INTEGER**: Whole numbers, typically 4 bytes. Range: -2,147,483,648 to 2,147,483,647.
- **BIGINT**: Larger whole numbers, 8 bytes. Range: -9 quintillion to +9 quintillion.
- **SMALLINT**: Smaller whole numbers, 2 bytes. Range: -32,768 to 32,767.
- **NUMERIC / DECIMAL**: Exact precision numbers, ideal for financial data (e.g., `NUMERIC(10,2)` for money).
- **SERIAL / BIGSERIAL**: Auto-incrementing integer (commonly used for primary keys).

**Example:**
```sql
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    balance NUMERIC(12,2) NOT NULL
);
```

---

### Character Types

- **CHAR(n)**: Fixed-length string (pads with spaces if shorter).
- **VARCHAR(n)**: Variable-length string, up to n characters.
- **TEXT**: Variable unlimited length.

**Example:**
```sql
CREATE TABLE customers (
    name VARCHAR(100),
    email TEXT
);
```

---

### Date/Time Types

- **DATE**: Calendar date (YYYY-MM-DD).
- **TIMESTAMP [WITHOUT TIME ZONE]**: Date and time (YYYY-MM-DD HH:MI:SS).
- **TIMESTAMPTZ**: Timestamp with time zone awareness.
- **TIME**: Time of day (HH:MI:SS).
- **INTERVAL**: Time span (e.g., '2 days', '3 hours').

**Example:**
```sql
CREATE TABLE events (
    event_date DATE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

### Boolean Type

- **BOOLEAN**: Stores `TRUE`, `FALSE`, or `NULL`.

**Example:**
```sql
CREATE TABLE flags (
    is_active BOOLEAN DEFAULT TRUE
);
```

---

### Other Common Types

- **UUID**: Universally unique identifier.
- **JSON / JSONB**: Stores JSON data; `JSONB` is binary and more efficient for querying.
- **ARRAY**: Stores arrays of any data type.
- **BYTEA**: Binary data (e.g., images, files).
- **ENUM**: Custom enumerated types for a fixed set of values.

**Example:**
```sql
CREATE TABLE orders (
    id UUID DEFAULT gen_random_uuid(),
    details JSONB,
    tags TEXT[]
);
```

---

**Tips & Best Practices:**
- Use the most restrictive type that fits your data (e.g., `SMALLINT` for small numbers).
- Prefer `TEXT` over large `VARCHAR(n)` unless you need length validation.
- Use `NUMERIC` for currency to avoid rounding errors.
- Use `TIMESTAMPTZ` for time zone–aware timestamps.
- Use `ENUM` for columns with a known, limited set of values.

---

**Summary Table**

| Type         | Example Syntax           | Use Case                        |
|--------------|-------------------------|---------------------------------|
| INT          | `age INT`               | Whole numbers                   |
| VARCHAR      | `name VARCHAR(50)`      | Short text fields               |
| TEXT         | `description TEXT`      | Long text                       |
| DATE         | `dob DATE`              | Birth dates                     |
| TIMESTAMPTZ  | `created_at TIMESTAMPTZ`| Timestamps with time zone       |
| BOOLEAN      | `is_active BOOLEAN`     | True/false flags                |
| NUMERIC      | `amount NUMERIC(10,2)`  | Precise decimals (money, etc.)  |
| JSONB        | `data JSONB`            | Semi-structured data            |
| ARRAY        | `tags TEXT[]`           | List of values                  |

---

**In Practice:**  
Selecting the right data type ensures data accuracy, efficient storage, and optimal query performance. Always consider the nature of your data and future scalability when designing schemas.
3. Basic Clauses: `SELECT`, `FROM`, `WHERE`
4. Filtering Data: `AND`, `OR`, `NOT`, `IN`, `BETWEEN`, `LIKE`
5. Sorting: `ORDER BY`
6. Aliases: `AS`
7. Null handling: `IS NULL`, `COALESCE`, `IFNULL`

---

## 📊 **Intermediate Level**

### 🧮 Aggregation & Grouping

8. Aggregate Functions: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
9. Grouping: `GROUP BY`, `HAVING`

### 🔗 Joins

10. `INNER JOIN`
11. `LEFT JOIN` / `RIGHT JOIN` / `FULL OUTER JOIN`
12. Self Joins
13. Cross Join
14. Anti Joins (`NOT EXISTS`, `NOT IN`, `LEFT JOIN WHERE IS NULL`)

### 🧾 Subqueries

15. Scalar Subqueries
16. Correlated Subqueries
17. `EXISTS`, `IN`, `ANY`, `ALL`

### 📋 Set Operations

18. `UNION` / `UNION ALL`
19. `INTERSECT`
20. `EXCEPT`

---

## 🚀 **Advanced Level**

### 🧱 Table Design

21. Normalization & Denormalization
22. Primary & Foreign Keys
23. Indexing (B-Tree, Hash, Composite, Partial Indexes)
24. Constraints (`UNIQUE`, `CHECK`, `DEFAULT`)

### 🧰 Advanced Queries

25. Window Functions: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LEAD()`, `LAG()`, `NTILE()`
26. CTEs (Common Table Expressions)
27. Recursive CTEs
28. Pivoting & Unpivoting Data
29. JSON Data Handling
30. Arrays and unnesting (esp. in PostgreSQL)

### ⚙️ Performance Tuning

31. Query Optimization
32. Explain Plans (`EXPLAIN`, `EXPLAIN ANALYZE`)
33. Index Usage & Selection
34. Vacuum & Analyze (PostgreSQL-specific)
35. Partitioning Strategies

---

## 🛡️ **Transactions & Security**

### 🗄️ Transactions

36. ACID Properties
37. `BEGIN`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`
38. Isolation Levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable

### 🔒 Security

39. Roles and Permissions
40. Row-Level Security (PostgreSQL)

---

## 🛠️ **Procedural SQL / Server-Specific**

41. PL/pgSQL (PostgreSQL)
42. Stored Procedures & Functions
43. Triggers
44. Event Scheduling (like `cron` jobs in PostgreSQL)
45. Extensions: `pg_stat_statements`, `uuid-ossp`, `citext`

---

## 🧩 **Real-world Scenarios**

46. Audit Logging with Triggers
47. Slowly Changing Dimensions (SCD)
48. Time Series Analysis
49. ETL with SQL
50. CDC (Change Data Capture)
51. Log Analysis with JSON data
52. Handling Dirty Data

---

If you'd like, I can turn this into a **clickable Notion doc, Word doc, PDF**, or break it into **day-wise learning plan**.

Would you like me to do that?
