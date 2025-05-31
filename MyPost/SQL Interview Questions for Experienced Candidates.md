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
<b style="color:#1C4980;font-weight:bold;">1. What is a SQL index and what are different types of indexes (clustered, non-clustered, unique, etc.)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    An <b>index</b> in SQL is a database object that enhances the speed of data retrieval operations on a table by providing a fast lookup mechanism, similar to an index in a book. While indexes improve SELECT query performance, they require additional storage and can add overhead to data modification operations (INSERT, UPDATE, DELETE) because the index must be maintained as data changes.
</p>

<ul>
    <li><b>Clustered Index:</b> Determines the physical order of data rows in the table. Each table can have only one clustered index because the data rows themselves can be sorted in only one order. The clustered index is typically created on the primary key by default.</li>
    <li><b>Non-Clustered Index:</b> A separate structure from the table data that contains a sorted list of key values and pointers (row locators) to the actual data rows. A table can have multiple non-clustered indexes. Non-clustered indexes are useful for speeding up queries that filter or sort by columns other than the clustered index key.</li>
    <li><b>Unique Index:</b> Ensures that all values in the indexed column(s) are unique across the table. Unique indexes are often used to enforce business rules, such as unique email addresses or usernames.</li>
    <li><b>Composite Index:</b> An index that covers two or more columns. Composite indexes are useful for queries that filter or sort by multiple columns together.</li>
    <li><b>Full-Text Index:</b> Specialized index for efficient searching of large text-based columns, supporting advanced search features like stemming and proximity.</li>
    <li><b>Spatial Index:</b> Used for indexing spatial data types (such as geometry or geography), enabling efficient spatial queries (e.g., finding points within a region).</li>
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

<ul>
    <li><b>Full-Text Index (SQL Server Example):</b></li>
</ul>

```sql
CREATE FULLTEXT INDEX ON Employees(Resume);
```
<p><i>This enables advanced text search capabilities on the <code>Resume</code> column.</i></p>

<ul>
    <li><b>Spatial Index (SQL Server Example):</b></li>
</ul>

```sql
CREATE SPATIAL INDEX idx_location ON Locations(GeoPoint);
```
<p><i>This allows efficient spatial queries on the <code>GeoPoint</code> column.</i></p>

<p>
    <b>Summary:</b> Indexes are essential for optimizing query performance. Choose the appropriate index type based on your query patterns and data structure. While indexes speed up data retrieval, they can slow down data modifications and require additional storage, so use them judiciously.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">2. What is the difference between a heap (no clustered index) and a table with a clustered index, and how can you identify a heap table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>heap</b> is a table that does <b>not</b> have a clustered index. In a heap, data rows are stored in no particular order, and their physical location is identified by a Row Identifier (RID). In contrast, a table with a <b>clustered index</b> stores its data rows in the order of the clustered index key, which means the physical order of the rows matches the logical order of the index.
</p>

<ul>
    <li><b>Heap Table:</b> 
        <ul>
            <li>No clustered index exists on the table.</li>
            <li>Data is unordered; new rows are placed wherever space is available.</li>
            <li>Row locations are tracked by RIDs (Row Identifiers).</li>
            <li>Heaps are typically faster for bulk inserts and minimal indexing, but slower for searches and lookups.</li>
        </ul>
    </li>
    <li><b>Clustered Index Table:</b>
        <ul>
            <li>Has a clustered index, which determines the physical order of the data rows.</li>
            <li>Data is stored and retrieved in the order of the clustered index key.</li>
            <li>Only one clustered index is allowed per table, as data can be physically sorted in only one way.</li>
            <li>Clustered indexes improve search, range queries, and ordered retrieval performance.</li>
        </ul>
    </li>
</ul>

<p><b style="color:#B9770E;">How to Identify a Heap Table:</b></p>
<ul>
    <li>In SQL Server, you can query the <code>sys.indexes</code> system catalog view. If a table has an entry with <code>index_id = 0</code>, it is a heap. If it has <code>index_id = 1</code>, it has a clustered index.</li>
    <li>Other databases have similar metadata tables or commands to check for clustered indexes.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Examples:</b></p>

<ul>
    <li><b>Create a heap (no clustered index):</b></li>
</ul>

```sql
CREATE TABLE HeapTable (
    ID INT,
    Name VARCHAR(50)
);
-- No clustered index is created, so this table is a heap.
```
<p><i>This table is a heap because it does not have a clustered index.</i></p>

<ul>
    <li><b>Add a clustered index to convert the heap:</b></li>
</ul>

```sql
CREATE CLUSTERED INDEX idx_id ON HeapTable(ID);
```
<p><i>After this, <code>HeapTable</code> is no longer a heap; it is now ordered by <code>ID</code>.</i></p>

<ul>
    <li><b>Identify a heap in SQL Server:</b></li>
</ul>

```sql
SELECT name, index_id
FROM sys.indexes
WHERE object_id = OBJECT_ID('HeapTable');
```
<p><i>If you see a row with <code>index_id = 0</code>, the table is a heap. If <code>index_id = 1</code> exists, it has a clustered index.</i></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Heap vs Clustered Index Table Comparison
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Aspect</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Heap Table</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Clustered Index Table</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Physical Order</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Unordered</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ordered by index key</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Index ID (SQL Server)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">0</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Performance</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Faster for bulk inserts, slower for searches</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Faster for searches, range queries, and ordered retrieval</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Use Case</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Staging tables, ETL, minimal indexing</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Transactional tables, reporting, frequent lookups</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> A heap is a table without a clustered index, storing data in no defined order and identified by <code>index_id = 0</code>. A clustered index table stores data in the order of the index key (<code>index_id = 1</code>), improving search and range query performance. Choose based on your workload and query patterns.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">3. What is the difference between a PRIMARY KEY and a UNIQUE KEY (or unique index) in SQL?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Both <b>PRIMARY KEY</b> and <b>UNIQUE KEY</b> (or unique index) are used to enforce uniqueness of values in one or more columns, but they have important differences in behavior, usage, and constraints.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        PRIMARY KEY vs UNIQUE KEY
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Aspect</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">PRIMARY KEY</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">UNIQUE KEY</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Purpose</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Uniquely identifies each row in a table</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ensures all values in the column(s) are unique</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Number per Table</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Only one PRIMARY KEY allowed</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Multiple UNIQUE KEYs allowed</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">NULL Values</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Cannot contain NULLs (all columns must be NOT NULL)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Can contain a single NULL (in most databases); some allow multiple NULLs</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Index Type</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Creates a unique clustered index by default (if none exists)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Creates a unique non-clustered index by default</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Usage</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Main identifier for table rows; used for relationships (foreign keys)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Enforces alternate unique constraints (e.g., email, username)</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

<ul>
    <li><b>Defining PRIMARY KEY and UNIQUE KEY in CREATE TABLE:</b></li>
</ul>

```sql
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,         -- PRIMARY KEY: unique, not null, only one per table
    Email VARCHAR(100) UNIQUE,          -- UNIQUE KEY: alternate unique constraint, can be null
    PhoneNumber VARCHAR(20)
);
```
<p><i>Here, <code>EmployeeID</code> is the primary key (unique, not null). <code>Email</code> is a unique key (can be null in some databases).</i></p>

<ul>
    <li><b>Adding a UNIQUE KEY after table creation:</b></li>
</ul>

```sql
ALTER TABLE Employees ADD CONSTRAINT uq_emp_phone UNIQUE (PhoneNumber);
```
<p><i>This adds a unique constraint to <code>PhoneNumber</code>, ensuring all phone numbers are unique (but can be null).</i></p>

<ul>
    <li><b>Composite Keys:</b> Both PRIMARY KEY and UNIQUE KEY can be defined on multiple columns (composite keys).</li>
</ul>

```sql
-- Composite PRIMARY KEY
CREATE TABLE ProjectAssignments (
    EmployeeID INT,
    ProjectID INT,
    AssignmentDate DATE,
    PRIMARY KEY (EmployeeID, ProjectID)
);

-- Composite UNIQUE KEY
ALTER TABLE Employees ADD CONSTRAINT uq_emp_email_phone UNIQUE (Email, PhoneNumber);
```

<p>
    <b>Summary:</b> Use <b>PRIMARY KEY</b> for the main unique identifier of a table (no NULLs, only one per table). Use <b>UNIQUE KEY</b> for enforcing alternate unique constraints (can be multiple per table, allows NULLs). Both help maintain data integrity, but PRIMARY KEY is essential for relational design and foreign key references.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">4. What are index “forwarding pointers” in a heap table, and how do they affect query performance?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    In SQL Server, a <b>heap table</b> is a table without a clustered index. When a row in a heap table is updated and the new data no longer fits in its original location (data page), SQL Server may move the row to a new page with enough space. To maintain references from non-clustered indexes or other pointers, SQL Server leaves a <b>forwarding pointer</b> at the original location. This pointer directs any access to the old location to the new location of the row.
</p>

<ul>
    <li><b>How Forwarding Pointers Are Created:</b> 
        <ul>
            <li>Occurs when an <code>UPDATE</code> operation increases the row size and there is not enough space on the original data page.</li>
            <li>The original row is replaced with a small stub (the forwarding pointer), and the full row is moved to a new page.</li>
        </ul>
    </li>
    <li><b>Impact on Query Performance:</b>
        <ul>
            <li>When a query or non-clustered index seeks the row, SQL Server first reads the original page, finds the forwarding pointer, and then reads the new page to retrieve the actual row data.</li>
            <li>This results in <b>additional I/O operations</b> (extra page reads), increasing latency and reducing query performance, especially if many forwarding pointers exist.</li>
            <li>Forwarding pointers can accumulate over time in heavily updated heap tables, leading to significant performance degradation.</li>
        </ul>
    </li>
    <li><b>Resolution and Maintenance:</b>
        <ul>
            <li>Forwarding pointers are removed by rebuilding the heap (using <code>ALTER TABLE ... REBUILD</code>) or by creating a clustered index on the table (which reorganizes the data and eliminates forwarding pointers).</li>
            <li>Regular maintenance is recommended for heaps with frequent updates to avoid performance issues.</li>
        </ul>
    </li>
</ul>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Update a row in a heap table that causes it to move
UPDATE HeapTable SET Name = REPLICATE('A', 1000) WHERE ID = 1;
-- If the new value doesn't fit on the original page, a forwarding pointer is created.
```
<p><i>Subsequent queries accessing this row will first read the original page, follow the forwarding pointer, and then read the new page, resulting in extra I/O.</i></p>

<p><b style="color:#B9770E;">How to Remove Forwarding Pointers:</b></p>

```sql
-- Rebuild the heap to remove forwarding pointers
ALTER TABLE HeapTable REBUILD;

-- Or create a clustered index (which also removes forwarding pointers)
CREATE CLUSTERED INDEX idx_id ON HeapTable(ID);
```

<p>
    <b>Summary:</b> Forwarding pointers in heap tables are created when updated rows are moved to new pages, leaving a pointer behind. They cause extra I/O and degrade query performance, especially with frequent updates. Regularly rebuilding the heap or adding a clustered index can eliminate forwarding pointers and restore optimal performance.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">5. What is a composite index, and how do you choose the order of columns in it for optimal performance?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>composite index</b> (also called a <b>multi-column index</b>) is an index that includes two or more columns from the same table. Composite indexes are useful for optimizing queries that filter or sort on multiple columns together. The <b>order of columns</b> in a composite index is critical for its effectiveness and determines which queries can benefit from the index.
</p>

<ul>
    <li><b>How Composite Indexes Work:</b>
        <ul>
            <li>The index is built in the order of the specified columns (e.g., <code>(A, B, C)</code>).</li>
            <li>Queries that filter on the <b>leading column(s)</b> (e.g., <code>A</code> or <code>A, B</code>) can use the index efficiently.</li>
            <li>If a query filters only on a non-leading column (e.g., <code>B</code> or <code>C</code> without <code>A</code>), the index may not be used or may be less efficient.</li>
        </ul>
    </li>
    <li><b>Choosing Column Order:</b>
        <ul>
            <li>Place the <b>most selective</b> (most unique) column first, especially if it is commonly used in <code>WHERE</code> or <code>JOIN</code> conditions.</li>
            <li>Consider the most common query patterns: columns used together in filters or sorts should appear in the same order as in the queries.</li>
            <li>If sorting is important (e.g., <code>ORDER BY</code>), include those columns in the index in the same order.</li>
        </ul>
    </li>
    <li><b>Index Coverage:</b>
        <ul>
            <li>A composite index on <code>(A, B, C)</code> can be used for queries filtering on <code>A</code>, <code>A, B</code>, or <code>A, B, C</code>, but not efficiently for <code>B</code> or <code>C</code> alone.</li>
        </ul>
    </li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Composite Index Usage Examples
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Index Definition</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Query Example</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Index Used?</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>(DepartmentID, Salary)</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>WHERE DepartmentID = 10</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>(DepartmentID, Salary)</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>WHERE DepartmentID = 10 AND Salary &gt; 50000</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>(DepartmentID, Salary)</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>WHERE Salary &gt; 50000</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No (or less efficient)</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
-- Composite index on DepartmentID and Salary
CREATE INDEX idx_dept_salary ON Employees(DepartmentID, Salary);
```
<p><i>This index is optimal for queries like <code>WHERE DepartmentID = ? AND Salary &gt; ?</code> or <code>WHERE DepartmentID = ?</code>. It is not efficient for queries filtering only on <code>Salary</code>.</i></p>

<ul>
    <li><b>Tip:</b> Analyze your most frequent queries and their filter conditions to determine the best column order for composite indexes.</li>
    <li><b>Best Practice:</b> Avoid creating overly wide composite indexes (many columns), as they increase storage and maintenance overhead.</li>
</ul>

<p>
    <b>Summary:</b> A composite index covers multiple columns and is most effective when queries filter on the leading column(s). Choose the column order based on selectivity and common query patterns to maximize performance.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">6. When should you use a covering index, and how does it improve the performance of a query?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>covering index</b> is an index that contains all the columns required to satisfy a query—either as part of the index key or as included (non-key) columns. When a query can be answered entirely from the index, the database engine does not need to access the underlying table (heap or clustered index), resulting in significant performance improvements.
</p>

