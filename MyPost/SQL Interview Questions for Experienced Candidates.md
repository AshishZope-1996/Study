<h1 style="color:#154360; text-align:left; font-size:2.5em; font-weight:bold; margin-bottom:0; letter-spacing:1px;">
    <span style="color:#1C4980;">SQL Interview Questions for Experienced Candidates (3+ years)</span>
</h1>

<hr style="border:1px solidrgb(0, 0, 0);">

<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Data Types & Miscellaneous Concepts</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">

<hr style="border:1px solidrgb(0, 0, 0);">

<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Normalization & Schema Design</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">


<hr style="border:1px solidrgb(0, 0, 0);">

<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Database Design Principles</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">

<hr style="border:1px solidrgb(0, 0, 0);">

<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Indexing Strategies & Keys</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">
<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Indexing Strategies & Keys</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">1. What is a SQL index and what are different types of indexes (clustered, non-clustered, unique, etc.)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    An <b>index</b> in SQL is a database object that improves the speed of data retrieval operations on a table at the cost of additional storage and maintenance overhead. Indexes work like a book's index, allowing the database engine to find rows quickly without scanning the entire table.
</p>

<ul>
    <li><b>Clustered Index:</b> Determines the physical order of data in the table. Each table can have only one clustered index.</li>
    <li><b>Non-Clustered Index:</b> A separate structure from the table data, containing pointers to the actual data rows. A table can have multiple non-clustered indexes.</li>
    <li><b>Unique Index:</b> Ensures that all values in the indexed column(s) are unique.</li>
    <li><b>Composite Index:</b> An index on two or more columns.</li>
    <li><b>Full-Text Index:</b> Used for efficient text searching.</li>
    <li><b>Spatial Index:</b> Used for spatial data types (e.g., geometry, geography).</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

<ul>
    <li><b>Clustered Index:</b></li>
</ul>

```sql
CREATE CLUSTERED INDEX idx_employee_id ON Employees(EmployeeID);
```
<p><i>This creates a clustered index on the <code>EmployeeID</code> column of the <code>Employees</code> table. The data rows will be physically ordered by <code>EmployeeID</code>.</i></p>

<ul>
    <li><b>Non-Clustered Index:</b></li>
</ul>

```sql
CREATE NONCLUSTERED INDEX idx_employee_lastname ON Employees(LastName);
```
<p><i>This creates a non-clustered index on the <code>LastName</code> column. The index is stored separately from the table data and contains pointers to the actual rows.</i></p>

<ul>
    <li><b>Unique Index:</b></li>
</ul>

```sql
CREATE UNIQUE INDEX idx_employee_email ON Employees(Email);
```
<p><i>This ensures that all values in the <code>Email</code> column are unique.</i></p>

<ul>
    <li><b>Composite Index:</b></li>
</ul>

```sql
CREATE INDEX idx_employee_dept_salary ON Employees(DepartmentID, Salary);
```
<p><i>This creates an index on both <code>DepartmentID</code> and <code>Salary</code>. Useful for queries filtering or sorting by both columns.</i></p>

<p>
    <b>Summary:</b> Indexes speed up SELECT queries but can slow down data modification operations (INSERT, UPDATE, DELETE).
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">2. What is the difference between a heap (no clustered index) and a table with a clustered index, and how can you identify a heap table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>heap</b> is a table without a clustered index. Data is stored in no particular order, and row locations are tracked by row identifiers (RIDs). A table with a <b>clustered index</b> stores data rows in the order of the index key.
</p>

<ul>
    <li><b>Heap Table:</b> No clustered index; data is unordered. Identified by querying system catalog views (e.g., <code>sys.indexes</code> in SQL Server) and checking for <code>index_id = 0</code>.</li>
    <li><b>Clustered Index Table:</b> Data is physically ordered by the clustered index key; <code>index_id = 1</code>.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

<ul>
    <li><b>Create a heap (no clustered index):</b></li>
</ul>

```sql
CREATE TABLE HeapTable (
    ID INT,
    Name VARCHAR(50)
);
-- No clustered index created, so this is a heap.
```
<p><i>This table is a heap because no clustered index is defined.</i></p>

<ul>
    <li><b>Add a clustered index:</b></li>
</ul>

```sql
CREATE CLUSTERED INDEX idx_id ON HeapTable(ID);
```
<p><i>Now, <code>HeapTable</code> is no longer a heap; it is ordered by <code>ID</code>.</i></p>

<ul>
    <li><b>Identify a heap in SQL Server:</b></li>
</ul>

```sql
SELECT name, index_id
FROM sys.indexes
WHERE object_id = OBJECT_ID('HeapTable');
```
<p><i>If <code>index_id = 0</code> exists, the table is a heap.</i></p>

<p>
    <b>Summary:</b> Heaps are faster for bulk inserts but slower for searches; clustered indexes improve search performance.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">3. What is the difference between a PRIMARY KEY and a UNIQUE KEY (or unique index) in SQL?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Both <b>PRIMARY KEY</b> and <b>UNIQUE KEY</b> enforce uniqueness on columns, but there are differences:
</p>

<ul>
    <li><b>PRIMARY KEY:</b> Uniquely identifies each row; only one per table; cannot contain NULLs; automatically creates a unique clustered index (if none exists).</li>
    <li><b>UNIQUE KEY:</b> Enforces uniqueness; multiple unique keys allowed per table; columns can contain a single NULL (in most databases); creates a unique non-clustered index by default.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

<ul>
    <li><b>PRIMARY KEY:</b></li>
</ul>

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    Email VARCHAR(100) UNIQUE
);
```
<p><i><code>EmployeeID</code> is the primary key (unique, not null). <code>Email</code> is a unique key (can be null in some databases).</i></p>

<ul>
    <li><b>UNIQUE KEY (explicit):</b></li>
</ul>

```sql
ALTER TABLE Employees ADD CONSTRAINT uq_emp_phone UNIQUE (PhoneNumber);
```
<p><i>This adds a unique constraint to <code>PhoneNumber</code>.</i></p>

<p>
    <b>Summary:</b> Use PRIMARY KEY for the main identifier; use UNIQUE KEY for alternate unique constraints.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">4. What are index “forwarding pointers” in a heap table, and how do they affect query performance?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    In a <b>heap table</b>, when a row is updated and no longer fits in its original location, it may be moved elsewhere. A <b>forwarding pointer</b> is left at the original location, pointing to the new location.
</p>

<ul>
    <li><b>Impact:</b> Causes extra I/O because the database must follow the pointer to find the actual row, slowing down queries.</li>
    <li><b>Resolution:</b> Rebuilding the table or adding a clustered index removes forwarding pointers.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Update a row in a heap table that causes it to move
UPDATE HeapTable SET Name = REPLICATE('A', 1000) WHERE ID = 1;
-- This may create a forwarding pointer if the row can't fit in its original page.
```
<p><i>Queries that access this row will incur extra I/O to follow the pointer.</i></p>

<p>
    <b>Summary:</b> Forwarding pointers degrade performance in heaps with frequent updates.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">5. What is a composite index, and how do you choose the order of columns in it for optimal performance?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>composite index</b> is an index on two or more columns. The order of columns matters for query optimization.
</p>

<ul>
    <li><b>Column Order:</b> Place the most selective (most unique) column first, or the column most often used in WHERE or JOIN conditions.</li>
    <li><b>Index Usage:</b> The index is most effective when queries filter on the leading column(s).</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
