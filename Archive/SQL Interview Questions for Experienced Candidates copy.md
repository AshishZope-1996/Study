<h1 style="color:#154360; text-align:center; font-size:2.5em; font-weight:bold; margin-bottom:0; letter-spacing:1px;">
    <span style="color:#2471A3;">SQL Interview Questions for Experienced Candidates (3+ years)</span>
</h1>

<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Data Types & Miscellaneous Concepts</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Normalization & Schema Design</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Database Design Principles</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Indexing Strategies & Keys</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">
<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Mastering SQL Joins</b>
</blockquote>

<b style="color:#2874A6;font-weight:bold;">1. What are the different types of SQL joins (<code>INNER JOIN</code>, <code>LEFT JOIN</code>, <code>RIGHT JOIN</code>, <code>FULL JOIN</code>, <code>CROSS JOIN</code>, etc.) and when would you use each?</b>
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

<b style="color:#2874A6;font-weight:bold;">2. What is the difference between a <code>CROSS JOIN</code> and a <code>FULL OUTER JOIN</code>?</b>

<p><b style="color:#B9770E;">Answer:</b><br>
    <code>CROSS JOIN</code> and <code>FULL OUTER JOIN</code> are both used to combine rows from two tables, but they operate very differently:
</p>

<table style="width:100%; border-collapse:collapse; border:1px solid #D5D8DC;">
    <thead>
        <tr style="background:#F4F6F7;">
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

<b style="color:#B9770E;">Answer:</b><br>
To retrieve the first and last names of employees along with their managers' names, you typically use a <b>JOIN</b> between the <code>Employees</code> and <code>Managers</code> tables. The exact query depends on the schema, but here are two common scenarios:

<b>Scenario 1: Separate <code>Employees</code> and <code>Managers</code> Tables</b>
<ul>
    <li><code>Employees</code> table: <code>EmployeeID</code>, <code>FirstName</code>, <code>LastName</code>, <code>ManagerID</code></li>
    <li><code>Managers</code> table: <code>ManagerID</code>, <code>FirstName</code>, <code>LastName</code></li>
</ul>

<b>Query:</b>
```sql
SELECT 
    e.FirstName AS EmployeeFirstName,
    e.LastName AS EmployeeLastName,
    m.FirstName AS ManagerFirstName,
    m.LastName AS ManagerLastName
FROM Employees e
LEFT JOIN Managers m ON e.ManagerID = m.ManagerID;
```
<ul>
    <li>This query uses a <b>LEFT JOIN</b> to include employees who may not have a manager (e.g., top-level managers).</li>
</ul>

<b>Scenario 2: Self-Join on <code>Employees</code> Table (Manager is also an Employee)</b>
<ul>
    <li><code>Employees</code> table: <code>EmployeeID</code>, <code>FirstName</code>, <code>LastName</code>, <code>ManagerID</code></li>
</ul>

<b>Query:</b>
```sql
SELECT 
    e.FirstName AS EmployeeFirstName,
    e.LastName AS EmployeeLastName,
    m.FirstName AS ManagerFirstName,
    m.LastName AS ManagerLastName
FROM Employees e
LEFT JOIN Employees m ON e.ManagerID = m.EmployeeID;
```
<ul>
    <li>This <b>self-join</b> approach is common when managers are also listed as employees.</li>
</ul>

<b>Explanation:</b><br>
- The <b>LEFT JOIN</b> ensures all employees are listed, even if they do not have a manager.<br>
- The manager's name is retrieved by joining the employee's <code>ManagerID</code> to the manager's <code>EmployeeID</code>.<br>
- This pattern is useful for hierarchical data, such as organizational charts.

<b style="color:#B9770E;">Answer:</b><br>

<b>4. Write a SQL query to find the average salary for each department, given tables <code>Employees</code> (with <code>DepartmentID</code>) and <code>Departments</code> (with <code>DepartmentName</code>).</b>

To find the average salary for each department, you need to join the <code>Employees</code> and <code>Departments</code> tables on <code>DepartmentID</code>, then group by department.

**Query:**
```sql
SELECT 
    d.DepartmentName,
    AVG(e.Salary) AS AverageSalary
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID
GROUP BY d.DepartmentName;
```
- <b>INNER JOIN</b> ensures only departments with employees are included.
- <b>AVG()</b> calculates the average salary per department.
- <b>GROUP BY</b> groups results by department name.

---

<b style="color:#B9770E;">Answer:</b><br>

<b>5. Write a SQL query to list all products that have never been ordered (products in a <code>Product</code> table with no matching rows in the <code>Orders</code> table).</b>

You can use a <b>LEFT JOIN</b> and filter for NULLs in the <code>Orders</code> table, or use <code>NOT EXISTS</code>.

**Query using LEFT JOIN:**
```sql
SELECT p.*
FROM Product p
LEFT JOIN Orders o ON p.ProductID = o.ProductID
WHERE o.ProductID IS NULL;
```