<ul>
    <li><b>When to Use:</b>
        <ul>
            <li>For queries that are run frequently and always retrieve the same set of columns.</li>
            <li>When you want to minimize I/O and speed up SELECT operations, especially in read-heavy workloads.</li>
            <li>For queries that filter on one or more columns and return additional columns (e.g., reporting, dashboards).</li>
        </ul>
    </li>
    <li><b>How It Improves Performance:</b>
        <ul>
            <li>Eliminates the need for "bookmark lookups" or "key lookups"—the extra step of fetching data from the base table after finding matching rows in the index.</li>
            <li>Reduces disk I/O and CPU usage, as all required data is available in the index structure itself.</li>
            <li>Improves query response time, especially for large tables or high-concurrency environments.</li>
        </ul>
    </li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Covering Index Example and Benefits
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Query</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Covering Index</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Benefit</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SELECT Salary, FirstName FROM Employees WHERE DepartmentID = ?</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>CREATE INDEX idx_covering ON Employees(DepartmentID) INCLUDE (Salary, FirstName);</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Query is satisfied entirely from the index—no table lookup needed.</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
-- Create a covering index for a query filtering by DepartmentID and returning Salary and FirstName
CREATE INDEX idx_covering ON Employees(DepartmentID) INCLUDE (Salary, FirstName);
```
<p><i>This index allows the database to answer <code>SELECT Salary, FirstName FROM Employees WHERE DepartmentID = ?</code> using only the index, with no need to access the base table.</i></p>

<ul>
    <li><b>Tip:</b> Use covering indexes for high-traffic queries that always access the same columns. Avoid including too many columns, as this increases index size and maintenance overhead.</li>
    <li><b>Best Practice:</b> Analyze your workload and use query execution plans to identify queries that would benefit most from covering indexes.</li>
</ul>

<p>
    <b>Summary:</b> Covering indexes are highly effective for optimizing read-heavy workloads with predictable query patterns. They reduce I/O by allowing the database to serve queries directly from the index, improving speed and scalability.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">7. How does the existence of an index on a column affect INSERT, UPDATE, and DELETE performance on a table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    While indexes are essential for improving the speed of <b>SELECT</b> queries, they introduce additional overhead for data modification operations such as <b>INSERT</b>, <b>UPDATE</b>, and <b>DELETE</b>. This is because the database must maintain the index structures in sync with the underlying table data.
</p>

<ul>
    <li><b>INSERT:</b>
        <ul>
            <li>When a new row is inserted, the database must add corresponding entries to all relevant indexes.</li>
            <li>If there are multiple indexes, each one must be updated, which increases the time required for the insert operation.</li>
            <li>Bulk inserts can be significantly slower if many indexes exist.</li>
        </ul>
    </li>
    <li><b>UPDATE:</b>
        <ul>
            <li>If an <b>indexed column</b> is updated, the database must remove the old index entry and add a new one reflecting the updated value.</li>
            <li>Updates to non-indexed columns have minimal impact on indexes, but updates to indexed columns can be costly, especially if the index is large or complex (e.g., composite or unique indexes).</li>
            <li>Frequent updates to indexed columns can lead to index fragmentation, further degrading performance over time.</li>
        </ul>
    </li>
    <li><b>DELETE:</b>
        <ul>
            <li>When a row is deleted, all associated index entries must also be removed.</li>
            <li>Deleting rows from a table with many indexes takes longer than from a table with few or no indexes.</li>
            <li>Large-scale deletes can cause index fragmentation, requiring periodic maintenance (e.g., index rebuilds).</li>
        </ul>
    </li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Impact of Indexes on Data Modification Operations
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Operation</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Effect of Indexes</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Best Practice</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">INSERT</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Each index must be updated with new row data, increasing insert time.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Minimize indexes on tables with heavy insert workloads.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">UPDATE</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Updates to indexed columns require index maintenance (remove old, add new entry).</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Avoid frequent updates to indexed columns; monitor fragmentation.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">DELETE</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Index entries must be removed for each deleted row, slowing down deletes.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Batch deletes and rebuild indexes periodically.</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Insert into a table with indexes
INSERT INTO Employees (EmployeeID, FirstName, LastName) VALUES (1, 'Ashish', 'Zope');
-- The database updates all relevant indexes after the insert.

-- Update an indexed column
UPDATE Employees SET LastName = 'Patil' WHERE EmployeeID = 1;
-- The index on LastName (if exists) must be updated.

-- Delete a row
DELETE FROM Employees WHERE EmployeeID = 1;
-- All index entries for EmployeeID = 1 are removed.
```
<p><i>The more indexes a table has, the more work the database must do for each insert, update, or delete operation.</i></p>

<ul>
    <li><b>Tip:</b> Only create indexes that are necessary for your most important queries. Excessive indexing can degrade write performance and increase storage requirements.</li>
    <li><b>Best Practice:</b> Regularly review and optimize indexes, especially on tables with heavy write activity. Consider dropping unused indexes and scheduling index maintenance (rebuild/reorganize) as needed.</li>
</ul>

<p>
    <b>Summary:</b> Indexes improve read (SELECT) performance but slow down write operations (INSERT, UPDATE, DELETE) due to the need to maintain index structures. Always balance the number and type of indexes based on your application's read/write workload.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">8. What is index selectivity, and why is it important for query optimization?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>Index selectivity</b> measures how well an index distinguishes between rows in a table. It is defined as the ratio of the number of distinct values in an indexed column (or set of columns) to the total number of rows in the table. High selectivity means the column has many unique values (e.g., a primary key), while low selectivity means the column has many repeated values (e.g., a boolean or gender column).
</p>

<ul>
    <li><b>High Selectivity:</b> An index is highly selective if most values are unique or nearly unique. Such indexes are very effective for filtering queries, as they quickly narrow down the result set to a small number of rows.</li>
    <li><b>Low Selectivity:</b> An index is poorly selective if most values are repeated (few unique values). These indexes are less useful for filtering, as they do not significantly reduce the number of rows scanned.</li>
    <li><b>Formula:</b> <code>Selectivity = (Number of Distinct Values) / (Total Number of Rows)</code></li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Index Selectivity Examples
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Column</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Distinct Values</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Total Rows</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Selectivity</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Index Usefulness</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">EmployeeID</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">10,000</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">10,000</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1.0 (high)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Very effective</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Gender</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">10,000</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">0.0002 (low)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Not effective</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">DepartmentID</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">20</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">10,000</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">0.002 (low)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Limited usefulness</td>
        </tr>
    </tbody>
</table>

<ul>
    <li><b>Why It Matters:</b> The database query optimizer uses selectivity to decide whether to use an index for a query. High-selectivity indexes allow the optimizer to quickly locate a small subset of rows, making queries much faster. Low-selectivity indexes may be ignored, as scanning the index provides little benefit over scanning the entire table.</li>
    <li><b>Composite Indexes:</b> Selectivity can be improved by creating composite indexes on multiple columns, especially if the combination of columns is highly unique.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
-- High selectivity: EmployeeID (unique for each row)
CREATE INDEX idx_employee_id ON Employees(EmployeeID);

-- Low selectivity: Gender (few unique values)
CREATE INDEX idx_gender ON Employees(Gender);
```
<p><i>The <code>idx_employee_id</code> index is highly selective and efficient for lookups. The <code>idx_gender</code> index is less useful because many rows share the same value.</i></p>

<ul>
    <li><b>Tip:</b> Use indexes on columns with high selectivity (e.g., primary keys, unique identifiers) for best query performance.</li>
    <li><b>Best Practice:</b> Avoid indexing columns with very low selectivity unless they are frequently used in combination with other columns in composite indexes.</li>
</ul>

<p>
    <b>Summary:</b> Index selectivity is a key factor in query optimization. High-selectivity indexes enable efficient data retrieval and are preferred by the query optimizer. Always consider selectivity when designing indexes for your tables.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">9. How many clustered indexes can a table have, and why?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A table can have <b>only one clustered index</b>. This is because a clustered index determines the <b>physical order</b> of the data rows in the table, and the data can be physically sorted in only one way at a time.
</p>

<ul>
    <li><b>Reason:</b> The clustered index sorts and stores the data rows of the table based on the index key. Since the actual data rows are organized on disk according to this key, only one such ordering is possible.</li>
    <li><b>Non-Clustered Indexes:</b> In contrast, a table can have multiple non-clustered indexes. These are separate structures that reference the data rows without affecting their physical order.</li>
    <li><b>Primary Key and Clustered Index:</b> By default, when you define a primary key on a table (and no clustered index exists), most databases automatically create a clustered index on the primary key column(s). However, you can explicitly specify a different column for the clustered index if needed.</li>
    <li><b>Attempting Multiple Clustered Indexes:</b> If you try to create a second clustered index on a table, the database will return an error, as only one is allowed.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Clustered vs Non-Clustered Indexes
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Index Type</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Physical Data Order</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Number Allowed per Table</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Typical Use</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Clustered Index</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes (orders data rows)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Primary key, main lookup column</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Non-Clustered Index</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No (separate structure)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Many (subject to DB limits)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Alternate queries, searches, sorts</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
-- Create a clustered index (only one allowed per table)
CREATE CLUSTERED INDEX idx_emp_id ON Employees(EmployeeID);

-- Create multiple non-clustered indexes (allowed)
CREATE NONCLUSTERED INDEX idx_emp_email ON Employees(Email);
CREATE NONCLUSTERED INDEX idx_emp_phone ON Employees(PhoneNumber);

-- Attempting to create a second clustered index will fail
CREATE CLUSTERED INDEX idx_emp_name ON Employees(LastName); -- Error!
```
<p><i>Only one clustered index can exist per table. Non-clustered indexes can be created on other columns as needed.</i></p>

<ul>
    <li><b>Tip:</b> Choose the clustered index carefully, as it affects the physical storage and performance of range queries and lookups.</li>
    <li><b>Best Practice:</b> Use the clustered index for columns that are frequently searched for ranges or used in sorting, such as primary keys or date columns.</li>
</ul>

<p>
    <b>Summary:</b> Each table can have only <b>one clustered index</b> because it defines the physical order of the data rows. You can create multiple non-clustered indexes to support additional query patterns.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">10. What is index fragmentation, and how can it be resolved or mitigated in a large database?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>Index fragmentation</b> refers to the condition where the physical order of pages in an index becomes misaligned with the logical order of the index keys. This misalignment leads to inefficient disk I/O, increased page reads, and slower query performance, especially for range scans and large data sets.
</p>

<ul>
    <li><b>Types of Fragmentation:</b>
        <ul>
            <li><b>Internal Fragmentation:</b> Occurs when index pages have excessive free space (low page density), often due to frequent row deletions or updates that reduce row size.</li>
            <li><b>External Fragmentation:</b> Happens when the logical order of index pages does not match their physical order on disk, causing additional I/O as the database engine jumps between non-contiguous pages.</li>
        </ul>
    </li>
    <li><b>Causes:</b>
        <ul>
            <li>Frequent <code>INSERT</code>, <code>UPDATE</code>, and <code>DELETE</code> operations, especially on tables with random key values (e.g., GUIDs).</li>
            <li>Page splits, where new rows are inserted into full pages, causing the page to split and data to be moved to a new page.</li>
            <li>Bulk data modifications or large-scale deletes.</li>
        </ul>
    </li>
    <li><b>Impact:</b>
        <ul>
            <li>Slower query performance due to increased logical and physical reads.</li>
            <li>Higher I/O and CPU usage, especially for range queries and index scans.</li>
            <li>Reduced cache efficiency, as more pages are needed to store the same amount of data.</li>
        </ul>
    </li>
    <li><b>Detection:</b>
        <ul>
            <li>Use database-specific tools or system views to monitor fragmentation levels (e.g., <code>sys.dm_db_index_physical_stats</code> in SQL Server).</li>
        </ul>
    </li>
    <li><b>Resolution:</b>
        <ul>
            <li><b>Rebuild Index:</b> Physically drops and recreates the index, removing all fragmentation and compacting pages. This is more resource-intensive but fully defragments the index.</li>
            <li><b>Reorganize Index:</b> Defragments the leaf level of the index by reordering pages and compacting rows. Less intensive than rebuild, suitable for moderate fragmentation.</li>
        </ul>
    </li>
    <li><b>Mitigation & Best Practices:</b>
        <ul>
            <li>Schedule regular index maintenance (rebuild or reorganize) based on fragmentation thresholds (e.g., rebuild if fragmentation &gt; 30%, reorganize if 5–30%).</li>
            <li>Monitor fragmentation using system views or maintenance plans.</li>
            <li>Choose appropriate fill factors when creating indexes to reduce page splits.</li>
            <li>Consider partitioning large tables to localize fragmentation and maintenance.</li>
        </ul>
    </li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Index Fragmentation: Detection and Resolution
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Action</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">SQL Server Example</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Detect Fragmentation</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                <code>
                SELECT index_id, avg_fragmentation_in_percent
                FROM sys.dm_db_index_physical_stats(DB_ID(), OBJECT_ID('Employees'), NULL, NULL, 'LIMITED');
                </code>
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Check current fragmentation levels</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Rebuild Index</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                <code>ALTER INDEX idx_emp_id ON Employees REBUILD;</code>
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Removes all fragmentation, recreates index</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Reorganize Index</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                <code>ALTER INDEX idx_emp_id ON Employees REORGANIZE;</code>
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Defragments leaf level, less intensive</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
-- Detect fragmentation (SQL Server)
SELECT index_id, avg_fragmentation_in_percent
FROM sys.dm_db_index_physical_stats(DB_ID(), OBJECT_ID('Employees'), NULL, NULL, 'LIMITED');

-- Rebuild an index (removes all fragmentation)
ALTER INDEX idx_emp_id ON Employees REBUILD;