CREATE INDEX idx_dept_salary ON Employees(DepartmentID, Salary);
```
<p><i>This index is useful for queries like <code>WHERE DepartmentID = ? AND Salary &gt; ?</code>. If you filter only on <code>Salary</code>, the index may not be used efficiently.</i></p>

<p>
    <b>Summary:</b> Choose column order based on query patterns and selectivity.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">6. When should you use a covering index, and how does it improve the performance of a query?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>covering index</b> includes all columns needed by a query (in the index key or as included columns), so the database can satisfy the query using only the index, without accessing the table data.
</p>

<ul>
    <li><b>Use Case:</b> For frequently run queries that select a small set of columns.</li>
    <li><b>Performance:</b> Reduces I/O and improves speed by avoiding lookups in the base table (bookmark lookups).</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
CREATE INDEX idx_covering ON Employees(DepartmentID) INCLUDE (Salary, FirstName);
```
<p><i>This index covers queries like <code>SELECT Salary, FirstName FROM Employees WHERE DepartmentID = ?</code> because all needed columns are in the index.</i></p>

<p>
    <b>Summary:</b> Covering indexes are powerful for read-heavy workloads with predictable queries.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">7. How does the existence of an index on a column affect INSERT, UPDATE, and DELETE performance on a table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Indexes speed up SELECT queries but add overhead to data modification operations.
</p>

<ul>
    <li><b>INSERT:</b> Indexes must be updated for each new row, increasing insert time.</li>
    <li><b>UPDATE:</b> If indexed columns are updated, the index must be modified, adding overhead.</li>
    <li><b>DELETE:</b> Index entries must be removed, which can slow down deletes.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Insert into a table with indexes
INSERT INTO Employees (EmployeeID, FirstName, LastName) VALUES (1, 'Ashish', 'Zope');
-- The database updates all relevant indexes after the insert.
```
<p><i>More indexes mean more work for each insert, update, or delete operation.</i></p>

<p>
    <b>Summary:</b> More indexes = faster reads, slower writes. Balance based on workload.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">8. What is index selectivity, and why is it important for query optimization?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>Index selectivity</b> is the ratio of the number of distinct values in an indexed column to the total number of rows. High selectivity means many unique values; low selectivity means many duplicates.
</p>

<ul>
    <li><b>Importance:</b> High selectivity indexes are more useful for filtering queries, as they reduce the number of rows scanned.</li>
    <li><b>Low Selectivity:</b> Indexes on columns with few unique values (e.g., gender) are less effective.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- High selectivity: EmployeeID (unique for each row)
CREATE INDEX idx_employee_id ON Employees(EmployeeID);

-- Low selectivity: Gender (few unique values)
CREATE INDEX idx_gender ON Employees(Gender);
```
<p><i>The <code>idx_employee_id</code> index is highly selective and efficient for lookups. The <code>idx_gender</code> index is less useful because many rows share the same value.</i></p>

<p>
    <b>Summary:</b> Use indexes on columns with high selectivity for best performance.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">9. How many clustered indexes can a table have, and why?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A table can have <b>only one clustered index</b> because the data rows can be physically ordered in only one way.
</p>

<ul>
    <li><b>Reason:</b> The clustered index defines the physical storage order of the table.</li>
    <li><b>Non-Clustered Indexes:</b> Multiple non-clustered indexes are allowed.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
-- Only one clustered index allowed
CREATE CLUSTERED INDEX idx_emp_id ON Employees(EmployeeID);

-- Multiple non-clustered indexes allowed
CREATE NONCLUSTERED INDEX idx_emp_email ON Employees(Email);
CREATE NONCLUSTERED INDEX idx_emp_phone ON Employees(PhoneNumber);
```
<p><i>Attempting to create a second clustered index will result in an error.</i></p>

<p>
    <b>Summary:</b> One clustered index per table; unlimited non-clustered indexes (within system limits).
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">10. What is index fragmentation, and how can it be resolved or mitigated in a large database?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>Index fragmentation</b> occurs when the logical order of index pages does not match the physical order, leading to inefficient I/O and slower queries.
</p>

<ul>
    <li><b>Causes:</b> Frequent INSERT, UPDATE, DELETE operations.</li>
    <li><b>Resolution:</b> Rebuild or reorganize indexes using database maintenance commands (e.g., <code>ALTER INDEX REBUILD</code> or <code>REORGANIZE</code> in SQL Server).</li>
    <li><b>Mitigation:</b> Schedule regular index maintenance, monitor fragmentation levels.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
-- Rebuild an index (removes fragmentation)
ALTER INDEX idx_emp_id ON Employees REBUILD;

-- Reorganize an index (less intensive)
ALTER INDEX idx_emp_id ON Employees REORGANIZE;
```
<p><i>Use these commands regularly to keep indexes efficient, especially in large, busy databases.</i></p>

<p>
    <b>Summary:</b> Regular index maintenance is essential for optimal performance in large databases.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Mastering SQL Joins</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">1. What are the different types of SQL joins (<code>INNER JOIN</code>, <code>LEFT JOIN</code>, <code>RIGHT JOIN</code>, <code>FULL JOIN</code>, <code>CROSS JOIN</code>, etc.) and when would you use each?</b>
<p><b style="color:#B9770E;">Answer:</b><br>
    SQL joins are used to combine rows from two or more tables based on related columns. The main types are:
</p>

<ul>
    <li><b>INNER JOIN:</b> Returns only rows with matching values in both tables. Use when you need records present in both tables.</li>
    <li><b>LEFT JOIN (LEFT OUTER JOIN):</b> Returns all rows from the left table and matched rows from the right table. Unmatched rows from the right table return NULLs. Use when you want all records from the left table, regardless of matches.</li>
    <li><b>RIGHT JOIN (RIGHT OUTER JOIN):</b> Returns all rows from the right table and matched rows from the left table. Unmatched rows from the left table return NULLs. Use when you want all records from the right table.</li>
    <li><b>FULL JOIN (FULL OUTER JOIN):</b> Returns all rows when there is a match in either table. Unmatched rows from either side return NULLs. Use when you want all records from both tables.</li>
    <li><b>CROSS JOIN:</b> Returns the Cartesian product of both tables (every row of the first table joined with every row of the second). Use rarely, typically for generating combinations.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b><br>
    <b>INNER JOIN:</b>
</p>

```sql
SELECT a.*, b.*
FROM TableA a
INNER JOIN TableB b ON a.id = b.a_id;
```

<p>
    <b>LEFT JOIN:</b>
</p>

```sql
SELECT a.*, b.*
FROM TableA a
LEFT JOIN TableB b ON a.id = b.a_id;
```

<p>
    <b>RIGHT JOIN:</b>
</p>

```sql
SELECT a.*, b.*
FROM TableA a
RIGHT JOIN TableB b ON a.id = b.a_id;
```

<p>
    <b>FULL OUTER JOIN:</b>
</p>

```sql
SELECT a.*, b.*
FROM TableA a
FULL OUTER JOIN TableB b ON a.id = b.a_id;
```

<p>
    <b>CROSS JOIN:</b>
</p>

```sql
SELECT a.*, b.*
FROM TableA a
CROSS JOIN TableB b;
```

<p>
    <b>Explanation:</b><br>
    - Use <b>INNER JOIN</b> when you only want rows with matches in both tables.<br>
    - Use <b>LEFT JOIN</b> to get all rows from the left table, even if there are no matches in the right.<br>
    - Use <b>RIGHT JOIN</b> to get all rows from the right table, even if there are no matches in the left.<br>
    - Use <b>FULL OUTER JOIN</b> to get all rows from both tables, with NULLs where there are no matches.<br>
    - Use <b>CROSS JOIN</b> to get every combination of rows from both tables (rarely used in practice).
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">2. What is the difference between a <code>CROSS JOIN</code> and a <code>FULL OUTER JOIN</code>?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <code>CROSS JOIN</code> and <code>FULL OUTER JOIN</code> are both used to combine rows from two tables, but they operate very differently:
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Join Type Comparison
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Feature</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">CROSS JOIN</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">FULL OUTER JOIN</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Purpose</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Returns the Cartesian product of both tables (all possible combinations of rows).</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Returns all rows from both tables, matching rows where possible, and filling with NULLs where there is no match.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Join Condition</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No join condition is used.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Join condition is required (typically ON clause).</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Result Size</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Number of rows = rows in TableA × rows in TableB.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Number of rows = all matched rows + unmatched rows from both tables.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Typical Use Case</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Generating all possible combinations (e.g., scheduling, permutations).</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Combining all data from both tables, showing matches and non-matches.</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example:</b></p>