**Query using NOT EXISTS:**
```sql
SELECT p.*
FROM Product p
WHERE NOT EXISTS (
    SELECT 1 FROM Orders o WHERE o.ProductID = p.ProductID
);
```
- Both queries return products that do not appear in any order.

---

<b style="color:#B9770E;">Answer:</b><br>

<b>6. Write a SQL query to list all employees who are also managers (for example, employees who appear as managers in the same table).</b>

Assuming the <code>Employees</code> table has <code>EmployeeID</code> and <code>ManagerID</code> columns:

**Query:**
```sql
SELECT DISTINCT e.*
FROM Employees e
WHERE e.EmployeeID IN (
    SELECT DISTINCT ManagerID FROM Employees WHERE ManagerID IS NOT NULL
);
```
- This finds employees whose <code>EmployeeID</code> appears as a <code>ManagerID</code> for someone else.

---

<b style="color:#B9770E;">Answer:</b><br>

<b>7. What is a <code>self-join</code>, and when might you use it? Provide an example scenario.</b>

A <b>self-join</b> is a join where a table is joined to itself. This is useful for hierarchical or recursive relationships, such as employees and their managers.

**Example Scenario:**  
Suppose you have an <code>Employees</code> table with <code>EmployeeID</code>, <code>Name</code>, and <code>ManagerID</code> (where <code>ManagerID</code> references another <code>EmployeeID</code>).

**Query:**
```sql
SELECT 
    e.Name AS Employee,
    m.Name AS Manager
FROM Employees e
LEFT JOIN Employees m ON e.ManagerID = m.EmployeeID;
```
- This lists each employee with their manager's name.
- Useful for organizational charts, bill of materials, etc.

---

<b style="color:#B9770E;">Answer:</b><br>

<b>8. How would you join more than two tables in a single SQL query? What factors affect the performance when joining multiple tables?</b>

You can join multiple tables by chaining <code>JOIN</code> clauses:

**Example:**
```sql
SELECT e.Name, d.DepartmentName, l.LocationName
FROM Employees e
INNER JOIN Departments d ON e.DepartmentID = d.DepartmentID
INNER JOIN Locations l ON d.LocationID = l.LocationID;
```

**Performance Factors:**
| Factor                | Impact                                                                 |
|-----------------------|------------------------------------------------------------------------|
| Indexes               | Proper indexes on join columns speed up joins.                         |
| Join Order            | The order of joins can affect execution plans and performance.         |
| Table Size            | Large tables increase join cost; filtering early helps.                |
| Join Type             | OUTER JOINs are generally slower than INNER JOINs.                     |
| Query Complexity      | More joins and conditions increase parsing and execution time.          |
| Database Statistics   | Up-to-date statistics help the optimizer choose efficient plans.        |

- Use <b>EXPLAIN</b> or query plans to analyze performance.
- Minimize the number of rows joined by filtering early (using <code>WHERE</code>).

---

<b style="color:#B9770E;">Answer:</b><br>

<b>9. Explain how an <code>OUTER JOIN</code> works when one side has no matching rows. How does this differ from an <code>INNER JOIN</code> in practice?</b>

| Join Type      | Rows Returned When No Match | NULLs in Result? | Use Case Example                        |
|----------------|----------------------------|------------------|-----------------------------------------|
| INNER JOIN     | Row is excluded            | No               | Only matching records from both tables  |
| LEFT OUTER JOIN| Row from left table shown, right columns NULL | Yes | All left table rows, even if no match  |
| RIGHT OUTER JOIN| Row from right table shown, left columns NULL | Yes | All right table rows, even if no match |
| FULL OUTER JOIN| Rows from both tables shown, unmatched side NULL | Yes | All rows from both tables              |

**Example:**
```sql
-- INNER JOIN: Only rows with matches
SELECT a.*, b.*
FROM A a
INNER JOIN B b ON a.id = b.a_id;

-- LEFT OUTER JOIN: All rows from A, NULLs for B if no match
SELECT a.*, b.*
FROM A a
LEFT JOIN B b ON a.id = b.a_id;
```

- <b>OUTER JOIN</b> includes unmatched rows from one or both tables, filling in NULLs for missing data.
- <b>INNER JOIN</b> only includes rows where a match exists in both tables.
- OUTER JOINs are useful for finding missing or unmatched data (e.g., customers with no orders).


<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Working with Views</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Stored Procedures & Functions</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Triggers & Automation</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Transactions & Concurrency Control</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">

<blockquote style="border-left: 5px solid #2980B9; background: #F4F6F7; padding: 0.7em 1.2em; border-radius:5px;">
    <b style="color:#154360; font-size:1.1em;">Performance Tuning & Query Optimization</b>
</blockquote>

<hr style="border:1px solid #D5D8DC;">