-- Reorganize an index (less intensive, for moderate fragmentation)
ALTER INDEX idx_emp_id ON Employees REORGANIZE;
```
<p><i>Schedule these commands as part of regular maintenance, especially for large or frequently updated tables.</i></p>

<ul>
    <li><b>Tip:</b> Automate index maintenance using database jobs or maintenance plans.</li>
    <li><b>Best Practice:</b> Monitor fragmentation regularly and adjust maintenance frequency based on workload and performance needs.</li>
</ul>

<p>
    <b>Summary:</b> Index fragmentation degrades query performance by causing inefficient I/O. Regularly detect, rebuild, or reorganize indexes to maintain optimal performance, especially in large, high-transaction databases.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Mastering SQL Joins</b>
</blockquote>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">1. What are the different types of SQL joins (<code>INNER JOIN</code>, <code>LEFT JOIN</code>, <code>RIGHT JOIN</code>, <code>FULL JOIN</code>, <code>CROSS JOIN</code>, etc.) and when would you use each?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    SQL joins are used to combine rows from two or more tables based on related columns. The main types of joins are:
</p>

<ul>
    <li><b>INNER JOIN:</b> Returns only rows where there is a match in both tables. Use when you want records that exist in both tables.</li>
    <li><b>LEFT JOIN (LEFT OUTER JOIN):</b> Returns all rows from the left table and matched rows from the right table. If there is no match, columns from the right table are NULL. Use when you want all records from the left table, regardless of matches in the right.</li>
    <li><b>RIGHT JOIN (RIGHT OUTER JOIN):</b> Returns all rows from the right table and matched rows from the left table. If there is no match, columns from the left table are NULL. Use when you want all records from the right table, regardless of matches in the left.</li>
    <li><b>FULL JOIN (FULL OUTER JOIN):</b> Returns all rows from both tables. Where there is a match, rows are combined; where there is no match, columns from the missing side are NULL. Use when you want all records from both tables, matched or unmatched.</li>
    <li><b>CROSS JOIN:</b> Returns the Cartesian product of both tables (every row of the first table joined with every row of the second). Use rarely, typically for generating all possible combinations.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        SQL Join Types Overview
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Join Type</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Description</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">When to Use</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">INNER JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Rows with matching values in both tables</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">When you need only records present in both tables</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">LEFT JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All rows from left table, matched rows from right; unmatched right rows are NULL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">When you want all records from the left table</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">RIGHT JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All rows from right table, matched rows from left; unmatched left rows are NULL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">When you want all records from the right table</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">FULL OUTER JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All rows from both tables; unmatched columns are NULL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">When you want all records from both tables</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">CROSS JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Cartesian product (all possible combinations)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Rarely used; for generating combinations</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Examples:</b></p>

<ul>
    <li><b>INNER JOIN:</b></li>
</ul>

```sql
SELECT a.*, b.*
FROM TableA a
INNER JOIN TableB b ON a.id = b.a_id;
```
<p><i>Returns only rows where <code>a.id = b.a_id</code>.</i></p>

<ul>
    <li><b>LEFT JOIN:</b></li>
</ul>

```sql
SELECT a.*, b.*
FROM TableA a
LEFT JOIN TableB b ON a.id = b.a_id;
```
<p><i>Returns all rows from <code>TableA</code>; <code>TableB</code> columns are NULL where no match exists.</i></p>

<ul>
    <li><b>RIGHT JOIN:</b></li>
</ul>

```sql
SELECT a.*, b.*
FROM TableA a
RIGHT JOIN TableB b ON a.id = b.a_id;
```
<p><i>Returns all rows from <code>TableB</code>; <code>TableA</code> columns are NULL where no match exists.</i></p>

<ul>
    <li><b>FULL OUTER JOIN:</b></li>
</ul>

```sql
SELECT a.*, b.*
FROM TableA a
FULL OUTER JOIN TableB b ON a.id = b.a_id;
```
<p><i>Returns all rows from both tables; unmatched columns are NULL.</i></p>

<ul>
    <li><b>CROSS JOIN:</b></li>
</ul>

```sql
SELECT a.*, b.*
FROM TableA a
CROSS JOIN TableB b;
```
<p><i>Returns every possible combination of rows from <code>TableA</code> and <code>TableB</code>.</i></p>

<p>
    <b>Summary:</b><br>
    - Use <b>INNER JOIN</b> for matching rows only.<br>
    - Use <b>LEFT JOIN</b> to include all left table rows.<br>
    - Use <b>RIGHT JOIN</b> to include all right table rows.<br>
    - Use <b>FULL OUTER JOIN</b> to include all rows from both tables.<br>
    - Use <b>CROSS JOIN</b> for all combinations (rarely needed in practice).
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">2. What is the difference between a <code>CROSS JOIN</code> and a <code>FULL OUTER JOIN</code>?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <code>CROSS JOIN</code> and <code>FULL OUTER JOIN</code> are both used to combine rows from two tables, but they serve very different purposes and produce fundamentally different results:
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

<p><b style="color:#B9770E;">Syntax & Examples:</b></p>

<ul>
    <li><b>CROSS JOIN:</b></li>
</ul>

```sql
SELECT a.*, b.*
FROM TableA a
CROSS JOIN TableB b;
```
<p><i>This returns every possible combination of rows from <code>TableA</code> and <code>TableB</code>. If TableA has 3 rows and TableB has 2 rows, the result will have 6 rows.</i></p>

<ul>
    <li><b>FULL OUTER JOIN:</b></li>
</ul>

```sql
SELECT a.*, b.*
FROM TableA a
FULL OUTER JOIN TableB b ON a.id = b.a_id;
```
<p><i>This returns all rows from both tables. Where there is a match on <code>a.id = b.a_id</code>, the rows are combined. Where there is no match, columns from the missing side are filled with <code>NULL</code>.</i></p>

<p>
    <b>Summary:</b><br>
    - <b>CROSS JOIN</b> produces the Cartesian product, combining every row from the first table with every row from the second table, regardless of any relationship.<br>
    - <b>FULL OUTER JOIN</b> returns all matched rows based on a join condition, plus all unmatched rows from both tables, using <code>NULL</code> for missing values.<br>
    - Use <b>CROSS JOIN</b> for generating all possible combinations; use <b>FULL OUTER JOIN</b> when you want to see all data from both tables, including non-matching rows.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">3. Write a SQL query to retrieve the first and last names of employees along with the names of their managers (given <code>Employees</code> and <code>Managers</code> tables).</b>

<p><b style="color:#B9770E;">Answer:</b><br>
To retrieve employee names along with their managers' names, you need to join the <code>Employees</code> table with the <code>Managers</code> table using a foreign key relationship (e.g., <code>ManagerID</code> in <code>Employees</code> referencing <code>Managers.ManagerID</code>).</p>

<ul>
    <li><b>INNER JOIN:</b> Returns only employees who have a matching manager.</li>
    <li><b>LEFT JOIN:</b> Returns all employees, including those without a manager (manager fields will be <code>NULL</code>).</li>
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
    - <b>LEFT JOIN</b> is used to include all employees, even those without a manager.<br>
    - <b>INNER JOIN</b> would exclude employees who do not have a manager.
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
            <td style="border:1px solid #D5D8DC; padding:8px;">Exclude employees without managers.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">LEFT JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">All employees are shown; manager fields are NULL if no manager.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Include all employees, even those without managers.</td>
        </tr>
    </tbody>
</table>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">4. Write a SQL query to find the average salary for each department, given tables <code>Employees</code> (with <code>DepartmentID</code>) and <code>Departments</code> (with <code>DepartmentName</code>).</b>

<p><b style="color:#B9770E;">Answer:</b><br>
To calculate the average salary for each department, join the <code>Employees</code> table with the <code>Departments</code> table on <code>DepartmentID</code>, then use <code>GROUP BY</code> to aggregate by department.</p>

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
To find products that have never been ordered, identify products in the <code>Product</code> table that do not have any corresponding entries in the <code>Orders</code> table. This can be done using a <b>LEFT JOIN</b> and checking for <code>NULL</code> in the joined table, or by using a <code>NOT EXISTS</code> or <code>NOT IN</code> subquery.
</p>

<ul>
    <li><b>LEFT JOIN:</b> Returns all products, and for those with no matching order, the order fields will be <code>NULL</code>. Filter these using <code>WHERE o.OrderID IS NULL</code>.</li>
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
To find employees who are also managers, use a <b>self-join</b> on the <code>Employees</code> table. This means joining the table to itself, matching employees whose <code>EmployeeID</code> appears as a <code>ManagerID</code> for other employees.
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

<p><b style="color:#B9770E;">Example Query:</b><br>
To list each employee along with their manager's name, you can use a self-join:</p>

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
    - <b>LEFT JOIN</b> ensures employees without a manager are included, with manager fields as NULL.
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
Suppose you have the following tables:</p>

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
    <li><b>LEFT OUTER JOIN (LEFT JOIN):</b> Returns all rows from the left table, and matched rows from the right table. If there is no match, right table columns are <code>NULL</code>.</li>
    <li><b>RIGHT OUTER JOIN (RIGHT JOIN):</b> Returns all rows from the right table, and matched rows from the left table. If there is no match, left table columns are <code>NULL</code>.</li>
    <li><b>FULL OUTER JOIN:</b> Returns all rows from both tables, with <code>NULL</code> in columns where there is no match.</li>
    <li><b>INNER JOIN:</b> Returns only rows where there is a match in both tables.</li>
</ul>

<p><b style="color:#B9770E;">Example Scenario:</b><br>
Suppose you have the following tables:</p>

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
    A <b>database view</b> is a virtual table defined by a SQL query. It does not store data itself, but presents data dynamically from one or more underlying tables. Views are used to simplify complex queries, provide abstraction, and restrict access to sensitive data.
</p>

<ul>
    <li><b>Updatable Views:</b> If a view is based on a single table and does not use aggregates, GROUP BY, DISTINCT, or joins, you can usually perform <code>INSERT</code>, <code>UPDATE</code>, and <code>DELETE</code> operations through the view. The changes affect the underlying base table.</li>
    <li><b>Read-Only Views:</b> Views that include joins, aggregate functions, GROUP BY, DISTINCT, or other complex logic are typically <b>read-only</b>. You cannot update data through these views.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Updatable vs Read-Only Views
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">View Type</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Can Update Base Table?</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Simple (single table, no aggregates)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SELECT EmployeeID, FirstName FROM Employees</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Complex (joins, GROUP BY, aggregates)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SELECT DepartmentID, COUNT(*) FROM Employees GROUP BY DepartmentID</code></td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Simple updatable view
CREATE VIEW vw_EmployeeNames AS
SELECT EmployeeID, FirstName, LastName FROM Employees;

-- Update through the view (affects base table)
UPDATE vw_EmployeeNames SET FirstName = 'John' WHERE EmployeeID = 1;
```

<p>
    <b>Summary:</b> Views provide abstraction, security, and query simplification. You can update data through a view only if it is simple and directly maps to a single base table without complex logic.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">2. What is the difference between a standard view and a materialized (or indexed) view?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
A <b>standard view</b> is a virtual table that does not store any data itself; it simply runs the underlying query each time you access it, always reflecting the current state of the base tables. In contrast, a <b>materialized view</b> (or <b>indexed view</b> in SQL Server) physically stores the result set of its defining query, providing faster access at the cost of storage and refresh overhead.
</p>

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
            <td style="border:1px solid #D5D8DC; padding:8px;">No data stored; always queries base tables</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Physically stores query result set</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Performance</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Slower for complex or large queries</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Much faster for repeated, heavy queries</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data Freshness</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Always up-to-date with base tables</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">May be stale; requires manual or scheduled refresh</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Use Case</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Abstraction, security, simplified queries</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Performance optimization for reporting, analytics</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Maintenance</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No maintenance needed</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Requires refresh and storage management</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Standard view (always current)
CREATE VIEW vw_EmployeeSummary AS
SELECT DepartmentID, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY DepartmentID;

-- Materialized view (Oracle/PostgreSQL) or indexed view (SQL Server)
CREATE MATERIALIZED VIEW mv_EmployeeSummary AS
SELECT DepartmentID, COUNT(*) AS EmployeeCount
FROM Employees
GROUP BY DepartmentID;
-- In SQL Server, use indexed view syntax with SCHEMABINDING and a unique clustered index
```

<p>
    <b>Summary:</b> Use <b>standard views</b> for abstraction, security, and up-to-date data. Use <b>materialized views</b> or <b>indexed views</b> to boost performance for complex, resource-intensive queries where real-time data is not critical.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">3. What happens if a materialized view is being refreshed (complete refresh) and a user queries it at the same time?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    When a <b>materialized view</b> undergoes a <b>complete refresh</b>, the entire result set is rebuilt from scratch. If a user queries the view during this process, the behavior depends on the database system and refresh method:
</p>

<ul>
    <li><b>Most databases (e.g., Oracle):</b> The materialized view remains available during the refresh. Users querying the view will see the <b>previous (old) data</b> until the refresh completes, ensuring data consistency and uninterrupted access.</li>
    <li><b>Some systems or configurations:</b> If the refresh locks the view or replaces it atomically, queries may be <b>blocked</b> until the refresh finishes, or users may receive an error indicating the view is temporarily unavailable.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Materialized View Refresh Behavior
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Database</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">User Query During Refresh</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Oracle</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Serves old data until refresh completes</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SQL Server (Indexed View)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Always up-to-date; no explicit refresh needed</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">PostgreSQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">May block or error if <code>WITH NO DATA</code> is used</td>
        </tr>
    </tbody>
</table>

<ul>
    <li><b>Tip:</b> Use <code>FAST REFRESH</code> (if supported) to minimize downtime and keep the view more current with incremental changes.</li>
    <li><b>Best Practice:</b> Schedule complete refreshes during off-peak hours to reduce user impact.</li>
</ul>

<p>
    <b>Summary:</b> During a complete refresh, most databases serve the old data to users until the refresh is finished, ensuring uninterrupted access. Always check your database documentation for specific behavior and consider refresh strategies that balance performance and data freshness.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">4. When would you use a view in a database design? What benefits do views provide (e.g. security, abstraction)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>view</b> is a virtual table based on the result of a SQL query. Views are a powerful tool in database design, offering several key benefits:
</p>

<ul>
    <li><b>Security:</b> Limit user access to sensitive data by exposing only specific columns or rows. For example, you can create a view that omits salary information, allowing users to query employee names without seeing confidential details.</li>
    <li><b>Abstraction:</b> Hide complex joins, aggregations, or calculations behind a simple interface. This allows end users and applications to interact with straightforward queries, without needing to understand the underlying schema or logic.</li>
    <li><b>Simplification:</b> Provide a consistent and simplified way to access data for reporting, analytics, or application development. Views can encapsulate frequently used queries, reducing code duplication and errors.</li>
    <li><b>Consistency:</b> Centralize business logic, calculations, or filters in one place. This ensures that all users and applications apply the same rules and definitions, improving data integrity and maintainability.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Benefits of Using Views
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Benefit</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Description</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Security</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Restrict access to sensitive columns or rows</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>vw_PublicEmployees</code> hides salary data</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Abstraction</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Hide complex joins/calculations</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">View for sales summary with aggregations</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Simplification</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Provide a simple interface for users</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">View for reporting on active customers</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Consistency</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Standardize business logic in one place</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">View for tax calculations</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Hide salary details from most users
CREATE VIEW vw_PublicEmployees AS
SELECT EmployeeID, FirstName, LastName FROM Employees;
```

<p>
    <b>Summary:</b> Views are essential for enforcing security, simplifying data access, and centralizing business logic. They enable you to present a tailored, consistent, and secure interface to your data, improving both usability and maintainability.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">5. Can you create an index on a view? If so, what are the implications (e.g. indexed view in SQL Server)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Yes, in some databases—most notably <b>SQL Server</b>—you can create an <b>indexed view</b> (also known as a <b>materialized view</b>). An indexed view physically stores the result set of the view and allows you to create indexes on it, just like a regular table.
</p>

<ul>
    <li><b>Performance Benefits:</b> Indexed views can dramatically improve query performance for complex aggregations, joins, or calculations by persisting the computed results and allowing fast index-based lookups.</li>
    <li><b>Storage & Maintenance Overhead:</b> Since the data is physically stored, indexed views consume additional disk space. They also require maintenance—any changes to the underlying tables (INSERT, UPDATE, DELETE) will trigger updates to the indexed view, potentially impacting write performance.</li>
    <li><b>Restrictions:</b> Not all views are eligible for indexing. The view definition must be <b>deterministic</b> (no randomness or non-deterministic functions), use <code>WITH SCHEMABINDING</code>, and meet other database-specific requirements (e.g., no outer joins, no subqueries in SELECT list, etc.).</li>
    <li><b>Use Cases:</b> Indexed views are ideal for reporting, dashboards, or analytics scenarios where the same complex query is run frequently and up-to-date data is not required in real time.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Indexed View Example (SQL Server)
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Step</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">SQL Syntax</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Create a view with SCHEMABINDING</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
<pre style="margin:0;"><code>CREATE VIEW vw_SalesSummary WITH SCHEMABINDING AS
SELECT StoreID, SUM(SalesAmount) AS TotalSales
FROM dbo.Sales
GROUP BY StoreID;
</code></pre>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Create a unique clustered index on the view</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
<pre style="margin:0;"><code>CREATE UNIQUE CLUSTERED INDEX idx_SalesSummary_StoreID
ON vw_SalesSummary(StoreID);
</code></pre>
            </td>
        </tr>
    </tbody>
</table>

<ul>
    <li><b>Tip:</b> Indexed views are automatically maintained by SQL Server, so any changes to the base tables are reflected in the view. However, this can slow down data modifications.</li>
    <li><b>Best Practice:</b> Use indexed views for scenarios with heavy read and aggregation workloads, but evaluate the impact on write performance and storage.</li>
</ul>

<p>
    <b>Summary:</b> Indexed views (materialized views) can significantly speed up complex queries by storing precomputed results and allowing indexing, but they come with additional storage and maintenance costs. Use them judiciously for performance-critical reporting and analytics.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">6. How do you modify or drop a view if the underlying table schema changes?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    When the schema of a base table changes (such as adding, renaming, or dropping columns), any dependent views may become invalid or outdated. To keep your views in sync with the underlying tables, you need to <b>modify</b> or <b>drop</b> the affected views accordingly.
</p>

<ul>
    <li><b>Modify a View:</b> 
        <ul>
            <li>Use <code>CREATE OR REPLACE VIEW</code> (Oracle, PostgreSQL, MySQL 5.7+), or <code>ALTER VIEW</code> (SQL Server) to update the view definition to match the new table schema.</li>
            <li>Update the SELECT statement in the view to reflect any changes in column names, data types, or structure.</li>
        </ul>
    </li>
    <li><b>Drop a View:</b>
        <ul>
            <li>Use <code>DROP VIEW view_name;</code> to remove the view if it is no longer needed or cannot be updated to match the new schema.</li>
        </ul>
    </li>
    <li><b>Tip:</b> If a column referenced by a view is dropped or renamed in the base table, the view will become invalid and must be recreated or altered before it can be used again.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Modifying and Dropping Views
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Action</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">SQL Syntax</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Modify</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
<pre style="margin:0;"><code>-- Oracle/PostgreSQL/MySQL
CREATE OR REPLACE VIEW vw_EmployeeNames AS
SELECT EmployeeID, FirstName FROM Employees;

-- SQL Server
ALTER VIEW vw_EmployeeNames AS
SELECT EmployeeID, FirstName FROM Employees;
</code></pre>
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Update the view definition to match the new schema.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Drop</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
<pre style="margin:0;"><code>DROP VIEW vw_EmployeeNames;</code></pre>
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Removes the view from the database.</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Always review and update dependent views after making changes to base table schemas. Modify the view to match the new structure, or drop and recreate it as needed to avoid errors and maintain data integrity.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">7. What is the difference between a view and a temporary table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
A <b>view</b> and a <b>temporary table</b> are both used to simplify complex queries and manage data, but they serve different purposes and have distinct behaviors in SQL databases.
</p>

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
            <td style="border:1px solid #D5D8DC; padding:8px;">Definition persists in the database; always reflects current data in base tables</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Exists only for the duration of a session or transaction; dropped automatically</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Storage</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No data stored (unless materialized); acts as a saved query</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Physically stores data in tempdb or memory</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Usage</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Abstraction, security, reusable logic, simplified access</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Storing intermediate results, breaking down complex queries, batch processing</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Modification</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Cannot be directly modified (unless updatable view)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Can be modified (INSERT, UPDATE, DELETE)</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Scope</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Global (available to all users with permission)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Session or transaction-specific (not visible to others)</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Create a view (persists, always current)
CREATE VIEW vw_ActiveEmployees AS
SELECT EmployeeID, FirstName, LastName FROM Employees WHERE IsActive = 1;