<p><b>CROSS JOIN:</b></p>

```sql
SELECT a.*, b.*
FROM TableA a
CROSS JOIN TableB b;
```

<p><b>FULL OUTER JOIN:</b></p>

```sql
SELECT a.*, b.*
FROM TableA a
FULL OUTER JOIN TableB b ON a.id = b.a_id;
```

<p>
    <b>Summary:</b><br>
    - <b>CROSS JOIN</b> creates every possible pair of rows from both tables.<br>
    - <b>FULL OUTER JOIN</b> returns all rows from both tables, matching where possible, and filling with NULLs where there is no match.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">3. Write a SQL query to retrieve the first and last names of employees along with the names of their managers (given <code>Employees</code> and <code>Managers</code> tables).</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    To retrieve employee names along with their managers' names, you typically join the <code>Employees</code> table with the <code>Managers</code> table using a foreign key (e.g., <code>ManagerID</code> in <code>Employees</code> referencing <code>Managers.ManagerID</code>).
</p>

<ul>
    <li><b>INNER JOIN:</b> Returns only employees who have a matching manager.</li>
    <li><b>LEFT JOIN:</b> Returns all employees, including those without a manager (manager fields will be NULL).</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
SELECT 
    e.FirstName AS EmployeeFirstName,
    e.LastName AS EmployeeLastName,
    m.FirstName AS ManagerFirstName,
    m.LastName AS ManagerLastName
FROM Employees e
LEFT JOIN Managers m ON e.ManagerID = m.ManagerID;
```

<p>
    <b>Explanation:</b><br>
    - <b>LEFT JOIN</b> is used to include employees who may not have a manager.<br>
    - <b>INNER JOIN</b> would exclude employees without a manager.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Employees and Managers Join Result
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Join Type</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Result</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Use Case</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">INNER JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Only employees with a manager are shown.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">When you want to exclude employees without managers.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">LEFT JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All employees are shown; manager fields are NULL if no manager.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">When you want to include all employees, even those without managers.</td>
        </tr>
    </tbody>
</table>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">4. Write a SQL query to find the average salary for each department, given tables <code>Employees</code> (with <code>DepartmentID</code>) and <code>Departments</code> (with <code>DepartmentName</code>).</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    To calculate the average salary for each department, join the <code>Employees</code> table with the <code>Departments</code> table on <code>DepartmentID</code>, then use <code>GROUP BY</code> to aggregate by department.
</p>

<ul>
    <li><b>INNER JOIN:</b> Returns only departments that have at least one employee.</li>
    <li><b>LEFT JOIN:</b> Returns all departments, showing <code>NULL</code> for average salary if there are no employees in a department.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
SELECT 
    d.DepartmentName,
    AVG(e.Salary) AS AverageSalary
FROM Departments d
LEFT JOIN Employees e ON d.DepartmentID = e.DepartmentID
GROUP BY d.DepartmentName;
```

<p>
    <b>Explanation:</b><br>
    - <b>LEFT JOIN</b> ensures all departments are listed, even those without employees.<br>
    - <b>AVG(e.Salary)</b> computes the average salary per department.<br>
    - <b>GROUP BY d.DepartmentName</b> groups results by department.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">5. Write a SQL query to list all products that have never been ordered (products in a <code>Product</code> table with no matching rows in the <code>Orders</code> table).</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    To find products that have never been ordered, you need to identify products in the <code>Product</code> table that do not have any corresponding entries in the <code>Orders</code> table. This is typically done using a <b>LEFT JOIN</b> and checking for <code>NULL</code> in the joined table, or by using a <code>NOT EXISTS</code> or <code>NOT IN</code> subquery.
</p>

<ul>
    <li><b>LEFT JOIN:</b> Returns all products, and for those with no matching order, the order fields will be <code>NULL</code>. Filter these using <code>WHERE Orders.OrderID IS NULL</code>.</li>
    <li><b>NOT EXISTS:</b> Checks for products where no matching order exists.</li>
    <li><b>NOT IN:</b> Selects products whose IDs are not present in the <code>Orders</code> table.</li>
</ul>

<p><b style="color:#B9770E;">Example using LEFT JOIN:</b></p>

```sql
SELECT p.ProductID, p.ProductName
FROM Product p
LEFT JOIN Orders o ON p.ProductID = o.ProductID
WHERE o.OrderID IS NULL;
```

<p><b style="color:#B9770E;">Example using NOT EXISTS:</b></p>

```sql
SELECT p.ProductID, p.ProductName
FROM Product p
WHERE NOT EXISTS (
    SELECT 1 FROM Orders o WHERE o.ProductID = p.ProductID
);
```

<p><b style="color:#B9770E;">Example using NOT IN:</b></p>

```sql
SELECT p.ProductID, p.ProductName
FROM Product p
WHERE p.ProductID NOT IN (
    SELECT o.ProductID FROM Orders o
);
```

<p>
    <b>Explanation:</b><br>
    - <b>LEFT JOIN</b> with <code>WHERE o.OrderID IS NULL</code> finds products with no orders.<br>
    - <b>NOT EXISTS</b> and <b>NOT IN</b> are alternative approaches, often preferred for readability or performance depending on the database.<br>
    - These queries help identify products that may need promotion or removal due to lack of sales.
</p>

<p><b style="color:#B9770E;">Sample Data:</b></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Sample Products Data
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">ProductID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">ProductName</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">101</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish's SQL Book</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">102</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil's Data Guide</td>
        </tr>
    </tbody>
</table>

<p>
    If <code>Ashish's SQL Book</code> and <code>Sunil's Data Guide</code> have never been ordered, they will appear in the result.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Approaches to Find Unordered Products
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Approach</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">When to Use</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">LEFT JOIN + IS NULL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Simple, readable, works well for moderate data sizes.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">NOT EXISTS</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Efficient for large datasets, especially with proper indexing.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">NOT IN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Readable, but can have issues with NULLs in subquery results.</td>
        </tr>
    </tbody>
</table>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">6. Write a SQL query to list all employees who are also managers (for example, employees who appear as managers in the same table).</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    To find employees who are also managers, you typically use a <b>self-join</b> on the <code>Employees</code> table. This means joining the table to itself, matching employees whose <code>EmployeeID</code> appears as a <code>ManagerID</code> for other employees.
</p>

<ul>
    <li><b>Self-Join:</b> The <code>Employees</code> table is joined to itself, using aliases to distinguish between the "employee" and the "manager" roles.</li>
    <li><b>INNER JOIN:</b> Returns only those employees who are referenced as managers by at least one other employee.</li>
    <li><b>DISTINCT:</b> Used to avoid duplicate rows if an employee manages multiple people.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
SELECT DISTINCT
    e.EmployeeID,
    e.FirstName,
    e.LastName
