<h1 style="color:#2E86C1; text-align:center; font-size:2.5em; font-weight:bold; margin-bottom:0; letter-spacing:1px;">
    <span style="color:#2874A6;">Scenario-Based SQL Interview Questions</span>
</h1></h1>
<hr style="border:1px solid #2E86C1;">

<!-- Section 1 -->
## <h2 style="color:#2874A6;font-weight:bold;">1. Write a Query to Find Duplicate Rows in a Table</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
To find duplicate rows in a table, group by the columns that define a duplicate and use the <code>HAVING</code> clause to filter groups with more than one occurrence.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
Suppose you have a table called <code>employees</code> with columns <code>first_name</code>, <code>last_name</code>, and <code>email</code>. To find duplicates based on <code>first_name</code> and <code>last_name</code>:
</p>

```sql
SELECT
    first_name,
    last_name,
    COUNT(*) AS duplicate_count
FROM
    employees
GROUP BY
    first_name,
    last_name
HAVING
    COUNT(*) > 1;
```

<p>
<b style="color:#2874A6;">Explanation:</b>
<ul>
  <li><b>GROUP BY</b> groups rows with the same <code>first_name</code> and <code>last_name</code>.</li>
  <li><b>COUNT(*)</b> counts the number of occurrences for each group.</li>
  <li><b>HAVING COUNT(*) &gt; 1</b> filters only those groups that have duplicates.</li>
</ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
  <b>Tip:</b> Adjust the columns in the <code>GROUP BY</code> clause to match the definition of a duplicate in your specific table.
</blockquote>

<hr style="border:1px solid #2E86C1;">

<!-- Section 2 -->
## <h2 style="color:#2874A6;font-weight:bold;">2. Explain the Difference Between INNER JOIN and OUTER JOIN with Examples</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
<b>INNER JOIN</b> returns only the rows that have matching values in both tables.<br>
<b>OUTER JOIN</b> returns all rows from one or both tables, filling in NULLs where there is no match.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
Suppose you have two tables: <code>employees</code> and <code>departments</code>.<br>
<ul>
  <li><code>employees(employee_id, name, department_id)</code></li>
  <li><code>departments(department_id, department_name)</code></li>
</ul>
</p>

<p><b style="color:#2874A6;">INNER JOIN Example:</b> Returns only employees who belong to a department.</p>

```sql
SELECT
    e.name,
    d.department_name
FROM
    employees e
INNER JOIN
    departments d ON e.department_id = d.department_id;
```

<p><b style="color:#2874A6;">OUTER JOIN Example (LEFT OUTER JOIN):</b> Returns all employees, including those who do not belong to any department.</p>

```sql
SELECT
    e.name,
    d.department_name
FROM
    employees e
LEFT OUTER JOIN
    departments d ON e.department_id = d.department_id;
```

<p>
<b style="color:#2874A6;">Explanation:</b>
<ul>
  <li><b>INNER JOIN</b> includes only rows with matching <code>department_id</code> in both tables.</li>
  <li><b>LEFT OUTER JOIN</b> includes all rows from <code>employees</code>, and fills <code>department_name</code> with NULL if there is no matching department.</li>
  <li>You can also use <b>RIGHT OUTER JOIN</b> or <b>FULL OUTER JOIN</b> to include all rows from the right table or both tables, respectively.</li>
</ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
  <b>Tip:</b> Use <code>INNER JOIN</code> when you need only matching records, and <code>OUTER JOIN</code> when you want to include unmatched rows as well.
</blockquote>

<hr style="border:1px solid #2E86C1;">

<!-- Section 3 -->
## <h2 style="color:#2874A6;font-weight:bold;">3. Write a Query to Fetch the Second-Highest Salary from an Employee Table</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
To get the second-highest salary, you can use the <code>ORDER BY</code> and <code>LIMIT</code> clauses, or use a subquery to exclude the highest salary.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
Suppose you have a table called <code>employees</code> with a column <code>salary</code>.
</p>

<p><b style="color:#2874A6;">Using LIMIT/OFFSET (works in MySQL, PostgreSQL):</b></p>

```sql
SELECT
    DISTINCT salary
FROM
    employees
ORDER BY
    salary DESC
LIMIT 1 OFFSET 1;
```

<p><b style="color:#2874A6;">Using Subquery (works in most SQL dialects):</b></p>

```sql
SELECT
    MAX(salary) AS second_highest_salary
FROM
    employees
WHERE
    salary &lt; (SELECT MAX(salary) FROM employees);
```
<p>
<b style="color:#2874A6;">Explanation:</b>
<ul>
  <li>The first query orders salaries in descending order, skips the highest, and fetches the next one.</li>
  <li>The second query finds the maximum salary that is less than the overall maximum, effectively giving the second-highest salary.</li>
  <li><b>DISTINCT</b> ensures duplicate salaries are not counted multiple times.</li>
</ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
  <b>Tip:</b> If there are multiple employees with the same second-highest salary, both queries will return that value. Adjust the query if you need all employees with the second-highest salary.
</blockquote>

<hr style="border:1px solid #2E86C1;">