-- Create a temporary table (session-specific, stores data)
CREATE TABLE #TempEmployees (
    EmployeeID INT,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50)
);

INSERT INTO #TempEmployees
SELECT EmployeeID, FirstName, LastName FROM Employees WHERE IsActive = 1;
```

<ul>
    <li><b>View:</b> Use when you need a reusable, secure, and always up-to-date abstraction over your data.</li>
    <li><b>Temporary Table:</b> Use when you need to store and manipulate intermediate results within a session or batch process.</li>
</ul>

<p>
    <b>Summary:</b> <b>Views</b> provide abstraction, security, and simplified access to live data, while <b>temporary tables</b> are ideal for storing and processing intermediate results during complex operations. Choose based on your need for persistence, scope, and data manipulation.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Stored Procedures & Functions</b>
</blockquote>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">1. What is the difference between a stored procedure and a user-defined function in SQL (aside from return value)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>stored procedure</b> and a <b>user-defined function (UDF)</b> are both programmable objects in SQL, but they serve different purposes and have distinct behaviors beyond just their return values.
</p>

<ul>
    <li><b>Stored Procedure:</b> A stored procedure is a precompiled set of SQL statements that can perform a wide range of operations, including modifying data (INSERT, UPDATE, DELETE), controlling transactions, and returning result sets or output parameters. Stored procedures are typically invoked using the <code>EXEC</code> or <code>CALL</code> statement and can contain complex logic, error handling, and flow control (IF, WHILE, etc.).</li>
    <li><b>User-Defined Function (UDF):</b> A UDF is a routine that returns a single value (scalar function) or a table (table-valued function). UDFs are designed to be used within SQL expressions, such as in <code>SELECT</code>, <code>WHERE</code>, or <code>JOIN</code> clauses. They are generally side-effect free and cannot modify database state (with rare exceptions in some databases).</li>
</ul>

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
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes (DML operations allowed)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No (read-only; cannot modify data)</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Can be used in SELECT/WHERE/JOIN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Transaction control</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Yes (can begin, commit, rollback)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Return type</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">None, scalar value, output parameters, or result set</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Scalar value or table</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Error handling</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Can use TRY...CATCH or equivalent</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Limited or not supported</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Usage context</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Called independently via EXEC/CALL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Used inline within SQL statements</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- Stored Procedure Example (SQL Server)
CREATE PROCEDURE UpdateEmployeeSalary
    @EmpID INT,
    @NewSalary DECIMAL(10,2)
AS
BEGIN
    UPDATE Employees SET Salary = @NewSalary WHERE EmployeeID = @EmpID;
END;

-- User-Defined Function Example (SQL Server)
CREATE FUNCTION dbo.GetEmployeeFullName(@EmpID INT)
RETURNS NVARCHAR(100)
AS
BEGIN
    DECLARE @FullName NVARCHAR(100);
    SELECT @FullName = FirstName + ' ' + LastName FROM Employees WHERE EmployeeID = @EmpID;
    RETURN @FullName;
END;
```

<p>
    <b>Summary:</b> Use stored procedures for complex operations, data modifications, and transaction control. Use user-defined functions for reusable computations or logic that can be embedded in queries. Functions are more restrictive but integrate seamlessly into SQL expressions, while procedures offer greater flexibility and control.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">2. What are the advantages and disadvantages of using stored procedures?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <b>Stored procedures</b> are precompiled collections of SQL statements and optional control-of-flow logic stored under a name and processed as a unit. They offer several benefits but also come with some trade-offs.
</p>

<ul>
    <li><b>Advantages:</b>
        <ul>
            <li><b>Encapsulation of Business Logic:</b> Centralizes complex business rules and data processing within the database, ensuring consistency and reusability across applications.</li>
            <li><b>Performance Improvement:</b> Stored procedures are precompiled and cached by the database engine, reducing parsing and execution time for repeated calls.</li>
            <li><b>Security:</b> You can grant users permission to execute procedures without giving direct access to underlying tables, reducing the risk of unauthorized data access or modification.</li>
            <li><b>Reduced Network Traffic:</b> Multiple SQL statements can be batched and executed in a single call, minimizing round-trips between application and database servers.</li>
            <li><b>Maintainability:</b> Changes to business logic can be made in one place (the procedure) without modifying application code.</li>
        </ul>
    </li>
    <li><b>Disadvantages:</b>
        <ul>
            <li><b>Deployment and Versioning Complexity:</b> Managing changes to stored procedures across environments (development, staging, production) can be more challenging than deploying application code, especially in teams or CI/CD pipelines.</li>
            <li><b>Potential for Increased Database Load:</b> Moving significant logic to the database can shift processing load from application servers to the database server, which may become a bottleneck under heavy use.</li>
            <li><b>Split Logic:</b> Business logic may be divided between application code and stored procedures, making it harder to trace, debug, and maintain overall system behavior.</li>
            <li><b>Portability Issues:</b> Stored procedure syntax and features can vary between database systems, making migrations or multi-database support more difficult.</li>
            <li><b>Testing and Debugging:</b> Debugging stored procedures is often less straightforward than debugging application code, and automated testing tools may be less mature.</li>
        </ul>
    </li>
</ul>

<p>
    <b>Summary:</b> Stored procedures are powerful for encapsulating logic, improving performance, and enhancing security, but they require careful management to avoid maintainability and deployment challenges. Use them when centralized logic and performance gains outweigh the added complexity.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">3. Can you perform INSERT/UPDATE/DELETE operations inside a SQL function? Why or why not?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    In most relational database systems, <b>user-defined functions (UDFs) are not allowed to perform data modification operations</b> such as <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code> on tables. This restriction is enforced to ensure that functions remain <b>deterministic</b> (always return the same result for the same input) and <b>side-effect free</b>. Functions are designed to be used within queries (e.g., in <code>SELECT</code>, <code>WHERE</code>, or <code>JOIN</code> clauses), and allowing data modifications could lead to unpredictable results, recursion, or performance issues.</p>

<ul>
    <li><b>SQL Server:</b> Scalar and table-valued functions cannot modify database state. Attempting to use DML statements inside a function will result in an error.</li>
    <li><b>PostgreSQL:</b> Functions written in SQL cannot perform DML; only procedural languages (like PL/pgSQL) allow limited modifications, and even then, such functions are not safe for use in queries.</li>
    <li><b>Oracle:</b> Standard SQL functions cannot modify data, but <b>autonomous transactions</b> in PL/SQL allow limited exceptions (not recommended for general use).</li>
</ul>

<p><b style="color:#B9770E;">Reason:</b></p>
<ul>
    <li><b>Determinism:</b> Functions must return consistent results and not depend on or alter external state.</li>
    <li><b>Query Safety:</b> Functions are often called many times during query execution; side effects could cause data corruption or unpredictable behavior.</li>
    <li><b>Optimization:</b> The query optimizer assumes functions are read-only, enabling better execution plans.</li>
</ul>

<p><b style="color:#B9770E;">Example (SQL Server):</b></p>

```sql
-- This will fail with an error
CREATE FUNCTION dbo.TryInsertEmployee(@Name NVARCHAR(50))
RETURNS INT
AS
BEGIN
    INSERT INTO Employees (FirstName) VALUES (@Name); -- Not allowed
    RETURN 1;
END;
-- Error: Invalid use of a side-effecting operator 'INSERT' within a function.
```

<p>
    <b>Summary:</b> Use <b>stored procedures</b> for operations that modify data. Use <b>functions</b> for computations, lookups, or logic that must be embedded in queries and remain side-effect free.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">4. What is a table-valued function and when would you use one in a query?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>table-valued function (TVF)</b> is a user-defined function that returns a table data type, rather than a single scalar value. TVFs can be used in the <code>FROM</code> clause of a query, just like a regular table or view. They are powerful for encapsulating reusable logic that produces a set of rows, such as filtering, joining, or transforming data based on input parameters.
</p>

<ul>
    <li><b>Inline TVF:</b> Returns the result of a single SELECT statement. Efficient and commonly used for simple logic.</li>
    <li><b>Multi-statement TVF:</b> Allows multiple statements and more complex logic, but may have performance overhead.</li>
    <li><b>Use Cases:</b> Encapsulate business rules, simplify complex joins, return filtered or computed sets, or modularize query logic for reuse.</li>
</ul>

<p><b style="color:#B9770E;">Example (SQL Server):</b></p>

```sql
-- Inline table-valued function: returns all employees in a given department
CREATE FUNCTION dbo.GetEmployeesByDept(@DeptID INT)
RETURNS TABLE
AS
RETURN (
    SELECT EmployeeID, FirstName, LastName
    FROM Employees
    WHERE DepartmentID = @DeptID
);

-- Usage in a query
SELECT * FROM dbo.GetEmployeesByDept(10);
```

<p>
    <b>Explanation:</b><br>
    - The function <code>GetEmployeesByDept</code> takes a department ID as input and returns a table of employees in that department.<br>
    - You can use the function in the <code>FROM</code> clause, join it with other tables, or filter its results further.<br>
    - TVFs help modularize and reuse query logic, making code easier to maintain and test.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Table-Valued Function Use Cases
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Scenario</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example Usage</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Reusable filtering logic</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Get all active customers by region</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Encapsulate business rules</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Return employees eligible for a bonus</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Simplify complex joins</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Return orders with computed totals</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Table-valued functions are ideal for encapsulating and reusing set-based query logic. Use them to simplify queries, enforce consistency, and modularize business rules that return multiple rows.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">5. When would you use a stored procedure instead of inline SQL queries in an application?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>stored procedure</b> is preferred over inline SQL queries in an application when you need to encapsulate business logic, improve security, enhance maintainability, or optimize performance. Stored procedures are precompiled and stored in the database, allowing you to centralize logic, reduce code duplication, and control access more effectively.
</p>

<ul>
    <li><b>Centralized Business Logic:</b> Complex calculations, validations, or data processing rules can be implemented once in a stored procedure and reused by multiple applications or users, ensuring consistency and reducing maintenance effort.</li>
    <li><b>Security:</b> By granting users permission to execute stored procedures (rather than direct table access), you can restrict data access and prevent unauthorized modifications. This also helps prevent SQL injection attacks, as parameters are handled safely by the database engine.</li>
    <li><b>Performance:</b> Stored procedures are compiled and cached by the database, reducing parsing and execution time for repeated operations. They can also batch multiple SQL statements, minimizing network round-trips between the application and the database.</li>
    <li><b>Maintainability:</b> Changes to business logic or data access can be made in the stored procedure without modifying application code, simplifying updates and deployments.</li>
    <li><b>Transaction Control:</b> Stored procedures can manage transactions (BEGIN, COMMIT, ROLLBACK) to ensure atomicity and consistency for multi-step operations.</li>
    <li><b>Auditing and Logging:</b> Procedures can include logic for auditing, logging, or error handling, which is harder to enforce with scattered inline SQL.</li>
</ul>

<p><b style="color:#B9770E;">Example Scenario:</b><br>
    Suppose you have a payroll application that needs to calculate bonuses, update salaries, and log changes. Instead of writing inline SQL in the application, you can create a stored procedure:
</p>

```sql
CREATE PROCEDURE ProcessPayroll
    @EmpID INT,
    @Bonus DECIMAL(10,2)
AS
BEGIN
    BEGIN TRANSACTION;
    UPDATE Employees SET Salary = Salary + @Bonus WHERE EmployeeID = @EmpID;
    INSERT INTO PayrollAudit (EmployeeID, Bonus, ProcessedAt) VALUES (@EmpID, @Bonus, GETDATE());
    COMMIT TRANSACTION;
END;
```

<p>
    The application simply calls <code>EXEC ProcessPayroll @EmpID, @Bonus</code>, ensuring all business rules, auditing, and transaction control are handled in one place.
</p>

<p>
    <b>Summary:</b> Use stored procedures for reusable, secure, and efficient data operations, especially when logic is complex, shared, or requires transaction management. Inline SQL is suitable for simple, one-off queries, but stored procedures offer greater control and maintainability for enterprise applications.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">6. How do you pass parameters to and receive results from stored procedures?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    Stored procedures accept parameters to make them flexible and reusable. Parameters can be of three types: <b>input</b> (provide values to the procedure), <b>output</b> (return values from the procedure), and <b>input/output</b> (both supply and return values). Results from stored procedures can be received in several ways:
</p>

<ul>
    <li><b>Input Parameters:</b> Used to pass values into the procedure for processing (e.g., filtering by ID).</li>
    <li><b>Output Parameters:</b> Used to return values back to the caller (e.g., computed results, status codes).</li>
    <li><b>Return Values:</b> A single integer value can be returned using the <code>RETURN</code> statement (often used for status or error codes).</li>
    <li><b>Result Sets:</b> Procedures can return one or more result sets using <code>SELECT</code> statements, which can be read by the calling application.</li>
</ul>

<p><b style="color:#B9770E;">Example (SQL Server):</b></p>

```sql
-- Define a stored procedure with input and output parameters
CREATE PROCEDURE GetEmployeeDetails
    @EmpID INT,                      -- Input parameter
    @FirstName NVARCHAR(50) OUTPUT,  -- Output parameter
    @LastName NVARCHAR(50) OUTPUT    -- Output parameter
AS
BEGIN
    SELECT 
        @FirstName = FirstName, 
        @LastName = LastName
    FROM Employees
    WHERE EmployeeID = @EmpID;
END;

-- Call the procedure and receive output parameters
DECLARE @FName NVARCHAR(50), @LName NVARCHAR(50);
EXEC GetEmployeeDetails 1, @FName OUTPUT, @LName OUTPUT;
SELECT @FName AS FirstName, @LName AS LastName;
```

<p>
    <b>Returning a Result Set:</b><br>
    A procedure can also return a result set directly using <code>SELECT</code>:
</p>

```sql
CREATE PROCEDURE GetEmployeesByDepartment
    @DeptID INT
AS
BEGIN
    SELECT EmployeeID, FirstName, LastName
    FROM Employees
    WHERE DepartmentID = @DeptID;
END;

-- Usage:
EXEC GetEmployeesByDepartment 10;
```

<p>
    <b>Returning a Value with RETURN:</b><br>
    You can use <code>RETURN</code> to send back a single integer (commonly used for status codes):
</p>

```sql
CREATE PROCEDURE CheckEmployeeExists
    @EmpID INT
AS
BEGIN
    IF EXISTS (SELECT 1 FROM Employees WHERE EmployeeID = @EmpID)
        RETURN 1; -- Exists
    ELSE
        RETURN 0; -- Does not exist
END;

-- Usage:
DECLARE @Result INT;
EXEC @Result = CheckEmployeeExists 1;
SELECT @Result AS ExistsFlag;
```

<ul>
    <li><b>Input parameters</b> are specified in the procedure definition and passed when calling the procedure.</li>
    <li><b>Output parameters</b> must be declared as <code>OUTPUT</code> in both the procedure and the call.</li>
    <li><b>Result sets</b> are retrieved using <code>SELECT</code> inside the procedure and read by the caller (application or script).</li>
    <li><b>Return values</b> are captured using the <code>RETURN</code> keyword and can be assigned to a variable when executing the procedure.</li>
</ul>

<p>
    <b>Summary:</b> Stored procedures support flexible parameter passing and can return results via output parameters, result sets, or return values. Choose the method that best fits your use case and calling environment.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">7. How would you debug or test a slow or failing stored procedure in production?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
Debugging or testing a slow or failing stored procedure in production requires a systematic approach to identify the root cause and minimize impact on users. Here are the recommended steps:
</p>