FROM Employees e
INNER JOIN Employees m ON e.EmployeeID = m.ManagerID;
```

<p>
    <b>Explanation:</b><br>
    - <b>e</b> represents the employee who is also a manager.<br>
    - <b>m</b> represents employees who report to a manager.<br>
    - The join condition <code>e.EmployeeID = m.ManagerID</code> finds all employees who are listed as a manager for someone else.<br>
    - <b>DISTINCT</b> ensures each manager appears only once, even if they manage multiple employees.
</p>

<p><b style="color:#B9770E;">Sample Data:</b></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Employees Table
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">EmployeeID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">FirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">LastName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">ManagerID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Patil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">3</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ravi</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Chaudhari</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">4</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Nehara</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
        </tr>
    </tbody>
</table>

<p>
    In this example, <b>Ashish Zope</b> (EmployeeID 1) is a manager for Sunil Patil and Ravi Chaudhari. <b>Sunil Patil</b> (EmployeeID 2) is a manager for Ashish Nehara. The query will return both Ashish Zope and Sunil Patil as employees who are also managers.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Employees Who Are Also Managers
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">EmployeeID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">FirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">LastName</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Patil</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b><br>
    - Use a <b>self-join</b> to identify employees who are also managers.<br>
    - This pattern is common in organizational hierarchies where the manager and employee data are stored in the same table.<br>
    - The approach can be extended to retrieve additional information, such as the number of direct reports each manager has.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">7. What is a <code>self-join</code>, and when might you use it? Provide an example scenario.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>self-join</b> is a regular join, but the table is joined with itself. This is useful when you want to compare rows within the same table or establish relationships between rows in the same table, such as hierarchical or recursive relationships (e.g., employees and their managers).
</p>

<ul>
    <li><b>Self-Join:</b> The same table is referenced twice in the query, using different aliases to distinguish between the two roles (e.g., employee and manager).</li>
    <li><b>Common Use Cases:</b> Organizational hierarchies, bill of materials, finding pairs of related records, comparing rows within a table.</li>
</ul>

<p><b style="color:#B9770E;">Example Scenario:</b><br>
    Suppose you have an <code>Employees</code> table where each employee may have a manager, and both employees and managers are stored in the same table.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Employees Table
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">EmployeeID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">FirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">LastName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">ManagerID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Patil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">3</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ravi</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Chaudhari</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">4</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Nehara</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example Query:</b><br>
    To list each employee along with their manager's name, you can use a self-join:
</p>

```sql
SELECT 
    e.FirstName AS EmployeeFirstName,
    e.LastName AS EmployeeLastName,
    m.FirstName AS ManagerFirstName,
    m.LastName AS ManagerLastName
FROM Employees e
LEFT JOIN Employees m ON e.ManagerID = m.EmployeeID;
```

<p>
    <b>Explanation:</b><br>
    - <b>e</b> is the alias for the employee.<br>
    - <b>m</b> is the alias for the manager.<br>
    - The join condition <code>e.ManagerID = m.EmployeeID</code> links each employee to their manager.<br>
    - <b>LEFT JOIN</b> ensures employees without a manager (e.g., Ashish Zope) are included, with manager fields as NULL.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Employee and Manager Self-Join Result
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Employee</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Manager</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil Patil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish Zope</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ravi Chaudhari</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish Zope</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish Nehara</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil Patil</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Other Example Use Cases:</b>
    <ul>
        <li>Finding all pairs of employees in the same department.</li>
        <li>Comparing rows for duplicates or relationships within the same table.</li>
        <li>Hierarchical queries, such as finding all subordinates of a manager.</li>
    </ul>
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Self-Join vs Regular Join
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Join Type</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Purpose</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Self-Join</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Relate rows within the same table (e.g., employee-manager relationship)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">List employees and their managers using <code>Employees</code> table</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Regular Join</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Relate rows between different tables</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Join <code>Employees</code> and <code>Departments</code> to get department names</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b><br>
    - A <b>self-join</b> is a powerful tool for querying hierarchical or related data within the same table.<br>
    - It is commonly used for organizational charts, bill of materials, and other recursive relationships.<br>
    - Use table aliases to clearly distinguish the roles of each instance of the table in the query.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">8. How would you join more than two tables in a single SQL query? What factors affect the performance when joining multiple tables?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Joining more than two tables in a single SQL query is common in real-world scenarios, such as retrieving employee details along with their department and manager information. This is achieved by chaining multiple <b>JOIN</b> clauses together, each connecting two tables at a time.
</p>

<ul>
    <li><b>Multiple Joins:</b> You can join as many tables as needed by specifying additional <code>JOIN</code> clauses, using appropriate join conditions for each pair.</li>
    <li><b>Types of Joins:</b> Any combination of <code>INNER JOIN</code>, <code>LEFT JOIN</code>, <code>RIGHT JOIN</code>, etc., can be used depending on the data you want to retrieve.</li>
    <li><b>Aliases:</b> Table aliases help keep queries readable, especially when joining several tables.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b><br>
    Suppose you have the following tables:
</p>

<ul>
    <li><b>Employees</b> (<code>EmployeeID</code>, <code>FirstName</code>, <code>LastName</code>, <code>DepartmentID</code>, <code>ManagerID</code>, <code>Salary</code>)</li>
    <li><b>Departments</b> (<code>DepartmentID</code>, <code>DepartmentName</code>)</li>
    <li><b>Managers</b> (<code>ManagerID</code>, <code>FirstName</code>, <code>LastName</code>)</li>
</ul>

<p>
    To retrieve each employee's name, department, manager's name, and salary:
</p>

```sql
SELECT 
    e.FirstName AS EmployeeFirstName,
    e.LastName AS EmployeeLastName,
    d.DepartmentName,
    m.FirstName AS ManagerFirstName,
    m.LastName AS ManagerLastName,
    e.Salary
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID
LEFT JOIN Managers m ON e.ManagerID = m.ManagerID;
```

<p>
    <b>Explanation:</b><br>
    - <b>LEFT JOIN</b> is used to include all employees, even if they do not have a department or manager.<br>
    - Each <code>JOIN</code> connects two tables at a time, building up the result set.<br>
    - Aliases (<code>e</code>, <code>d</code>, <code>m</code>) make the query concise and readable.
</p>

<p><b style="color:#B9770E;">Sample Data:</b></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Employees Table
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">EmployeeID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">FirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">LastName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">ManagerID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Salary</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">10</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">120000</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Patil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">20</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">95000</td>
        </tr>
    </tbody>
</table>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Departments Table
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentName</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">10</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Engineering</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">20</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data Science</td>
        </tr>
    </tbody>
</table>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Managers Table
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">ManagerID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">FirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">LastName</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Result:</b></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Query Result for Employee, Department, and Manager
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">EmployeeFirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">EmployeeLastName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">ManagerFirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">ManagerLastName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Salary</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Engineering</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">120000</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Patil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data Science</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">95000</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Performance Factors When Joining Multiple Tables:</b></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Performance Factors
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Factor</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Impact</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Best Practice</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Indexes</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Lack of indexes on join columns can cause slow queries.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Create indexes on columns used in <code>ON</code> clauses (e.g., <code>DepartmentID</code>, <code>ManagerID</code>).</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Join Order</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Joining large tables first can increase intermediate result size.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Join smaller or filtered tables first when possible.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Join Type</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">OUTER joins can be slower than INNER joins due to more data being returned.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Use <code>INNER JOIN</code> when possible for better performance.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data Volume</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Large tables increase processing time and memory usage.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Filter data early using <code>WHERE</code> clauses.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Query Complexity</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Complex queries with many joins can be harder to optimize.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Break down complex queries or use views for clarity.</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b><br>
    - You can join multiple tables by chaining <code>JOIN</code> clauses.<br>
    - Use table aliases for readability.<br>
    - Performance depends on indexes, join order, join type, data volume, and query complexity.<br>
    - Always test and optimize queries, especially as the number of joins increases.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">9. Explain how an <code>OUTER JOIN</code> works when one side has no matching rows. How does this differ from an <code>INNER JOIN</code> in practice?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    An <b>OUTER JOIN</b> returns all rows from one (or both) tables, even if there are no matching rows in the joined table. When there is no match, the columns from the missing side are filled with <code>NULL</code> values. In contrast, an <b>INNER JOIN</b> only returns rows where there is a match in both tables.
</p>

<ul>
    <li><b>LEFT OUTER JOIN (LEFT JOIN):</b> Returns all rows from the left table (<code>Employees</code>), and matched rows from the right table (<code>Departments</code>). If there is no match, right table columns are <code>NULL</code>.</li>
    <li><b>RIGHT OUTER JOIN (RIGHT JOIN):</b> Returns all rows from the right table, and matched rows from the left table. If there is no match, left table columns are <code>NULL</code>.</li>
    <li><b>FULL OUTER JOIN:</b> Returns all rows from both tables, with <code>NULL</code> in columns where there is no match.</li>
    <li><b>INNER JOIN:</b> Returns only rows where there is a match in both tables.</li>
</ul>

<p><b style="color:#B9770E;">Example Scenario:</b><br>
    Suppose you have the following tables:
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Employees Table
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">EmployeeID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">FirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">LastName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentID</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">10</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Patil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">20</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">3</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ravi</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Chaudhari</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL</td>
        </tr>
    </tbody>
</table>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Departments Table
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentID</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentName</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">10</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Engineering</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">20</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data Science</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">30</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">HR</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">LEFT OUTER JOIN Example:</b></p>

```sql
SELECT 
    e.FirstName, 
    e.LastName, 
    d.DepartmentName
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```

<p><b>Result:</b></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        LEFT OUTER JOIN Result
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">FirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">LastName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentName</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Engineering</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Patil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data Science</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ravi</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Chaudhari</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL</td>
        </tr>
    </tbody>
</table>

<p>
    Notice that <b>Ravi Chaudhari</b> has no department, so <code>DepartmentName</code> is <code>NULL</code>. If you used an <b>INNER JOIN</b>, Ravi would not appear in the result.
</p>

<p><b style="color:#B9770E;">INNER JOIN Example:</b></p>

```sql
SELECT 
    e.FirstName, 
    e.LastName, 
    d.DepartmentName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID;