<ul>
    <li><b>Capture the Actual Execution Plan:</b> Use tools like SQL Server Management Studio (SSMS), <code>SHOWPLAN</code>, or <code>EXPLAIN</code> to obtain the execution plan. Look for table scans, missing indexes, or expensive operations that may cause slowness.</li>
    <li><b>Monitor Performance Metrics:</b> Check CPU, memory, and I/O usage on the database server. Use built-in monitoring tools (e.g., SQL Profiler, Extended Events, Performance Monitor) to track resource consumption during procedure execution.</li>
    <li><b>Enable Logging or Add Debug Output:</b> Temporarily add <code>PRINT</code> statements, logging to a debug table, or use <code>RAISE NOTICE</code> (PostgreSQL) to trace variable values and control flow. This helps pinpoint where the procedure is failing or slowing down.</li>
    <li><b>Check for Blocking and Deadlocks:</b> Use system views (e.g., <code>sys.dm_tran_locks</code>, <code>sp_who2</code>) or monitoring tools to detect if the procedure is waiting on locks or involved in a deadlock.</li>
    <li><b>Test with Representative Data in a Non-Production Environment:</b> Reproduce the issue using a copy of production data in a development or staging environment. This allows safe experimentation and tuning without affecting live users.</li>
    <li><b>Review Recent Changes:</b> Investigate any recent schema modifications, index changes, or data growth that could impact performance. Roll back or adjust changes if necessary.</li>
    <li><b>Optimize Queries and Indexes:</b> Refactor inefficient queries, add or update indexes, and avoid unnecessary cursors or loops. Use query hints judiciously if needed.</li>
    <li><b>Check for Parameter Sniffing Issues:</b> If performance varies with different inputs, consider using local variables or <code>OPTION (RECOMPILE)</code> to avoid suboptimal plans.</li>
    <li><b>Analyze Error Logs and Exception Handling:</b> Review database and application logs for error messages or exceptions related to the procedure.</li>
</ul>

<p>
    <b>Summary:</b> Debugging stored procedures involves analyzing execution plans, monitoring system resources, tracing logic, and testing in a safe environment. Always document findings and changes, and coordinate with your DBA or operations team when working in production.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">8. How do you grant a user permission to execute a specific stored procedure?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    To allow a user to execute a specific stored procedure without granting broader access to the underlying tables or database, you use the <code>GRANT EXECUTE</code> statement. This provides the user with permission to run the procedure, but not to modify or view the procedure's code or access other database objects directly.
</p>

<ul>
    <li><b>Principle of Least Privilege:</b> Granting execute permission on a stored procedure is a best practice for security, as it restricts the user's actions to only what the procedure allows.</li>
    <li><b>Granular Control:</b> You can grant execute permission on individual procedures, groups of procedures, or all procedures within a schema, depending on your requirements.</li>
    <li><b>Revoking Permission:</b> If needed, you can later revoke the permission using the <code>REVOKE EXECUTE</code> statement.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example (SQL Server):</b></p>

```sql
-- Grant execute permission on a specific stored procedure to a user
GRANT EXECUTE ON OBJECT::GetEmployeeByID TO [username];
```

<ul>
    <li><code>OBJECT::GetEmployeeByID</code> specifies the stored procedure.</li>
    <li><code>[username]</code> is the database user or role you want to grant permission to.</li>
</ul>

<p><b style="color:#B9770E;">Example (Oracle):</b></p>

```sql
GRANT EXECUTE ON GetEmployeeByID TO username;
```

<p>
    <b>Explanation:</b><br>
    - The user can now execute the <code>GetEmployeeByID</code> procedure using <code>EXEC GetEmployeeByID</code> or equivalent.<br>
    - The user cannot alter, drop, or view the procedure's definition unless granted additional permissions.<br>
    - This approach is commonly used to expose business logic through stored procedures while protecting sensitive data and enforcing security policies.
</p>

<p>
    <b>Summary:</b> Use <code>GRANT EXECUTE</code> to securely allow users to run specific stored procedures, following the principle of least privilege and maintaining tight control over database access.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">1. What is a trigger in SQL, and when would you use one? Give an example use case.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>trigger</b> is a special type of stored procedure that is automatically executed (or "triggered") by the database engine in response to specific events on a table or view, such as <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code> operations. Triggers are used to enforce business rules, maintain data integrity, automate system tasks, or audit changes without requiring explicit calls from application code.
</p>

<ul>
    <li><b>Use Cases:</b>
        <ul>
            <li><b>Auditing:</b> Automatically log changes to sensitive data (e.g., salary updates, deletions).</li>
            <li><b>Enforcing Business Rules:</b> Prevent invalid data changes, such as disallowing deletion of a parent row if child rows exist.</li>
            <li><b>Maintaining Derived Data:</b> Keep summary or aggregate tables up to date when base data changes.</li>
            <li><b>Cascading Actions:</b> Implement custom cascading updates or deletes not natively supported by foreign keys.</li>
            <li><b>Synchronizing Tables:</b> Copy or replicate data between tables automatically.</li>
        </ul>
    </li>
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

<p>
    <i>This trigger fires automatically after any <code>UPDATE</code> to the <code>Employees</code> table. If an employee's salary changes, it inserts a record into the <code>SalaryAudit</code> table, capturing the employee ID, old salary, new salary, and the timestamp of the change. This is useful for auditing and compliance purposes, ensuring all salary modifications are tracked without requiring changes to application code.</i>
</p>

<p>
    <b>Summary:</b> Triggers are powerful tools for automating responses to data changes, enforcing complex business logic, and maintaining data integrity. Use them judiciously, as they can introduce hidden logic and impact performance if overused.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">2. What is the difference between an AFTER trigger and an INSTEAD OF trigger (e.g. in SQL Server)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    In SQL Server, <b>AFTER</b> and <b>INSTEAD OF</b> triggers are both used to respond to data modification events (<code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>), but they differ in when and how they execute:
</p>

<ul>
    <li><b>AFTER Trigger:</b> Executes <b>after</b> the triggering DML operation has completed and the data has been modified in the table. Used for auditing, enforcing business rules, or cascading changes. If the trigger fails, the entire transaction is rolled back.</li>
    <li><b>INSTEAD OF Trigger:</b> Executes <b>instead of</b> the triggering DML operation. The original operation does not occur unless explicitly performed inside the trigger. Commonly used on views to enable custom logic for <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code> operations that would otherwise be invalid.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        AFTER vs INSTEAD OF Trigger Comparison
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Trigger Type</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">When It Fires</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Typical Use Case</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">AFTER</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">After the DML operation completes</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Auditing, enforcing rules, cascading actions</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">INSTEAD OF</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">In place of the DML operation</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Custom logic for views, complex updates</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example:</b></p>

```sql
-- AFTER trigger on a table (audit log)
CREATE TRIGGER trg_AfterInsert
ON Employees
AFTER INSERT
AS
BEGIN
    INSERT INTO AuditLog (EmployeeID, Action, ActionDate)
    SELECT EmployeeID, 'INSERT', GETDATE() FROM inserted;
END;

-- INSTEAD OF trigger on a view (custom update logic)
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

<p>
    <b>Summary:</b> Use <b>AFTER triggers</b> to respond to completed data changes on tables. Use <b>INSTEAD OF triggers</b> to override or customize DML operations, especially on views or when special handling is required.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
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
The <b>ACID</b> properties are a set of four key guarantees that ensure reliable processing of database transactions. They are fundamental to maintaining data integrity, especially in multi-user and concurrent environments. Each letter in ACID stands for a specific property:
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        ACID Properties Explained
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Property</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Description</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><b>Atomicity</b></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">A transaction is an indivisible unit: either all its operations succeed, or none do. If any part fails, the entire transaction is rolled back.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Transferring money between accounts: both debit and credit must succeed, or neither happens.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><b>Consistency</b></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">A transaction brings the database from one valid state to another, maintaining all defined rules (constraints, triggers, cascades).</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">A transaction cannot violate foreign key or unique constraints.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><b>Isolation</b></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Concurrent transactions do not affect each other’s intermediate states. Each transaction executes as if it were the only one running.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Two users updating the same data do not see each other's uncommitted changes.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><b>Durability</b></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Once a transaction is committed, its changes are permanent—even in the event of a system crash or power failure.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">After a successful transfer, the updated balances remain even if the server restarts.</td>
        </tr>
    </tbody>
</table>

<ul>
    <li><b>Atomicity:</b> Guarantees "all or nothing" execution for transactions.</li>
    <li><b>Consistency:</b> Ensures data validity before and after the transaction.</li>
    <li><b>Isolation:</b> Prevents concurrent transactions from interfering with each other.</li>
    <li><b>Durability:</b> Makes committed changes permanent and crash-proof.</li>
</ul>

<p>
    <b>Summary:</b> The ACID properties are essential for reliable, predictable, and safe database operations. They protect data integrity and enable robust multi-user applications.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">2. What are the different SQL isolation levels (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE), and what phenomena do they prevent (dirty reads, non-repeatable reads, phantom reads)?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
SQL isolation levels define how transaction integrity is maintained when multiple transactions occur concurrently. Each level balances data consistency and system performance by controlling which changes made by one transaction are visible to others. The main phenomena controlled by isolation levels are:
</p>
<ul>
    <li><b>Dirty Read:</b> Reading uncommitted changes from another transaction.</li>
    <li><b>Non-Repeatable Read:</b> A row read twice in the same transaction returns different values (due to another transaction's update/commit).</li>
    <li><b>Phantom Read:</b> New rows added or removed by another transaction appear/disappear in repeated queries within the same transaction.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        SQL Isolation Levels and Prevented Phenomena
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Isolation Level</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Dirty Reads</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Non-Repeatable Reads</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Phantom Reads</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">READ UNCOMMITTED</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#C0392B;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#C0392B;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#C0392B;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Lowest isolation; transactions can see uncommitted changes from others. Fastest, but least safe.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">READ COMMITTED</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#27AE60;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#C0392B;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#C0392B;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Default in most databases; only committed data is visible. Non-repeatable and phantom reads can occur.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">REPEATABLE READ</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#27AE60;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#27AE60;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#C0392B;">Possible</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ensures rows read cannot change during the transaction. New rows (phantoms) may still appear.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SERIALIZABLE</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#27AE60;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#27AE60;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px; color:#27AE60;">Prevented</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Highest isolation; transactions are fully isolated as if run sequentially. Safest, but slowest and most restrictive.</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Higher isolation levels prevent more anomalies but can reduce concurrency and increase locking. Choose the level that best fits your application's consistency and performance needs.
</p>

<ul>
    <li><b>READ UNCOMMITTED:</b> Use for reporting or analytics where dirty data is acceptable and performance is critical.</li>
    <li><b>READ COMMITTED:</b> Good default for most OLTP workloads; balances safety and concurrency.</li>
    <li><b>REPEATABLE READ:</b> Use when you need consistent reads of the same data within a transaction (e.g., financial calculations).</li>
    <li><b>SERIALIZABLE:</b> Use for critical operations requiring strict consistency, such as end-of-day batch processing.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Isolation Level Use Cases
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Isolation Level</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Typical Use Case</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">READ UNCOMMITTED</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Fast reporting, analytics, non-critical reads</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">READ COMMITTED</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">General OLTP, web applications</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">REPEATABLE READ</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Financial calculations, batch processing</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SERIALIZABLE</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Critical transactions, strict data integrity</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Tip:</b> Always test your application's behavior under different isolation levels to ensure the right balance between consistency and performance.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">3. What is a deadlock in database terms, and how can you prevent or resolve deadlocks?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
A <b>deadlock</b> is a situation in a database where two or more transactions are each waiting for the other to release a lock, causing all of them to remain blocked indefinitely. Deadlocks are a classic concurrency problem in multi-user database systems and can halt progress unless resolved by the database engine.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Deadlock Scenario Example
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Transaction 1</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Transaction 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                Locks <b>Table A</b><br>
                Tries to lock <b>Table B</b> (blocked)
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                Locks <b>Table B</b><br>
                Tries to lock <b>Table A</b> (blocked)
            </td>
        </tr>
    </tbody>
</table>

<ul>
    <li><b>Symptoms:</b> Queries hang or time out; database engine logs deadlock errors.</li>
    <li><b>Detection:</b> Most modern databases automatically detect deadlocks and resolve them by rolling back one of the involved transactions (the "deadlock victim").</li>
</ul>

<p><b style="color:#B9770E;">How to Prevent Deadlocks:</b></p>
<ul>
    <li><b>Access Resources in a Consistent Order:</b> Always acquire locks on tables and rows in the same order in all transactions.</li>
    <li><b>Keep Transactions Short:</b> Minimize the time locks are held by keeping transactions as brief as possible.</li>
    <li><b>Use Lower Isolation Levels:</b> Where appropriate, use <code>READ COMMITTED</code> or <code>READ UNCOMMITTED</code> to reduce locking contention.</li>
    <li><b>Avoid User Interaction in Transactions:</b> Do not prompt for user input or perform long-running operations inside transactions.</li>
    <li><b>Index Appropriately:</b> Proper indexing can reduce the number of locked rows and the duration of locks.</li>
</ul>

<p><b style="color:#B9770E;">How to Resolve Deadlocks:</b></p>
<ul>
    <li><b>Automatic Resolution:</b> The database engine detects the deadlock and rolls back one transaction, allowing others to proceed.</li>
    <li><b>Manual Intervention:</b> If deadlocks are frequent, analyze deadlock graphs or logs to identify problematic queries and refactor them.</li>
    <li><b>Retry Logic:</b> Implement retry mechanisms in application code to handle deadlock errors gracefully.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Deadlock Prevention & Resolution Strategies
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Strategy</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Consistent Lock Order</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Always lock tables/rows in the same order in all transactions.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Short Transactions</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Reduce lock duration by keeping transactions brief.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Retry Logic</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Automatically retry transactions that are rolled back due to deadlocks.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Analyze Deadlock Graphs</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Use database tools to identify and fix deadlock-prone queries.</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Deadlocks are a natural risk in concurrent systems. Prevent them by designing transactions carefully and resolving them by letting the database engine choose a victim and retrying as needed.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">4. How do you control transactions in SQL (BEGIN, COMMIT, ROLLBACK)? Give an example of using a transaction in a stored procedure or batch.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
A <b>transaction</b> is a sequence of one or more SQL statements executed as a single unit of work. Transactions ensure that either all operations succeed (commit) or none take effect (rollback), preserving data integrity. You control transactions using the following commands:
</p>

<ul>
    <li><b>BEGIN TRANSACTION</b> (or <code>START TRANSACTION</code>): Starts a new transaction block.</li>
    <li><b>COMMIT:</b> Saves all changes made during the transaction to the database.</li>
    <li><b>ROLLBACK:</b> Undoes all changes made during the transaction, reverting the database to its previous state.</li>
</ul>

<p>
    Transactions are essential for operations that must be atomic, such as transferring money between accounts, batch updates, or multi-step data modifications.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Transaction Control Commands
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Command</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>BEGIN TRANSACTION</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Start a new transaction</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>COMMIT</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Make all changes permanent</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ROLLBACK</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Undo all changes since the transaction began</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example: Atomic Money Transfer</b></p>

Suppose you want to transfer funds between two accounts. Both updates must succeed together, or neither should happen.

```sql
BEGIN TRANSACTION;
    UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;
    UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 2;
    IF @@ERROR <> 0
        ROLLBACK;
    ELSE
        COMMIT;
```
<p><i>This ensures that if either update fails (e.g., insufficient funds, constraint violation), the entire transaction is rolled back and no money is lost or created.</i></p>

<p><b style="color:#B9770E;">Example: Transaction in a Stored Procedure (SQL Server)</b></p>

```sql
CREATE PROCEDURE TransferFunds
    @FromAccount INT,
    @ToAccount INT,
    @Amount DECIMAL(10,2)
AS
BEGIN
    BEGIN TRANSACTION;
    BEGIN TRY
        UPDATE Accounts SET Balance = Balance - @Amount WHERE AccountID = @FromAccount;
        UPDATE Accounts SET Balance = Balance + @Amount WHERE AccountID = @ToAccount;
        COMMIT;
    END TRY
    BEGIN CATCH
        ROLLBACK;
        THROW;
    END CATCH
END;
```
<p><i>This stored procedure safely transfers funds and ensures all-or-nothing execution, with error handling for robustness.</i></p>

<ul>
    <li><b>Tip:</b> Always use transactions for multi-step operations that must be atomic and consistent.</li>
    <li><b>Note:</b> Syntax may vary slightly between SQL dialects (e.g., MySQL uses <code>START TRANSACTION</code>).</li>
</ul>

<p>
    <b>Summary:</b> Use <code>BEGIN TRANSACTION</code>, <code>COMMIT</code>, and <code>ROLLBACK</code> to control atomicity and consistency in SQL. Transactions are critical for reliable, error-proof data operations.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">5. If you run a long SELECT query on a table while another transaction is updating rows in that table, will your session see the old data or new data by default? (Consider default isolation level behavior.)</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    By default, most databases use the <b>READ COMMITTED</b> isolation level. In this mode, a <code>SELECT</code> query only sees data that has been committed at the moment each row is read—not necessarily at the start of the query. This means:
</p>

<ul>
    <li>If another transaction updates and commits a row <b>before</b> your SELECT reads it, you will see the <b>new (updated)</b> data.</li>
    <li>If your SELECT reads a row <b>before</b> the other transaction commits its update, you will see the <b>old (pre-update)</b> data.</li>
    <li>You may see a mix of old and new data within the same query if the update commits during your SELECT's execution (this is called a <b>non-repeatable read</b>).</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Isolation Level Impact on SELECT Visibility
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Isolation Level</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">SELECT Sees</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Phenomena</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">READ COMMITTED (default)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Latest committed data at time of row read</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Non-repeatable reads possible</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">REPEATABLE READ</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data as of start of query/transaction</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevents non-repeatable reads</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SERIALIZABLE</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Data as of start of transaction; strictest</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevents phantoms and non-repeatable reads</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example Scenario:</b></p>

<ol>
    <li><b>Transaction A</b> starts a long SELECT on <code>Employees</code>.</li>
    <li><b>Transaction B</b> updates a row and commits while Transaction A's SELECT is still running.</li>
    <li>If Transaction A's SELECT has not yet read that row, it will see the updated value. If it already read the row, it will see the old value.</li>
</ol>

<p>
    <b>Summary:</b> With the default <b>READ COMMITTED</b> isolation, your SELECT may see a mix of old and new data depending on when each row is read and when updates are committed. For consistent results, use <b>REPEATABLE READ</b> or <b>SERIALIZABLE</b> isolation levels.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">6. What is the difference between pessimistic and optimistic locking, and when would you use each?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
Locking strategies are essential for managing concurrent access to data in multi-user database environments. The two primary approaches are <b>pessimistic locking</b> and <b>optimistic locking</b>. Each has its own use cases, advantages, and trade-offs.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Pessimistic vs Optimistic Locking
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Aspect</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Pessimistic Locking</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Optimistic Locking</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">How it works</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Locks data as soon as it is read or before it is updated, preventing others from modifying it until the transaction completes.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Allows multiple transactions to read data without locking; checks for conflicts only when updating, typically using a version or timestamp column.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Concurrency</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Lower concurrency; can cause blocking and deadlocks.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Higher concurrency; conflicts detected at commit time.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Best for</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">High-conflict scenarios (e.g., banking, inventory management).</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Low-conflict scenarios (e.g., web apps, reporting, most OLTP workloads).</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Implementation</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Database locks (row/table locks, SELECT ... FOR UPDATE).</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Version columns, timestamps, or checksums.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Drawbacks</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Can reduce throughput and cause contention.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">May require retry logic if conflicts are detected.</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Pessimistic Locking Example:</b></p>

```sql
-- Lock a row for update (blocks others)
SELECT * FROM accounts WHERE account_id = 1 FOR UPDATE;
-- Perform updates, then COMMIT or ROLLBACK
```
<p><i>This prevents other transactions from reading or updating the locked row until the transaction completes.</i></p>

<p><b style="color:#B9770E;">Optimistic Locking Example:</b></p>

Suppose you have a <code>version</code> column in your table:

```sql
-- Step 1: Read the row and note the version
SELECT account_id, balance, version FROM accounts WHERE account_id = 1;

-- Step 2: Attempt to update, checking the version
UPDATE accounts
SET balance = balance + 100, version = version + 1
WHERE account_id = 1 AND version = 5;
```
<p><i>If the version has changed since you read it, the update affects 0 rows, indicating a conflict (someone else updated it first).</i></p>

<ul>
    <li><b>Pessimistic Locking:</b> Use when data contention is high and consistency is critical (e.g., financial transactions).</li>
    <li><b>Optimistic Locking:</b> Use when conflicts are rare and you want maximum concurrency (e.g., most web applications).</li>
</ul>

<p>
    <b>Summary:</b> <b>Pessimistic locking</b> prevents conflicts by locking data up front but can reduce performance. <b>Optimistic locking</b> allows more concurrency and only checks for conflicts at update time, making it ideal for most modern applications where write conflicts are infrequent.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">7. What is a savepoint in a transaction, and how do you use it?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
A <b>savepoint</b> is a marker set within a transaction that allows you to partially roll back to a specific point, rather than rolling back the entire transaction. Savepoints provide finer control over error handling and complex transactional logic, especially in long or multi-step transactions. They are useful when you want to undo only part of the work done in a transaction without losing all previous successful operations.
</p>

<ul>
    <li><b>Granular Rollback:</b> Roll back to a savepoint to undo only the changes made after that point.</li>
    <li><b>Multiple Savepoints:</b> You can set multiple savepoints within a single transaction and roll back to any of them as needed.</li>
    <li><b>Supported In:</b> Most major databases (SQL Server, PostgreSQL, Oracle, MySQL with InnoDB) support savepoints.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Savepoint Commands Overview
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Command</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SAVEPOINT savepoint_name;</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Creates a named savepoint within the current transaction.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ROLLBACK TO SAVEPOINT savepoint_name;</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Undoes all changes after the savepoint, but keeps the transaction open.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>RELEASE SAVEPOINT savepoint_name;</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Removes the savepoint (optional; some DBs do this automatically).</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example: Using Savepoints in a Transaction</b></p>

Suppose you are transferring funds between two accounts and want to ensure that if the second update fails, you can roll back only that part, not the entire transaction.

```sql
BEGIN TRANSACTION;
    UPDATE Accounts SET Balance = Balance - 100 WHERE AccountID = 1;
    SAVEPOINT after_debit;
    UPDATE Accounts SET Balance = Balance + 100 WHERE AccountID = 2;
    -- Suppose the above update fails, roll back to the savepoint:
    ROLLBACK TO SAVEPOINT after_debit;
    -- Optionally, try a different operation or log the error
COMMIT;
```
<p><i>In this example, if the credit to AccountID 2 fails, only that operation is undone; the debit from AccountID 1 remains unless you roll back further or the whole transaction.</i></p>

<ul>
    <li><b>Tip:</b> Use savepoints for complex business logic, error recovery, or when partial success is acceptable within a transaction.</li>
    <li><b>Note:</b> Savepoints are only valid within the current transaction scope. Rolling back the entire transaction discards all savepoints.</li>
</ul>

<p>
    <b>Summary:</b> Savepoints provide flexible, granular control over transaction rollback, making them invaluable for robust error handling and complex transactional workflows.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">8. How do two-phase commit protocols work in distributed transactions?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
The <b>two-phase commit (2PC)</b> protocol is a standard method for ensuring <b>atomicity</b> and <b>consistency</b> across multiple databases or systems involved in a single distributed transaction. It coordinates all participating nodes (databases, services, etc.) so that either <b>all</b> commit the transaction or <b>all</b> roll it back, even in the presence of failures. This prevents data inconsistencies in distributed environments.</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Two-Phase Commit Protocol Steps
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Phase</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Coordinator Action</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Participant Action</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><b>1. Prepare (Voting)</b></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Sends <b>PREPARE</b> request to all participants, asking if they can commit.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Each participant tries to prepare (e.g., writes to a log, locks resources) and replies <b>YES</b> (ready to commit) or <b>NO</b> (cannot commit).</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;"><b>2. Commit (Decision)</b></td>
            <td style="border:1px solid #D5D8DC; padding:8px;">If all reply <b>YES</b>, sends <b>COMMIT</b> to all; if any reply <b>NO</b>, sends <b>ROLLBACK</b> to all.</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">On <b>COMMIT</b>, each participant commits and releases resources. On <b>ROLLBACK</b>, each undoes changes.</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example Scenario:</b></p>

<ul>
    <li><b>Bank Transfer:</b> Moving money from an account in Database A to another in Database B. Both must succeed or fail together.</li>
</ul>

<ol>
    <li><b>Prepare Phase:</b> Coordinator asks both databases if they can commit the transfer. Each checks constraints and locks rows.</li>
    <li><b>Commit Phase:</b> If both reply YES, coordinator tells both to commit. If either says NO (e.g., insufficient funds), coordinator tells both to roll back.</li>
</ol>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Two-Phase Commit: Key Points
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Advantage</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Drawback</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Ensures atomicity and consistency across distributed systems</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Can block resources if a participant or coordinator crashes (blocking protocol)</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Prevents partial commits in distributed transactions</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Adds network and logging overhead; not ideal for high-latency or unreliable networks</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> The <b>two-phase commit protocol</b> is the foundation for reliable distributed transactions, ensuring all-or-nothing outcomes across multiple systems. While robust, it can introduce blocking and performance trade-offs, so it's best used when strong consistency is required.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">9. How can you identify and terminate a blocking or long-running transaction in a SQL database?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
Identifying and terminating blocking or long-running transactions is crucial for maintaining database performance and availability. Blocking transactions can prevent other queries from executing, leading to slowdowns or application timeouts. Most relational databases provide tools and system views to help you detect and resolve these issues.
</p>

<ul>
    <li><b>Identify Blocking or Long-Running Transactions:</b>
        <ul>
            <li><b>SQL Server:</b> Use system views such as <code>sys.dm_exec_requests</code>, <code>sys.dm_tran_locks</code>, and <code>sys.dm_os_waiting_tasks</code> to find blocking sessions. The <code>sp_who2</code> stored procedure is also commonly used to list active sessions and identify blockers.</li>
            <li><b>Oracle:</b> Query <code>v$session</code>, <code>v$locked_object</code>, and <code>v$session_longops</code> to find sessions holding locks or running long operations.</li>
            <li><b>PostgreSQL:</b> Use <code>pg_stat_activity</code> and <code>pg_locks</code> to monitor active queries and lock holders.</li>
            <li><b>MySQL:</b> Use <code>SHOW PROCESSLIST</code> or query <code>information_schema.PROCESSLIST</code> to see running queries and their states.</li>
        </ul>
    </li>
    <li><b>Terminate the Problematic Session:</b>
        <ul>
            <li><b>SQL Server:</b> Use <code>KILL session_id;</code> to terminate a specific session.</li>
            <li><b>Oracle:</b> Use <code>ALTER SYSTEM KILL SESSION 'sid,serial#';</code> to end a session.</li>
            <li><b>PostgreSQL:</b> Use <code>SELECT pg_terminate_backend(pid);</code> to terminate a backend process.</li>
            <li><b>MySQL:</b> Use <code>KILL thread_id;</code> to stop a running query or connection.</li>
        </ul>
    </li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Identifying and Terminating Blocking Sessions by Database
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Database</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Identify Blocking Session</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Terminate Session</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SQL Server</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>sp_who2</code>, <code>sys.dm_exec_requests</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>KILL session_id;</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Oracle</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>v$session</code>, <code>v$locked_object</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ALTER SYSTEM KILL SESSION 'sid,serial#';</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">PostgreSQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>pg_stat_activity</code>, <code>pg_locks</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SELECT pg_terminate_backend(pid);</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">MySQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SHOW PROCESSLIST</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>KILL thread_id;</code></td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Example (SQL Server):</b></p>

```sql
-- Find blocking sessions
EXEC sp_who2;

-- Terminate a session (replace 53 with the actual session_id)
KILL 53;
```

<p><b style="color:#B9770E;">Example (PostgreSQL):</b></p>

```sql
-- Find long-running queries
SELECT pid, usename, state, query_start, query
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY query_start;

-- Terminate a session (replace 12345 with the actual pid)
SELECT pg_terminate_backend(12345);
```

<ul>
    <li><b>Tip:</b> Always investigate the cause of blocking before terminating sessions, as killing a session can roll back uncommitted work and affect users or applications.</li>
    <li><b>Monitor regularly:</b> Set up alerts for long-running or blocking transactions to proactively manage performance.</li>
</ul>

<p>
    <b>Summary:</b> Use system views and monitoring tools to identify blocking or long-running transactions, and terminate them using the appropriate command for your database system. Regular monitoring and quick intervention help maintain database health and application responsiveness.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">10. What is deadlock detection, and how does the database engine choose a deadlock victim?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
Deadlock detection is a mechanism used by database engines to identify situations where two or more transactions are waiting indefinitely for each other to release locks, resulting in a cycle that cannot be resolved without intervention. Instead of letting transactions hang forever, the database actively monitors for deadlocks and takes action to resolve them automatically.
</p>

<ul>
    <li><b>Detection Process:</b> The database engine periodically scans the lock manager's wait-for graph to look for cycles (deadlocks). If a cycle is found, it means a deadlock exists.</li>
    <li><b>Choosing a Victim:</b> Once a deadlock is detected, the engine must break the cycle by rolling back one of the involved transactions—the "deadlock victim." The choice is typically based on minimizing the cost and impact:
        <ul>
            <li><b>Least Cost:</b> The transaction that has done the least amount of work (fewest changes, shortest duration, lowest resource usage) is usually chosen as the victim.</li>
            <li><b>User Priority:</b> Some databases allow you to set a deadlock priority, so lower-priority transactions are more likely to be chosen as victims.</li>
            <li><b>Rollback:</b> The victim transaction is rolled back, releasing its locks and allowing the other transactions to proceed. The application receives an error and can retry if needed.</li>
        </ul>
    </li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Deadlock Detection & Resolution Workflow
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Step</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">1. Monitor Locks</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Database engine tracks which transactions are waiting for which locks.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">2. Detect Cycle</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Engine scans for cycles in the wait-for graph (deadlock detection algorithm).</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">3. Select Victim</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Chooses the transaction with the lowest cost or priority to roll back.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">4. Rollback & Notify</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Victim transaction is rolled back, locks are released, and an error is sent to the application.</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">5. Continue</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Other transactions can now proceed, breaking the deadlock.</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Example (SQL Server):</b><br>
    SQL Server automatically detects deadlocks and chooses a victim based on the <code>DEADLOCK_PRIORITY</code> and the amount of work done. The victim receives error 1205 ("Transaction (Process ID) was deadlocked on resources...").
</p>

<p>
    <b>Summary:</b> Deadlock detection ensures that your database does not hang indefinitely due to resource contention. By automatically identifying and resolving deadlocks, the engine maintains system availability and allows applications to handle errors gracefully—often by retrying the failed transaction.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">

<blockquote style="border-left: 5px solid #F1C40F; background: #FCF3CF; padding: 0.7em 1.2em; border-radius:0.005px; text-align:left;">
    <b style="color:#154360; font-size:1.5em;">Performance Tuning & Query Optimization</b>
</blockquote>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">1. What is a query execution plan and how do you use it to improve performance?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
A <b>query execution plan</b> is a detailed roadmap generated by the database engine that outlines how a SQL query will be executed. It includes the sequence of operations (such as scans, joins, sorts), the access methods (e.g., index seek, table scan), and the estimated cost of each step. By analyzing the execution plan, you can identify inefficiencies like full table scans, missing indexes, or suboptimal join strategies, and then optimize your queries or schema accordingly.
</p>

<ul>
    <li><b>How to View:</b> Use <code>EXPLAIN</code> (MySQL, PostgreSQL), <code>EXPLAIN PLAN</code> (Oracle), or graphical tools (SQL Server Management Studio, pgAdmin, etc.).</li>
    <li><b>Optimization:</b> Look for expensive operations (e.g., table scans), add or adjust indexes, rewrite queries, or refactor schema based on plan insights.</li>
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
            <td style="border:1px solid #D5D8DC; padding:8px;">Reads all rows in a table; slow for large tables</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Index Seek</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Efficiently finds rows using an index</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Nested Loop Join</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Efficient for small result sets or indexed joins</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Hash Join</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Good for joining large, unsorted data sets</td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
EXPLAIN SELECT * FROM Employees WHERE DepartmentID = 10;
```
<p><i>This command shows the execution plan for the query, including whether an index is used.</i></p>

<p>
    <b>Summary:</b> Always review execution plans for slow queries to identify and resolve performance bottlenecks.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">2. How would you optimize a slow SQL query in production?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