```

<p><b>Result:</b></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        INNER JOIN Result
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">FirstName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">LastName</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">DepartmentName</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ashish</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Zope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Engineering</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sunil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Patil</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data Science</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Explanation:</b><br>
    - <b>OUTER JOIN</b> includes all rows from one or both tables, filling in <code>NULL</code> where there is no match.<br>
    - <b>INNER JOIN</b> only includes rows where there is a match in both tables.<br>
    - Use <b>OUTER JOIN</b> when you want to see all records from one side, even if there are no matches on the other side (e.g., all employees, even those without a department).
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        INNER JOIN vs OUTER JOIN
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Join Type</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Rows Returned</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">NULLs for Missing Data?</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example Use Case</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">INNER JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Only matching rows</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Employees with a department</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">LEFT OUTER JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All left table rows</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes, for right table columns</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All employees, even those without a department</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">RIGHT OUTER JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All right table rows</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes, for left table columns</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All departments, even those without employees</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">FULL OUTER JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All rows from both tables</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes, for missing matches on either side</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All employees and all departments, showing all possible matches and non-matches</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b><br>
    - <b>OUTER JOIN</b> is useful for finding unmatched data (e.g., employees without departments, or departments without employees).<br>
    - <b>INNER JOIN</b> is used when you only care about records that exist in both tables.<br>
    - In practice, <b>OUTER JOIN</b> helps in reporting, auditing, and identifying missing relationships in your data.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Working with Views</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">1. What is a database view, and can you update data in the base tables through it?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>view</b> is a virtual table based on the result of a SQL query. It does not store data itself but presents data from one or more tables. You can often update base tables through a view if the view is <b>simple</b> (e.g., based on a single table, no aggregates, no GROUP BY). Complex views (with joins, aggregates, etc.) are usually <b>read-only</b>.
</p>

<ul>
    <li><b>Updatable View:</b> Simple SELECT from one table, no aggregates or DISTINCT.</li>
    <li><b>Read-Only View:</b> Contains joins, GROUP BY, aggregate functions, or DISTINCT.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Simple updatable view
CREATE VIEW vw_EmployeeNames AS
SELECT EmployeeID, FirstName, LastName FROM Employees;

-- Update through the view
UPDATE vw_EmployeeNames SET FirstName = 'John' WHERE EmployeeID = 1;
```

<p>
    <b>Summary:</b> Views provide a way to simplify queries and restrict access. Updates are allowed only for simple views.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">2. What is the difference between a standard view and a materialized (or indexed) view?</b>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Standard View vs Materialized View
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Feature</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Standard View</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Materialized/Indexed View</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Storage</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No data stored; query runs each time</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Stores result set physically</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Performance</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Slower for complex queries</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Faster for repeated access</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Refresh</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Always current</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Needs refresh (manual or automatic)</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Use standard views for abstraction; use materialized views for performance on large, complex queries.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">3. What happens if a materialized view is being refreshed (complete refresh) and a user queries it at the same time?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    During a <b>complete refresh</b>, the materialized view is rebuilt. If a user queries it during refresh:
</p>
<ul>
    <li>Most databases (e.g., Oracle) serve the <b>old data</b> until the refresh completes, ensuring consistency.</li>
    <li>Some systems may block queries or return an error if the view is unavailable.</li>
</ul>
<p>
    <b>Tip:</b> Use <code>FAST REFRESH</code> or schedule refreshes during low-traffic periods to minimize impact.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">4. When would you use a view in a database design? What benefits do views provide (e.g. security, abstraction)?</b>

<ul>
    <li><b>Security:</b> Restrict access to sensitive columns or rows.</li>
    <li><b>Abstraction:</b> Hide complex joins or calculations from end users.</li>
    <li><b>Simplification:</b> Provide a simple interface for reporting or applications.</li>
    <li><b>Consistency:</b> Standardize business logic in one place.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Hide salary details from most users
CREATE VIEW vw_PublicEmployees AS
SELECT EmployeeID, FirstName, LastName FROM Employees;
```

<p>
    <b>Summary:</b> Views help enforce security, simplify access, and centralize logic.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">5. Can you create an index on a view? If so, what are the implications (e.g. indexed view in SQL Server)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Yes, in some databases (like SQL Server), you can create an <b>indexed view</b> (also called a materialized view). This physically stores the view's result set and creates an index on it.
</p>
<ul>
    <li><b>Benefits:</b> Greatly improves performance for complex aggregations or joins.</li>
    <li><b>Drawbacks:</b> Increases storage and maintenance overhead; restrictions on view definition (e.g., must be deterministic).</li>
</ul>

<p><b style="color:#B9770E;">Example (SQL Server):</b></p>

```sql
CREATE VIEW vw_SalesSummary WITH SCHEMABINDING AS
SELECT StoreID, SUM(SalesAmount) AS TotalSales
FROM dbo.Sales
GROUP BY StoreID;

CREATE UNIQUE CLUSTERED INDEX idx_SalesSummary_StoreID ON vw_SalesSummary(StoreID);
```

<p>
    <b>Summary:</b> Indexed views boost performance but add complexity and storage cost.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">6. How do you modify or drop a view if the underlying table schema changes?</b>

<ul>
    <li><b>Modify:</b> Use <code>CREATE OR REPLACE VIEW</code> (Oracle, PostgreSQL) or <code>ALTER VIEW</code> (SQL Server) to update the view definition.</li>
    <li><b>Drop:</b> Use <code>DROP VIEW view_name;</code> to remove the view.</li>
    <li><b>Tip:</b> If a column used in the view is dropped from the base table, the view becomes invalid and must be recreated or altered.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Modify a view
CREATE OR REPLACE VIEW vw_EmployeeNames AS
SELECT EmployeeID, FirstName FROM Employees;

-- Drop a view
DROP VIEW vw_EmployeeNames;
```