Optimizing a slow query involves a systematic approach:
</p>
<ul>
    <li><b>Analyze the Execution Plan:</b> Identify bottlenecks such as full table scans, missing indexes, or expensive joins.</li>
    <li><b>Add Indexes:</b> Create indexes on columns used in WHERE, JOIN, and ORDER BY clauses.</li>
    <li><b>Rewrite Queries:</b> Simplify complex queries, avoid unnecessary subqueries, and use set-based operations instead of row-by-row processing.</li>
    <li><b>Select Only Needed Columns:</b> Avoid <code>SELECT *</code>; retrieve only the columns you need.</li>
    <li><b>Partition Large Tables:</b> Use table partitioning to improve query performance on very large datasets.</li>
    <li><b>Update Statistics & Rebuild Indexes:</b> Ensure the query optimizer has up-to-date statistics and that indexes are not fragmented.</li>
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
    <b>Summary:</b> Use a combination of indexing, query rewriting, and regular maintenance for optimal performance.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">3. What is the difference between UNION and UNION ALL in SQL, and when would you use each?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
<b>UNION</b> combines the results of two queries and removes duplicate rows. <b>UNION ALL</b> combines results and keeps all duplicates. <b>UNION ALL</b> is faster because it does not perform the extra step of removing duplicates.
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
            <td style="border:1px solid #D5D8DC; padding:8px;">Slower (deduplication required)</td>
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
To identify duplicate rows in a table, you typically use the <code>GROUP BY</code> clause on the columns that define a duplicate, combined with the <code>HAVING</code> clause to filter groups that occur more than once. This approach helps you find which values are repeated and how many times they appear.
</p>

<ul>
    <li><b>Step 1:</b> Decide which columns define a duplicate (e.g., all columns, or a subset such as <code>email</code> or <code>first_name, last_name</code>).</li>
    <li><b>Step 2:</b> Use <code>GROUP BY</code> on those columns and count the occurrences.</li>
    <li><b>Step 3:</b> Use <code>HAVING COUNT(*) &gt; 1</code> to filter only the duplicates.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

```sql
-- Example: Find duplicates based on column1 and column2
SELECT column1, column2, COUNT(*) AS duplicate_count
FROM table_name
GROUP BY column1, column2
HAVING COUNT(*) > 1;
```
<p><i>This query lists each combination of <code>column1</code> and <code>column2</code> that appears more than once, along with the number of times it occurs.</i></p>

<p>
    <b>Example Scenario:</b><br>
    Suppose you have a <code>users</code> table with columns <code>email</code> and <code>username</code>, and you want to find duplicate emails:
</p>

```sql
SELECT email, COUNT(*) AS duplicate_count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```
<p><i>This returns all email addresses that appear more than once in the <code>users</code> table.</i></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Sample Output
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">email</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">duplicate_count</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">ashish@example.com</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">3</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">sunil@example.com</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">2</td>
        </tr>
    </tbody>
</table>

<p>
    <b>To retrieve the full duplicate rows</b> (not just the duplicate values), you can join the results back to the original table:
</p>

```sql
SELECT t.*
FROM table_name t
JOIN (
    SELECT column1, column2
    FROM table_name
    GROUP BY column1, column2
    HAVING COUNT(*) > 1
) dup
ON t.column1 = dup.column1 AND t.column2 = dup.column2;
```
<p><i>This returns all rows from <code>table_name</code> that are considered duplicates based on <code>column1</code> and <code>column2</code>.</i></p>

<p>
    <b>Summary:</b> Use <code>GROUP BY</code> and <code>HAVING COUNT(*) &gt; 1</code> to find duplicates. Adjust the columns in <code>GROUP BY</code> to match your definition of a duplicate row.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">5. Write a SQL query to find the 10th highest salary in an Employee table.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
To find the 10th highest salary, you need to rank the unique salary values in descending order and select the one at position 10. There are several approaches, depending on your SQL dialect and requirements (e.g., handling duplicate salaries).
</p>

<ul>
    <li><b>Approach 1: Subquery with DISTINCT, ORDER BY, LIMIT/OFFSET (MySQL, PostgreSQL)</b></li>
</ul>

<p>
    This method selects the top 10 unique salaries in descending order, then picks the minimum (which is the 10th highest).
</p>

```sql
SELECT MIN(Salary) AS TenthHighestSalary
FROM (
    SELECT DISTINCT Salary
    FROM Employee
    ORDER BY Salary DESC
    LIMIT 10
) AS Top10;
```
<p><i>This returns the 10th highest unique salary. If there are fewer than 10 unique salaries, it returns NULL.</i></p>

<ul>
    <li><b>Approach 2: Using OFFSET (MySQL, PostgreSQL)</b></li>
</ul>

<p>
    You can also use <code>OFFSET</code> to directly get the 10th highest salary:
</p>

```sql
SELECT DISTINCT Salary
FROM Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 9;
```
<p><i>This returns the 10th highest unique salary (OFFSET is zero-based).</i></p>

<ul>
    <li><b>Approach 3: Using Window Functions (SQL Server, PostgreSQL, Oracle)</b></li>
</ul>

<p>
    Window functions like <code>DENSE_RANK()</code> can be used to assign a rank to each unique salary:
</p>

```sql
SELECT Salary AS TenthHighestSalary
FROM (
    SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk
    FROM Employee
) t
WHERE rnk = 10;
```
<p><i>This works in databases that support window functions and handles ties (duplicate salaries) correctly.</i></p>

<ul>
    <li><b>Approach 4: Correlated Subquery (Standard SQL)</b></li>
</ul>

<p>
    This approach counts how many distinct salaries are greater than the current one:
</p>

```sql
SELECT Salary AS TenthHighestSalary
FROM Employee e1
WHERE (
    SELECT COUNT(DISTINCT Salary)
    FROM Employee e2
    WHERE e2.Salary > e1.Salary
) = 9
LIMIT 1;
```
<p><i>This returns the 10th highest unique salary. If there are fewer than 10 unique salaries, it returns no row.</i></p>

<p>
    <b>Summary:</b> Use <code>DISTINCT</code> to ignore duplicate salaries. Choose the approach that fits your SQL dialect and performance needs. Window functions are preferred for clarity and efficiency in modern databases.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">6. How would you retrieve the last 5 records (by date or ID) from a table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
To retrieve the last 5 records from a table, you need to determine which column defines the "order" of your data—typically a date column (e.g., <code>created_at</code>, <code>order_date</code>) or a unique, incrementing ID (e.g., <code>id</code>, <code>record_id</code>). You then sort the table in descending order by that column and use the <code>LIMIT</code> clause (or its equivalent) to fetch only the top 5 rows. This approach works in most SQL databases, including MySQL, PostgreSQL, and SQLite.</p>

<ul>
    <li><b>Step 1:</b> Identify the column that determines the record order (e.g., <code>date_column</code> or <code>id</code>).</li>
    <li><b>Step 2:</b> Use <code>ORDER BY</code> in descending order (<code>DESC</code>) to bring the latest or highest values to the top.</li>
    <li><b>Step 3:</b> Use <code>LIMIT 5</code> to restrict the result to the last 5 records.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Examples:</b></p>

<ul>
    <li><b>By Date:</b></li>
</ul>

```sql
SELECT *
FROM table_name
ORDER BY date_column DESC
LIMIT 5;
```
<p><i>This returns the 5 most recent records based on <code>date_column</code>.</i></p>

<ul>
    <li><b>By ID (assuming higher IDs are newer):</b></li>
</ul>

```sql
SELECT *
FROM table_name
ORDER BY id DESC
LIMIT 5;
```
<p><i>This returns the 5 records with the highest (latest) IDs.</i></p>

<ul>
    <li><b>To return the last 5 records in ascending order (oldest to newest among the last 5):</b></li>
</ul>

```sql
SELECT *
FROM (
    SELECT *
    FROM table_name
    ORDER BY date_column DESC
    LIMIT 5
) AS last_five
ORDER BY date_column ASC;
```
<p><i>This subquery first selects the last 5 records, then reorders them in ascending order.</i></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Retrieval Methods by SQL Dialect
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Database</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Syntax</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">MySQL / PostgreSQL / SQLite</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ORDER BY column DESC LIMIT 5</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SQL Server</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SELECT TOP 5 * FROM table_name ORDER BY column DESC</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Oracle</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>SELECT * FROM (SELECT * FROM table_name ORDER BY column DESC) WHERE ROWNUM &lt;= 5</code></td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Use <code>ORDER BY ... DESC LIMIT 5</code> to get the last 5 records by date or ID. Adjust the column and syntax for your database system.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">7. Write a SQL query to exclude specific values (e.g., select all rows except those where ID is X or Y).</b>

<p><b style="color:#B9770E;">Answer:</b><br>
To exclude specific values from your query results, use the <code>NOT IN</code> operator or multiple <code>!=</code> (or <code>&lt;&gt;</code>) conditions in the <code>WHERE</code> clause. This is useful when you want to filter out rows with certain values in a column, such as excluding students with specific IDs.
</p>

<ul>
    <li><b>NOT IN:</b> Excludes all rows where the column matches any value in the list.</li>
    <li><b>!= or &lt;&gt;:</b> Excludes rows matching a single value; combine with <code>AND</code> for multiple exclusions.</li>
    <li><b>NOT EQUALS (for a single value):</b> Use <code>WHERE ID != X</code> or <code>WHERE ID &lt;&gt; X</code>.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Examples:</b></p>

<ul>
    <li><b>Exclude multiple values using NOT IN:</b></li>
</ul>

```sql
SELECT *
FROM Student
WHERE ID NOT IN (101, 102);
```
<p><i>This query returns all students except those with ID 101 or 102.</i></p>

<ul>
    <li><b>Exclude a single value using != (or &lt;&gt;):</b></li>
</ul>

```sql
SELECT *
FROM Student
WHERE ID != 101;
-- or
SELECT *
FROM Student
WHERE ID <> 101;
```
<p><i>This returns all students except the one with ID 101.</i></p>

<ul>
    <li><b>Exclude multiple values using AND:</b></li>
</ul>

```sql
SELECT *
FROM Student
WHERE ID != 101 AND ID != 102;
```
<p><i>This is equivalent to using <code>NOT IN (101, 102)</code>.</i></p>

<ul>
    <li><b>Exclude values in a string column:</b></li>
</ul>

```sql
SELECT *
FROM Student
WHERE Name NOT IN ('Ashish', 'Sunil');
```
<p><i>This excludes students named Ashish or Sunil.</i></p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Exclusion Methods Comparison
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Method</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Use Case</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">NOT IN</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Exclude multiple values</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ID NOT IN (101, 102)</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">!= or &lt;&gt;</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Exclude a single value</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ID != 101</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">AND with !=</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Exclude several values (few)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ID != 101 AND ID != 102</code></td>
        </tr>
    </tbody>
</table>

<p>
    <b>Notes:</b>
    <ul>
        <li>If the column contains <code>NULL</code> values, <code>NOT IN</code> may return no rows if any value in the list is <code>NULL</code>. Use <code>IS NOT NULL</code> if needed.</li>
        <li>For large exclusion lists, <code>NOT IN</code> is more concise and readable.</li>
    </ul>
</p>

<p>
    <b>Summary:</b> Use <code>NOT IN</code> to exclude multiple values, or <code>!=</code>/<code>&lt;&gt;</code> for single values. Adjust the column and values as needed for your query.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">8. How do you retrieve the Nth record (e.g., the 3rd record) from a table?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
Retrieving the Nth record from a table depends on the SQL dialect and whether you want the Nth row in a specific order. The most common approach is to use <code>ORDER BY</code> with <code>LIMIT</code> and <code>OFFSET</code> (supported in MySQL, PostgreSQL, SQLite), or <code>ROW_NUMBER()</code> window function (in SQL Server, PostgreSQL, Oracle).
</p>

<ul>
    <li><b>Step 1:</b> Decide the column(s) that define the order (e.g., <code>created_at</code>, <code>id</code>).</li>
    <li><b>Step 2:</b> Use <code>ORDER BY</code> to specify the order.</li>
    <li><b>Step 3:</b> Use <code>OFFSET</code> to skip the first N-1 rows and <code>LIMIT 1</code> to get the Nth row.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Examples:</b></p>

<ul>
    <li><b>MySQL / PostgreSQL / SQLite:</b></li>
</ul>

```sql
SELECT *
FROM table_name
ORDER BY ordering_column
LIMIT 1 OFFSET N-1;
```
<p><i>For example, to get the 3rd record (N=3):</i></p>

```sql
SELECT *
FROM table_name
ORDER BY ordering_column
LIMIT 1 OFFSET 2;
```
<p><i>This returns the 3rd row in the specified order (OFFSET is zero-based).</i></p>

<ul>
    <li><b>SQL Server:</b></li>
</ul>

```sql
SELECT *
FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY ordering_column) AS rn
    FROM table_name
) t
WHERE rn = N;
```
<p><i>Replace <code>N</code> with the desired row number (e.g., 3 for the 3rd record).</i></p>

<ul>
    <li><b>Oracle:</b></li>
</ul>

```sql
SELECT *
FROM (
    SELECT t.*, ROW_NUMBER() OVER (ORDER BY ordering_column) AS rn
    FROM table_name t
)
WHERE rn = N;
```

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Nth Record Retrieval Methods by SQL Dialect
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Database</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Syntax</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">MySQL / PostgreSQL / SQLite</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ORDER BY ... LIMIT 1 OFFSET N-1</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SQL Server / Oracle</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>ROW_NUMBER() OVER (ORDER BY ...) = N</code></td>
        </tr>
    </tbody>
</table>

<p>
    <b>Notes:</b>
    <ul>
        <li>If the table has no explicit ordering, the result may be unpredictable. Always use <code>ORDER BY</code> for deterministic results.</li>
        <li>For large tables, ensure the ordering column is indexed for better performance.</li>
    </ul>
</p>

<p>
    <b>Summary:</b> Use <code>ORDER BY</code> with <code>LIMIT 1 OFFSET N-1</code> (or <code>ROW_NUMBER()</code> in SQL Server/Oracle) to retrieve the Nth record in a specified order.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">9. How do you obtain the CREATE TABLE DDL for an existing table in SQL?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
To obtain the <b>CREATE TABLE</b> DDL (Data Definition Language) statement for an existing table, you use database-specific commands or tools that generate the SQL statement required to recreate the table structure, including columns, data types, constraints, indexes, and other properties. This is useful for documentation, migration, backup, or recreating tables in another environment.
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        DDL Retrieval Methods by Database
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Database</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">How to Get CREATE TABLE DDL</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">MySQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Use <code>SHOW CREATE TABLE</code> command</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                <code>SHOW CREATE TABLE employees;</code>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">PostgreSQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                Use <code>pg_dump</code> with <code>--schema-only</code> or query <code>pg_catalog</code>/<code>information_schema</code>. Many GUI tools (e.g., pgAdmin) also provide "Generate SQL" or "DDL" options.
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                <code>pg_dump -U username -d dbname -t employees --schema-only</code>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SQL Server</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                Use SQL Server Management Studio (SSMS): right-click table &rarr; Script Table as &rarr; CREATE To &rarr; New Query Editor Window. Or use <code>sp_help</code> for table details.
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                <i>SSMS GUI: Script Table as &rarr; CREATE To</i>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Oracle</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                Use <code>DBMS_METADATA.GET_DDL</code> function or tools like SQL Developer.
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                <code>SELECT DBMS_METADATA.GET_DDL('TABLE', 'EMPLOYEES') FROM DUAL;</code>
            </td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SQLite</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                Query <code>sqlite_master</code> table for the SQL statement.
            </td>
            <td style="border:1px solid #D5D8DC; padding:8px;">
                <code>SELECT sql FROM sqlite_master WHERE type='table' AND name='employees';</code>
            </td>
        </tr>
    </tbody>
</table>

<ul>
    <li><b>GUI Tools:</b> Most database management tools (e.g., MySQL Workbench, pgAdmin, SSMS, Oracle SQL Developer) provide right-click options to generate the CREATE TABLE script for any table.</li>
    <li><b>Command-Line Utilities:</b> Utilities like <code>mysqldump</code>, <code>pg_dump</code>, or <code>expdp</code> (Oracle) can export DDL for tables or entire schemas.</li>
    <li><b>Information Schema:</b> For advanced scripting, you can query metadata tables (e.g., <code>information_schema.columns</code>) to reconstruct DDL, but this is rarely needed for standard use cases.</li>
</ul>
<p><b style="color:#B9770E;">Example Output (MySQL):</b></p>

```sql
SHOW CREATE TABLE employees;
```

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        SHOW CREATE TABLE employees Result
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Table</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Create Table</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px; vertical-align:top;">employees</td>
            <td style="border:1px solid #D5D8DC; padding:8px; font-family:monospace; white-space:pre;">