<p>
    <b>Summary:</b> Always update or drop dependent views after schema changes to base tables.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">7. What is the difference between a view and a temporary table?</b>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        View vs Temporary Table
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Aspect</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">View</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Temporary Table</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Persistence</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Definition persists; data is always current</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Exists only for session or transaction</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Storage</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No data stored (unless materialized)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Physically stores data</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Use Case</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Reusable query abstraction, security</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Intermediate results, complex processing</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Use views for abstraction and security; use temporary tables for storing intermediate results in complex queries.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Stored Procedures & Functions</b>
</blockquote>
<b style="color:#1C4980;font-weight:bold;">1. What is the difference between a stored procedure and a user-defined function in SQL (aside from return value)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>stored procedure</b> is a precompiled collection of SQL statements that can perform actions such as modifying data, controlling transactions, and returning results. A <b>user-defined function (UDF)</b> is a routine that returns a value (scalar or table) and is typically used in SELECT, WHERE, or JOIN clauses.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Stored Procedure vs User-Defined Function
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Aspect</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Stored Procedure</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">User-Defined Function</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Can modify data</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No (except in some DBs with special permissions)</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Can be used in SELECT</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Transaction control</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Return type</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">None, scalar, or result set</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Scalar or table</td>
        </tr>
    </tbody>
</table>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">2. What are the advantages and disadvantages of using stored procedures?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>Advantages:</b>
</p>
<ul>
    <li>Encapsulate business logic in the database</li>
    <li>Improve performance via precompilation</li>
    <li>Enhance security (grant EXECUTE instead of table access)</li>
    <li>Reduce network traffic (batch multiple statements)</li>
</ul>
<p><b>Disadvantages:</b></p>
<ul>
    <li>Harder to version and deploy than application code</li>
    <li>May increase database server load</li>
    <li>Logic split between app and DB can complicate maintenance</li>
</ul>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">3. Can you perform INSERT/UPDATE/DELETE operations inside a SQL function? Why or why not?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    In most databases (e.g., SQL Server, PostgreSQL), <b>user-defined functions cannot perform INSERT/UPDATE/DELETE</b> operations on tables. This restriction ensures functions are deterministic and side-effect free, making them safe for use in queries. Some databases (like Oracle with autonomous transactions) allow limited exceptions.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">4. What is a table-valued function and when would you use one in a query?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>table-valued function (TVF)</b> returns a table as its result. You use TVFs in the FROM clause of a query, similar to a regular table or view. TVFs are useful for encapsulating reusable query logic that returns sets of rows.
</p>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- SQL Server example
CREATE FUNCTION dbo.GetEmployeesByDept(@DeptID INT)
RETURNS TABLE
AS
RETURN (
    SELECT EmployeeID, FirstName, LastName
    FROM Employees
    WHERE DepartmentID = @DeptID
);

-- Usage
SELECT * FROM dbo.GetEmployeesByDept(10);
```

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">5. When would you use a stored procedure instead of inline SQL queries in an application?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use a <b>stored procedure</b> when you want to:</p>
<ul>
    <li>Centralize and reuse business logic</li>
    <li>Improve security by restricting direct table access</li>
    <li>Reduce SQL injection risk (parameterized execution)</li>
    <li>Optimize performance for complex or repetitive operations</li>
    <li>Batch multiple statements in a single call</li>
</ul>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">6. How do you pass parameters to and receive results from stored procedures?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>Parameters</b> are passed to stored procedures as input, output, or input/output arguments. Results can be returned via output parameters, result sets (SELECT), or return values.
</p>

<p><b style="color:#B9770E;">Example (SQL Server):</b></p>

```sql
-- Define procedure
CREATE PROCEDURE GetEmployeeByID
    @EmpID INT,
    @FirstName NVARCHAR(50) OUTPUT
AS
BEGIN
    SELECT @FirstName = FirstName FROM Employees WHERE EmployeeID = @EmpID;
END;

-- Execute procedure
DECLARE @Name NVARCHAR(50);
EXEC GetEmployeeByID 1, @Name OUTPUT;
SELECT @Name;
```

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">7. How would you debug or test a slow or failing stored procedure in production?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <ul>
        <li>Capture execution plans to identify bottlenecks</li>
        <li>Use logging or print statements for tracing</li>
        <li>Test with sample data in a development environment</li>
        <li>Check for blocking, deadlocks, or resource waits</li>
        <li>Review recent schema or data changes</li>
        <li>Use database profiling tools (e.g., SQL Profiler, Extended Events)</li>
    </ul>
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">8. How do you grant a user permission to execute a specific stored procedure?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use the <code>GRANT EXECUTE</code> statement to allow a user to run a stored procedure.
</p>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
GRANT EXECUTE ON OBJECT::GetEmployeeByID TO username;
```
<p><i>This grants the user permission to execute the <code>GetEmployeeByID</code> procedure.</i></p>

<hr style="border:1px solidrgb(0, 0, 0);">

<hr style="border:1px solidrgb(0, 0, 0);">
<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Triggers & Automation</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">1. What is a trigger in SQL, and when would you use one? Give an example use case.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>trigger</b> is a special kind of stored procedure that automatically executes in response to certain events on a table or view (such as <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code>). Triggers are used for enforcing business rules, auditing changes, maintaining derived data, or automating tasks.
</p>

<ul>
    <li><b>Use Cases:</b> Auditing changes, enforcing complex constraints, cascading updates/deletes, logging, or synchronizing tables.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Audit trigger: Log every employee salary change
CREATE TRIGGER trg_AuditSalaryChange
ON Employees
AFTER UPDATE
AS
BEGIN
    INSERT INTO SalaryAudit (EmployeeID, OldSalary, NewSalary, ChangedAt)
    SELECT i.EmployeeID, d.Salary, i.Salary, GETDATE()
    FROM inserted i
    JOIN deleted d ON i.EmployeeID = d.EmployeeID
    WHERE i.Salary <> d.Salary;
END;
```
<p><i>This trigger logs salary changes to an audit table whenever an employee's salary is updated.</i></p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">2. What is the difference between an AFTER trigger and an INSTEAD OF trigger (e.g. in SQL Server)?</b>

<b style="color:#1C4980;font-weight:bold;">3. What are the “inserted” and “deleted” magic tables in SQL Server triggers?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    In SQL Server, <b>inserted</b> and <b>deleted</b> are special (magic) tables available inside triggers:
</p>

<ul>
    <li><b>inserted:</b> Holds the new rows for <code>INSERT</code> and <code>UPDATE</code> operations.</li>
    <li><b>deleted:</b> Holds the old rows for <code>DELETE</code> and <code>UPDATE</code> operations.</li>
</ul>

<p>
    <b>Example:</b> In an <code>AFTER UPDATE</code> trigger, <code>inserted</code> has new values, <code>deleted</code> has old values.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">4. How can triggers be used to enforce business rules or data integrity (e.g. auditing changes, simulating foreign keys)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Triggers can enforce business rules by validating data, preventing invalid changes, logging modifications, or simulating constraints not natively supported (e.g., cascading deletes, custom referential integrity).
</p>

<ul>
    <li><b>Auditing:</b> Log changes to sensitive data (e.g., salary updates).</li>
    <li><b>Enforcing Rules:</b> Prevent deletion of parent rows if child rows exist (simulate foreign key).</li>
    <li><b>Data Integrity:</b> Automatically update related tables or maintain derived columns.</li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Prevent deleting a department if employees exist
CREATE TRIGGER trg_PreventDeptDelete
ON Departments
INSTEAD OF DELETE
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Employees e JOIN deleted d ON e.DepartmentID = d.DepartmentID)
        RAISERROR('Cannot delete department with employees.', 16, 1);
    ELSE
        DELETE FROM Departments WHERE DepartmentID IN (SELECT DepartmentID FROM deleted);
END;
```
<p><i>This trigger blocks deletion of a department if employees are assigned to it.</i></p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">5. What are the potential drawbacks of using triggers (such as performance impact or hidden logic)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Triggers can introduce hidden logic and performance overhead:
</p>

<ul>
    <li><b>Performance:</b> Triggers add extra processing to DML operations, potentially slowing down inserts, updates, or deletes.</li>
    <li><b>Hidden Logic:</b> Business rules in triggers may not be obvious to developers, making debugging and maintenance harder.</li>
    <li><b>Complexity:</b> Nested or recursive triggers can cause unexpected behavior.</li>
    <li><b>Portability:</b> Trigger syntax and behavior can vary between database systems.</li>
</ul>

<p>
    <b>Summary:</b> Use triggers judiciously; document their behavior and monitor performance.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">6. How do INSTEAD OF triggers on a view work?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>INSTEAD OF triggers</b> on a view intercept <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code> operations and allow you to define custom logic for how those operations are handled. This is useful for updatable views that join multiple tables or require special handling.
</p>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Allow updates to a view that joins Employees and Departments
CREATE VIEW vw_EmployeeDept AS
SELECT e.EmployeeID, e.FirstName, d.DepartmentName
FROM Employees e
JOIN Departments d ON e.DepartmentID = d.DepartmentID;

CREATE TRIGGER trg_UpdateEmpDept
ON vw_EmployeeDept
INSTEAD OF UPDATE
AS
BEGIN
    UPDATE Employees
    SET FirstName = i.FirstName
    FROM inserted i
    WHERE Employees.EmployeeID = i.EmployeeID;
END;
```
<p><i>This trigger allows updates to the <code>FirstName</code> column via the view.</i></p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">7. Can triggers call stored procedures, and are there any limitations to doing that?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Yes, triggers can call stored procedures. However, there are limitations:
</p>

<ul>
    <li><b>Side Effects:</b> Procedures called from triggers should not commit/rollback transactions independently.</li>
    <li><b>Performance:</b> Long-running procedures can slow down DML operations.</li>
    <li><b>Recursion:</b> Be careful to avoid recursive trigger/procedure calls.</li>
    <li><b>Permissions:</b> The trigger must have permission to execute the procedure.</li>
</ul>

<p>
    <b>Summary:</b> Triggers can call stored procedures, but keep logic efficient and avoid transactional conflicts.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Transactions & Concurrency Control</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">1. What are the ACID properties of a database transaction (atomicity, consistency, isolation, durability)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>ACID</b> stands for:
</p>
<ul>
    <li><b>Atomicity:</b> All operations in a transaction succeed or all fail (no partial changes).</li>
    <li><b>Consistency:</b> Transactions bring the database from one valid state to another, preserving rules.</li>
    <li><b>Isolation:</b> Concurrent transactions do not interfere; intermediate states are hidden.</li>
    <li><b>Durability:</b> Once committed, changes are permanent even after a crash.</li>
</ul>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">2. What are the different SQL isolation levels (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE), and what phenomena do they prevent (dirty reads, non-repeatable reads, phantom reads)?</b>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        SQL Isolation Levels and Phenomena
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Level</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Dirty Reads</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Non-Repeatable Reads</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Phantom Reads</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">READ UNCOMMITTED</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Possible</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">READ COMMITTED</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Possible</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">REPEATABLE READ</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Possible</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SERIALIZABLE</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevented</td>
        </tr>
    </tbody>
</table>
<p>
    <b>Summary:</b> Higher isolation = fewer anomalies, but more locking and lower concurrency.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">3. What is a deadlock in database terms, and how can you prevent or resolve deadlocks?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>deadlock</b> occurs when two or more transactions block each other, each waiting for the other to release locks. Neither can proceed.
</p>
<ul>
    <li><b>Prevention:</b> Access tables in the same order, keep transactions short, use lower isolation levels if possible.</li>
    <li><b>Resolution:</b> The database detects deadlocks and aborts (rolls back) one transaction (the "victim").</li>
</ul>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">4. How do you control transactions in SQL (BEGIN, COMMIT, ROLLBACK)? Give an example of using a transaction in a stored procedure or batch.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use <code>BEGIN TRANSACTION</code> to start, <code>COMMIT</code> to save, and <code>ROLLBACK</code> to undo.
</p>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
BEGIN TRANSACTION;
    UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;
    UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 2;
IF @@ERROR <> 0
    ROLLBACK;
ELSE
    COMMIT;
```
<p><i>This ensures both updates succeed or both are undone.</i></p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">5. If you run a long SELECT query on a table while another transaction is updating rows in that table, will your session see the old data or new data by default? (Consider default isolation level behavior.)</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    By default (READ COMMITTED), your SELECT sees only committed data at the time each row is read. You may see new data if the update commits before your SELECT reads that row.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">6. What is the difference between pessimistic and optimistic locking, and when would you use each?</b>

<ul>
    <li><b>Pessimistic Locking:</b> Locks data when read, blocking others until transaction ends. Use for high-conflict scenarios.</li>
    <li><b>Optimistic Locking:</b> No locks when reading; checks for changes before writing (e.g., using a version column). Use when conflicts are rare.</li>
</ul>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">7. What is a savepoint in a transaction, and how do you use it?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>savepoint</b> marks a point within a transaction to which you can roll back without affecting earlier work.
</p>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
BEGIN TRANSACTION;
    UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;
    SAVE TRANSACTION Save1;
    UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 2;
    -- If needed:
    ROLLBACK TRANSACTION Save1;
COMMIT;
```

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">8. How do two-phase commit protocols work in distributed transactions?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>Two-phase commit</b> ensures all participants in a distributed transaction agree to commit or roll back:
</p>
<ol>
    <li><b>Prepare phase:</b> Coordinator asks all nodes if they can commit.</li>
    <li><b>Commit phase:</b> If all agree, coordinator tells all to commit; otherwise, tells all to roll back.</li>
</ol>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">9. How can you identify and terminate a blocking or long-running transaction in a SQL database?</b>

<ul>
    <li><b>Identify:</b> Use system views (e.g., <code>sys.dm_exec_requests</code>, <code>sp_who2</code> in SQL Server) to find blocking sessions.</li>
    <li><b>Terminate:</b> Use <code>KILL session_id</code> (SQL Server) or <code>ALTER SYSTEM KILL SESSION</code> (Oracle) to end the session.</li>
</ul>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">10. What is deadlock detection, and how does the database engine choose a deadlock victim?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    The database periodically checks for deadlocks. When found, it picks a "victim" transaction to roll back (usually the one with the least cost or least work done) to break the cycle and let others proceed.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Performance Tuning & Query Optimization</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">1. What is a query execution plan and how do you use it to improve performance?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>query execution plan</b> is a step-by-step breakdown of how the database engine will execute a SQL query. It shows the order of operations, join types, index usage, and estimated costs. Reviewing the plan helps identify bottlenecks (e.g., full table scans, missing indexes) and guides query optimization.
</p>

<ul>
    <li><b>How to View:</b> Use <code>EXPLAIN</code> (MySQL/PostgreSQL), <code>SET SHOWPLAN</code> (SQL Server), or graphical tools in database GUIs.</li>
    <li><b>Optimization:</b> Add indexes, rewrite queries, or adjust schema based on plan findings.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Common Execution Plan Operators
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Operator</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Table Scan</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Reads all rows; slow for large tables</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Index Seek</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Efficient lookup using an index</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Nested Loop Join</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Good for small result sets</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Hash Join</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Efficient for large, unsorted data</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
EXPLAIN SELECT * FROM Employees WHERE DepartmentID = 10;
```
<p><i>This shows how the query will be executed and whether an index is used.</i></p>