CREATE TABLE `employees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            </td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Use the appropriate command or tool for your database system to generate the CREATE TABLE DDL for an existing table. This is essential for migrations, backups, and documentation.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">10. Explain the difference between the RANK() and DENSE_RANK() window functions.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
<b>RANK()</b> and <b>DENSE_RANK()</b> are window functions used to assign a ranking number to each row within a result set, based on the ordering of one or more columns. They are commonly used for tasks like leaderboard generation, top-N queries, and reporting. The key difference between them is how they handle ties (rows with equal values in the ordering column).
</p>

<ul>
    <li><b>RANK():</b> Assigns the same rank to tied rows, but leaves gaps in the ranking sequence after the tie. The next rank after a tie is incremented by the number of tied rows.</li>
    <li><b>DENSE_RANK():</b> Also assigns the same rank to tied rows, but does not leave gaps. The next rank after a tie is incremented by one, regardless of the number of tied rows.</li>
</ul>

<p><b style="color:#B9770E;">Syntax:</b></p>

```sql
SELECT
    column1,
    RANK() OVER (ORDER BY column2 DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY column2 DESC) AS dense_rank
FROM table_name;
```

<p><b style="color:#B9770E;">Example:</b></p>

Suppose you have a <code>Scores</code> table:

| Player | Score |
|--------|-------|
| A      | 100   |
| B      | 90    |
| C      | 90    |
| D      | 80    |

Applying <code>RANK()</code> and <code>DENSE_RANK()</code>:

| Player | Score | RANK() | DENSE_RANK() |
|--------|-------|--------|--------------|
| A      | 100   | 1      | 1            |
| B      | 90    | 2      | 2            |
| C      | 90    | 2      | 2            |
| D      | 80    | 4      | 3            |

<ul>
    <li>With <b>RANK()</b>, both B and C have rank 2 (tie), and the next rank is 4 (skips 3).</li>
    <li>With <b>DENSE_RANK()</b>, both B and C have rank 2, and the next rank is 3 (no gap).</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        RANK() vs DENSE_RANK() Comparison
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
            <td style="border:1px solid #D5D8DC; padding:8px;">Skips ranks after ties (gaps in ranking)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1, 2, 2, 4</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">DENSE_RANK()</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">No gaps after ties (consecutive ranking)</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">1, 2, 2, 3</td>
        </tr>
    </tbody>
</table>

<p>
    <b>When to use:</b>
    <ul>
        <li>Use <b>RANK()</b> when you want to reflect the number of tied rows in the ranking (e.g., for competition scoring where the next rank skips ahead).</li>
        <li>Use <b>DENSE_RANK()</b> when you want consecutive ranking numbers without gaps, even if there are ties (e.g., for reporting or grouping).</li>
    </ul>
</p>

<p>
    <b>Summary:</b> <b>RANK()</b> leaves gaps after ties; <b>DENSE_RANK()</b> does not. Choose based on your ranking requirements.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">11. When would you use ROW_NUMBER(), RANK(), or DENSE_RANK() in a query? Give a use case.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
<code>ROW_NUMBER()</code>, <code>RANK()</code>, and <code>DENSE_RANK()</code> are window functions used to assign a sequential number or rank to rows within a result set, based on a specified ordering. They are commonly used for tasks such as pagination, ranking, deduplication, and leaderboard generation. The choice among them depends on how you want to handle ties (rows with equal values in the ordering column).</p>

<ul>
    <li>
        <b>ROW_NUMBER():</b> Assigns a unique sequential number to each row within the partition, regardless of ties. No two rows get the same number, even if their values are identical.
        <ul>
            <li><b>Use Case:</b> Pagination (fetching rows N to M), removing duplicates (keeping only the first occurrence), or selecting the "top N" per group.</li>
        </ul>
    </li>
    <li>
        <b>RANK():</b> Assigns the same rank to tied rows, but leaves gaps in the ranking sequence after ties. The next rank after a tie is incremented by the number of tied rows.
        <ul>
            <li><b>Use Case:</b> Competition ranking where ties should skip ranks (e.g., Olympic medals: 1, 2, 2, 4).</li>
        </ul>
    </li>
    <li>
        <b>DENSE_RANK():</b> Assigns the same rank to tied rows, but does not leave gaps. The next rank after a tie is incremented by one.
        <ul>
            <li><b>Use Case:</b> Leaderboards or reporting where consecutive ranking is desired without gaps (e.g., 1, 2, 2, 3).</li>
        </ul>
    </li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example:</b></p>

Suppose you have a <code>Sales</code> table:

| Employee | SalesAmount |
|----------|-------------|
| Alice    | 500         |
| Bob      | 400         |
| Carol    | 400         |
| Dave     | 300         |

To assign rankings based on <code>SalesAmount</code> (highest first):

```sql
SELECT
    Employee,
    SalesAmount,
    ROW_NUMBER() OVER (ORDER BY SalesAmount DESC) AS row_num,
    RANK() OVER (ORDER BY SalesAmount DESC) AS rank,
    DENSE_RANK() OVER (ORDER BY SalesAmount DESC) AS dense_rank
FROM Sales;
```

Result:

| Employee | SalesAmount | row_num | rank | dense_rank |
|----------|-------------|---------|------|------------|
| Alice    | 500         | 1       | 1    | 1          |
| Bob      | 400         | 2       | 2    | 2          |
| Carol    | 400         | 3       | 2    | 2          |
| Dave     | 300         | 4       | 4    | 3          |

<ul>
    <li><b>ROW_NUMBER():</b> Each row gets a unique number (no ties).</li>
    <li><b>RANK():</b> Bob and Carol tie for 2nd place, so both get rank 2; the next rank is 4 (gap).</li>
    <li><b>DENSE_RANK():</b> Bob and Carol tie for 2nd, both get 2; the next rank is 3 (no gap).</li>
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
            <td style="border:1px solid #D5D8DC; padding:8px;">Pagination, deduplication, selecting Nth row</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">RANK()</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Competition ranking with gaps after ties</td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">DENSE_RANK()</td>
            <td style="border:1px solid #D5D8DC; padding:8px;">Leaderboard or reporting with consecutive ranks</td>
        </tr>
    </tbody>
</table>

<p>
    <b>Summary:</b> Use <code>ROW_NUMBER()</code> for unique row numbering, <code>RANK()</code> for rankings with gaps after ties, and <code>DENSE_RANK()</code> for consecutive rankings without gaps. Choose based on your business logic and how you want to handle ties.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">12. Write a SQL query to compute the median number of searches made by users, given a summary table of search counts.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
The <b>median</b> is the middle value in a sorted list of numbers. If the count of values is odd, the median is the value at the center. If the count is even, the median is the average of the two central values. Calculating the median in SQL requires ordering the data and identifying the middle value(s). This is typically done using window functions such as <code>ROW_NUMBER()</code>, <code>RANK()</code>, or <code>PERCENTILE_CONT()</code> (if supported by your database).
</p>

<ul>
    <li><b>Step 1:</b> Order the search counts for all users.</li>
    <li><b>Step 2:</b> Assign a row number to each record and count the total number of records.</li>
    <li><b>Step 3:</b> Select the middle row(s) based on the total count.</li>
    <li><b>Step 4:</b> For even counts, average the two middle values; for odd counts, select the single middle value.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example (Standard SQL):</b></p>

Suppose you have a table <code>user_search_summary</code> with columns <code>user_id</code> and <code>search_count</code>.

```sql
SELECT AVG(search_count) AS median_searches
FROM (
    SELECT
        search_count,
        ROW_NUMBER() OVER (ORDER BY search_count) AS rn,
        COUNT(*) OVER () AS total
    FROM user_search_summary
) t
WHERE
    rn = (total + 1) / 2
    OR (total % 2 = 0 AND rn = (total / 2) + 1);
```

<ul>
    <li>This query works for both odd and even numbers of rows.</li>
    <li>For odd counts, it selects the middle row. For even counts, it averages the two central rows.</li>
    <li><code>ROW_NUMBER()</code> assigns a unique sequential number to each row in order of <code>search_count</code>.</li>
    <li><code>COUNT(*) OVER ()</code> gives the total number of rows.</li>
</ul>

<p><b style="color:#B9770E;">Alternative (Using PERCENTILE_CONT, if supported):</b></p>

Some databases (e.g., PostgreSQL, Oracle, SQL Server 2012+) support the <code>PERCENTILE_CONT</code> window function, which directly computes the median:

```sql
SELECT
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY search_count) AS median_searches
FROM user_search_summary;
```

<ul>
    <li>This is the most concise and efficient way to compute the median if your database supports it.</li>
</ul>

<p><b style="color:#B9770E;">Sample Data:</b></p>

| user_id | search_count |
|---------|-------------|
| 1       | 5           |
| 2       | 2           |
| 3       | 7           |
| 4       | 3           |
| 5       | 4           |

<ul>
    <li>Ordered <code>search_count</code>: 2, 3, 4, 5, 7</li>
    <li>Median is 4 (the third value in the sorted list)</li>
</ul>

<p>
    <b>Summary:</b> To compute the median in SQL, use window functions to rank and select the middle value(s), or use <code>PERCENTILE_CONT(0.5)</code> if available. The median provides a robust measure of central tendency, especially when data contains outliers.
</p>
<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">13. Write a SQL query to calculate the sum of odd-numbered and even-numbered measurements separately for each day.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
To calculate the sum of odd-numbered and even-numbered measurements for each day, you can use a <b>CASE</b> expression inside the <b>SUM()</b> aggregate function. This allows you to conditionally sum values based on whether the <code>measurement_number</code> is odd or even. The <code>MOD()</code> (or <code>%</code> in some databases) function is used to determine if a number is odd (<code>MOD(measurement_number, 2) = 1</code>) or even (<code>MOD(measurement_number, 2) = 0</code>).</p>

<ul>
    <li><b>Step 1:</b> Use <code>CASE</code> to check if <code>measurement_number</code> is odd or even.</li>
    <li><b>Step 2:</b> Use <code>SUM()</code> to aggregate the values for odd and even numbers separately.</li>
    <li><b>Step 3:</b> <code>GROUP BY</code> the <code>day</code> column to get results per day.</li>
</ul>

<p><b style="color:#B9770E;">Syntax & Example (Standard SQL):</b></p>

```sql
SELECT
    day,
    SUM(CASE WHEN MOD(measurement_number, 2) = 1 THEN value ELSE 0 END) AS odd_sum,
    SUM(CASE WHEN MOD(measurement_number, 2) = 0 THEN value ELSE 0 END) AS even_sum
FROM measurements
GROUP BY day;
```

<ul>
    <li><code>MOD(measurement_number, 2) = 1</code> checks for odd numbers.</li>
    <li><code>MOD(measurement_number, 2) = 0</code> checks for even numbers.</li>
    <li>Replace <code>MOD</code> with <code>%</code> if your database uses that syntax (e.g., <code>measurement_number % 2</code>).</li>
</ul>

<p><b style="color:#B9770E;">Example Data:</b></p>

| day        | measurement_number | value |
|------------|-------------------|-------|
| 2024-06-01 | 1                 | 10    |
| 2024-06-01 | 2                 | 20    |
| 2024-06-01 | 3                 | 30    |
| 2024-06-02 | 1                 | 15    |
| 2024-06-02 | 2                 | 25    |

<p><b style="color:#B9770E;">Result:</b></p>

| day        | odd_sum | even_sum |
|------------|---------|----------|
| 2024-06-01 | 40      | 20       |
| 2024-06-02 | 15      | 25       |

<ul>
    <li>For 2024-06-01: odd measurements (1 and 3) sum to 10 + 30 = 40; even measurement (2) is 20.</li>
    <li>For 2024-06-02: odd measurement (1) is 15; even measurement (2) is 25.</li>
</ul>

<p>
    <b>Summary:</b> Use <code>CASE</code> with <code>SUM()</code> and <code>MOD()</code> (or <code>%</code>) to separate and aggregate odd and even measurement values for each day.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
<b style="color:#1C4980;font-weight:bold;">14. Write a SQL query to get the average review rating for each product for each month.</b>

<p><b style="color:#B9770E;">Answer:</b><br>
To calculate the average review rating for each product for each month, you need to:
</p>
<ul>
    <li>Group reviews by <b>product</b> and by <b>month</b> (derived from the review date).</li>
    <li>Use an aggregate function (<code>AVG()</code>) to compute the average rating per group.</li>
    <li>Use a date truncation or formatting function to extract the month from the review date. The exact function depends on your SQL dialect.</li>
</ul>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <caption style="caption-side: top; font-weight: bold; color: #1C4980; padding: 6px;">
        Date Truncation Functions by SQL Dialect
    </caption>
    <thead>
        <tr style="background:#D6EAF8;">
            <th style="border:1px solid #D5D8DC; padding:8px;">Database</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Function</th>
            <th style="border:1px solid #D5D8DC; padding:8px;">Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">PostgreSQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>DATE_TRUNC('month', review_date)</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>DATE_TRUNC('month', review_date)</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">MySQL</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>DATE_FORMAT(review_date, '%Y-%m')</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>DATE_FORMAT(review_date, '%Y-%m')</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">SQL Server</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>FORMAT(review_date, 'yyyy-MM')</code> or <code>YEAR(review_date), MONTH(review_date)</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>FORMAT(review_date, 'yyyy-MM')</code></td>
        </tr>
        <tr>
            <td style="border:1px solid #D5D8DC; padding:8px;">Oracle</td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>TO_CHAR(review_date, 'YYYY-MM')</code></td>
            <td style="border:1px solid #D5D8DC; padding:8px;"><code>TO_CHAR(review_date, 'YYYY-MM')</code></td>
        </tr>
    </tbody>
</table>

<p><b style="color:#B9770E;">Syntax & Examples:</b></p>

<ul>
    <li><b>PostgreSQL:</b></li>
</ul>

```sql
SELECT
    product_id,
    DATE_TRUNC('month', review_date) AS review_month,
    AVG(rating) AS avg_rating
FROM reviews
GROUP BY product_id, DATE_TRUNC('month', review_date)
ORDER BY product_id, review_month;
```

<ul>
    <li><b>MySQL:</b></li>
</ul>

```sql
SELECT
    product_id,
    DATE_FORMAT(review_date, '%Y-%m') AS review_month,
    AVG(rating) AS avg_rating
FROM reviews
GROUP BY product_id, review_month
ORDER BY product_id, review_month;
```

<ul>
    <li><b>SQL Server:</b></li>
</ul>

```sql
SELECT
    product_id,
    FORMAT(review_date, 'yyyy-MM') AS review_month,
    AVG(rating) AS avg_rating
FROM reviews
GROUP BY product_id, FORMAT(review_date, 'yyyy-MM')
ORDER BY product_id, review_month;
```

<ul>
    <li><b>Oracle:</b></li>
</ul>

```sql
SELECT
    product_id,
    TO_CHAR(review_date, 'YYYY-MM') AS review_month,
    AVG(rating) AS avg_rating
FROM reviews
GROUP BY product_id, TO_CHAR(review_date, 'YYYY-MM')
ORDER BY product_id, review_month;
```

<p><b style="color:#B9770E;">Sample Data:</b></p>

| product_id | review_date | rating |
|------------|-------------|--------|
| 101        | 2024-05-10  | 4      |
| 101        | 2024-05-15  | 5      |
| 101        | 2024-06-01  | 3      |
| 102        | 2024-05-20  | 2      |
| 102        | 2024-06-05  | 4      |

<p><b style="color:#B9770E;">Sample Output:</b></p>

| product_id | review_month | avg_rating |
|------------|--------------|------------|
| 101        | 2024-05-01   | 4.5        |
| 101        | 2024-06-01   | 3.0        |
| 102        | 2024-05-01   | 2.0        |
| 102        | 2024-06-01   | 4.0        |

<ul>
    <li><b>Note:</b> The <code>review_month</code> column format may vary by SQL dialect (e.g., <code>2024-05-01</code> or <code>2024-05</code>).</li>
</ul>

<p>
    <b>Summary:</b> Use <code>GROUP BY</code> with a date truncation or formatting function to aggregate average ratings per product per month. Adjust the date function for your database system.
</p>

<hr style="border:1px solidrgb(0, 0, 0);">