<p>
    <b>Summary:</b> Always review execution plans for slow queries to find and fix performance issues.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">2. How would you optimize a slow SQL query in production?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Optimizing a slow query involves analyzing execution plans, indexing, and query rewriting.
</p>

<ul>
    <li>Add indexes on columns used in WHERE, JOIN, and ORDER BY clauses.</li>
    <li>Rewrite queries to avoid unnecessary subqueries or correlated subqueries.</li>
    <li>Avoid <code>SELECT *</code>; select only needed columns.</li>
    <li>Use query execution plans to identify bottlenecks.</li>
    <li>Partition large tables if appropriate.</li>
    <li>Update statistics and rebuild fragmented indexes.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Optimization Techniques Comparison
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Technique</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">When to Use</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Indexing</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Frequent filtering or joining on columns</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Query Rewrite</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Complex or inefficient queries</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Partitioning</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Very large tables</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Use a combination of indexing, query rewriting, and maintenance for best performance.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">3. What is the difference between UNION and UNION ALL in SQL, and when would you use each?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>UNION</b> combines results from two queries and removes duplicate rows. <b>UNION ALL</b> combines results and keeps all duplicates.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        UNION vs UNION ALL
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Operator</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Duplicates Removed?</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Performance</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">UNION</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Slower (needs sorting/deduplication)</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">UNION ALL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Faster</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT Name FROM Employees
UNION
SELECT Name FROM Managers;

SELECT Name FROM Employees
UNION ALL
SELECT Name FROM Managers;
```

<p>
    <b>Summary:</b> Use <b>UNION ALL</b> for better performance if you do not need to remove duplicates.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">4. How can you find duplicate rows in a table using SQL?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use <code>GROUP BY</code> and <code>HAVING COUNT(*) > 1</code> to find duplicates based on one or more columns.
</p>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT column1, column2, COUNT(*)
FROM table_name
GROUP BY column1, column2
HAVING COUNT(*) > 1;
```
<p><i>This finds rows where (column1, column2) are duplicated.</i></p>

<p>
    <b>Summary:</b> Adjust columns in <code>GROUP BY</code> to match your definition of "duplicate."
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">5. Write a SQL query to find the 10th highest salary in an Employee table.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use <code>ORDER BY</code> with <code>LIMIT</code> and <code>OFFSET</code> or a subquery with <code>DISTINCT</code> to get the 10th highest unique salary.
</p>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT MIN(Salary) AS TenthHighestSalary
FROM (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 10
) AS Top10;
```
<p><i>This returns the 10th highest unique salary.</i></p>

<p>
    <b>Summary:</b> Use <code>DISTINCT</code> to ignore duplicates; adjust <code>LIMIT</code> for other ranks.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">6. How would you retrieve the last 5 records (by date or ID) from a table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Order by the relevant column in descending order and use <code>LIMIT</code>.
</p>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT *
FROM table_name
ORDER BY date_column DESC
LIMIT 5;
```
<p><i>Replace <code>date_column</code> with your ordering column.</i></p>

<p>
    <b>Summary:</b> This returns the most recent 5 records.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">7. Write a SQL query to exclude specific values (e.g., select all rows except those where ID is X or Y).</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use <code>NOT IN</code> or <code>!=</code> in the WHERE clause to exclude specific values.
</p>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT *
FROM Student
WHERE ID NOT IN (X, Y);
```

<p>
    <b>Summary:</b> Replace <code>X</code> and <code>Y</code> with the IDs to exclude.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">8. How do you retrieve the Nth record (e.g., the 3rd record) from a table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use <code>ORDER BY</code> with <code>LIMIT</code> and <code>OFFSET</code> to get the Nth row.
</p>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT *
FROM table_name
ORDER BY ordering_column
LIMIT 1 OFFSET 2; -- 0-based offset; 2 = 3rd row
```

<p>
    <b>Summary:</b> Adjust <code>OFFSET</code> for the desired row number (N-1).
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">9. How do you obtain the CREATE TABLE DDL for an existing table in SQL?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use database-specific commands or tools to get the DDL.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        DDL Retrieval Methods
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Database</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Command/Tool</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">MySQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SHOW CREATE TABLE table_name;</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">PostgreSQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>pg_dump</code> or query <code>information_schema</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SQL Server</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">SSMS "Script Table as" or <code>sp_helptext</code> for views/procs</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Use the appropriate command for your database to script table definitions.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">10. Explain the difference between the RANK() and DENSE_RANK() window functions.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Both functions assign ranks to rows based on ordering, but handle ties differently.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        RANK() vs DENSE_RANK()
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Function</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Ranking Behavior</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example Output</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">RANK()</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Skips rank after ties</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1, 2, 2, 4</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">DENSE_RANK()</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No gaps after ties</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1, 2, 2, 3</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Use <b>RANK()</b> when you want gaps after ties; use <b>DENSE_RANK()</b> for consecutive ranking.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">11. When would you use ROW_NUMBER(), RANK(), or DENSE_RANK() in a query? Give a use case.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use these window functions for ranking, pagination, or deduplication.
</p>

<ul>
    <li><b>ROW_NUMBER():</b> Assigns a unique sequential number to each row (e.g., for pagination).</li>
    <li><b>RANK():</b> Ranks rows with possible gaps after ties (e.g., competition ranking).</li>
    <li><b>DENSE_RANK():</b> Ranks rows without gaps after ties (e.g., leaderboard with shared positions).</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Window Function Use Cases
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Function</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Typical Use Case</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">ROW_NUMBER()</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Pagination, deduplication</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">RANK()</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Competition ranking with gaps</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">DENSE_RANK()</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Leaderboard without gaps</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Choose the function based on how you want to handle ties and numbering.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">12. Write a SQL query to compute the median number of searches made by users, given a summary table of search counts.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use window functions to rank and find the median value.
</p>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT AVG(search_count) AS median_searches
FROM (
    SELECT search_count,
           ROW_NUMBER() OVER (ORDER BY search_count) AS rn,
           COUNT(*) OVER () AS total
    FROM user_search_summary
) t
WHERE rn IN (FLOOR((total + 1) / 2), CEIL((total + 1) / 2));
```
<p><i>This works for both even and odd row counts.</i></p>

<p>
    <b>Summary:</b> Median is the middle value (or average of two middle values) in ordered data.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">13. Write a SQL query to calculate the sum of odd-numbered and even-numbered measurements separately for each day.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use <code>CASE</code> expressions to separate odd and even measurement numbers.
</p>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT
    day,
    SUM(CASE WHEN MOD(measurement_number, 2) = 1 THEN value ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN MOD(measurement_number, 2) = 0 THEN value ELSE 0 END) AS even_sum
FROM measurements
GROUP BY day;
```

<p>
    <b>Summary:</b> Use <code>MOD</code> or <code>%</code> operator to distinguish odd/even numbers.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<b style="color:#1C4980;font-weight:bold;">14. Write a SQL query to get the average review rating for each product for each month.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Use <code>GROUP BY</code> with date truncation to aggregate by month.
</p>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
SELECT
    product_id,
    DATE_TRUNC('month', review_date) AS review_month,
    AVG(rating) AS avg_rating
FROM reviews
GROUP BY product_id, DATE_TRUNC('month', review_date);
```
<p><i>Replace <code>DATE_TRUNC</code> with the appropriate function for your SQL dialect.</i></p>

<p>
    <b>Summary:</b> Aggregating by truncated date groups results by month.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
