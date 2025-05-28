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
<!-- Section 4 -->

## <h2 style="color:#2874A6;font-weight:bold;">4. How Do You Use GROUP BY and HAVING Together? Provide an Example.</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
The <code>GROUP BY</code> clause groups rows that have the same values in specified columns into summary rows. The <code>HAVING</code> clause is used to filter groups based on a condition, typically involving aggregate functions.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
Suppose you have a table called <code>orders</code> with columns <code>customer_id</code> and <code>order_amount</code>. To find customers who have placed more than 2 orders:
</p>

```sql
SELECT
    customer_id,
    COUNT(*) AS total_orders
FROM
    orders
GROUP BY
    customer_id
HAVING
    COUNT(*) > 2;
```

<p>
<b style="color:#2874A6;">Explanation:</b>
<ul>
  <li><b>GROUP BY</b> groups the rows by <code>customer_id</code>.</li>
  <li><b>COUNT(*)</b> counts the number of orders for each customer.</li>
  <li><b>HAVING COUNT(*) &gt; 2</b> filters the groups to include only those customers with more than 2 orders.</li>
</ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
  <b>Tip:</b> Use <code>HAVING</code> to filter groups after aggregation, while <code>WHERE</code> filters rows before grouping.
</blockquote>

<hr style="border:1px solid #2E86C1;">

## <h2 style="color:#2874A6;font-weight:bold;">5. Write a Query to Find Employees Earning More Than Their Managers</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
To find employees who earn more than their managers, you typically need a table where each employee has a <code>manager_id</code> referencing another employee's <code>employee_id</code>. You can use a self-join to compare each employee's salary with their manager's salary.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
Suppose you have an <code>employees</code> table with columns <code>employee_id</code>, <code>name</code>, <code>salary</code>, and <code>manager_id</code>.
</p>

```sql
SELECT
    e.name AS employee_name,
    e.salary AS employee_salary,
    m.name AS manager_name,
    m.salary AS manager_salary
FROM
    employees e
JOIN
    employees m ON e.manager_id = m.employee_id
WHERE
    e.salary > m.salary;
```

<p>
<b style="color:#2874A6;">Explanation:</b>
<ul>
  <li>The table is joined to itself: <code>e</code> represents employees, <code>m</code> represents their managers.</li>
  <li>The <code>WHERE</code> clause filters for employees whose salary is greater than their manager's salary.</li>
</ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
  <b>Tip:</b> Make sure <code>manager_id</code> is not NULL to avoid comparing employees without managers.
</blockquote>

<hr style="border:1px solid #2E86C1;">

## <h2 style="color:#2874A6;font-weight:bold;">6. What is a Window Function in SQL? Provide Examples of ROW_NUMBER and RANK.</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
A <b>window function</b> performs a calculation across a set of table rows that are somehow related to the current row. Unlike aggregate functions, window functions do not collapse rows; they return a value for each row in the result set. Common window functions include <code>ROW_NUMBER</code>, <code>RANK</code>, <code>DENSE_RANK</code>, <code>SUM</code>, and <code>AVG</code> used with the <code>OVER</code> clause.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
Suppose you have an <code>employees</code> table with columns <code>employee_id</code>, <code>name</code>, and <code>salary</code>.
</p>

<p><b style="color:#2874A6;">ROW_NUMBER Example:</b> Assigns a unique sequential number to each row within a partition, ordered by salary descending.</p>

```sql
SELECT
    employee_id,
    name,
    salary,
    ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM
    employees;
```

<p><b style="color:#2874A6;">RANK Example:</b> Assigns a rank to each row within the result set, with gaps for ties.</p>

```sql
SELECT
    employee_id,
    name,
    salary,
    RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM
    employees;
```

<p>
<b style="color:#2874A6;">Explanation:</b>
<ul>
  <li><b>ROW_NUMBER()</b> gives each row a unique number based on the specified order.</li>
  <li><b>RANK()</b> assigns the same rank to rows with equal values, but leaves gaps in the ranking sequence for ties.</li>
  <li>The <code>OVER (ORDER BY salary DESC)</code> clause defines the window for the function, ordering employees by salary from highest to lowest.</li>
</ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
  <b>Tip:</b> Use window functions when you need to perform calculations across rows related to the current row, such as ranking, running totals, or moving averages.
</blockquote>

<hr style="border:1px solid #2E86C1;">

## <h2 style="color:#2874A6;font-weight:bold;">7. Write a Query to Fetch the Top 3 Performing Products Based on Sales</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
To find the top 3 performing products based on sales, you can aggregate the sales data by product, order the results by total sales in descending order, and then limit the output to the top 3 products.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
Suppose you have a table called <code>sales</code> with columns <code>product_id</code> and <code>sale_amount</code>, and a <code>products</code> table with <code>product_id</code> and <code>product_name</code>.
</p>

```sql
SELECT
    p.product_name,
    SUM(s.sale_amount) AS total_sales
FROM
    sales s
JOIN
    products p ON s.product_id = p.product_id
GROUP BY
    p.product_name
ORDER BY
    total_sales DESC
LIMIT 3;
```

<p>
<b style="color:#2874A6;">Explanation:</b>
<ul>
  <li><b>JOIN</b> combines the <code>sales</code> and <code>products</code> tables to get product names.</li>
  <li><b>SUM(s.sale_amount)</b> calculates the total sales for each product.</li>
  <li><b>GROUP BY</b> groups the results by product name.</li>
  <li><b>ORDER BY total_sales DESC</b> sorts products from highest to lowest sales.</li>
  <li><b>LIMIT 3</b> returns only the top 3 products.</li>
</ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
  <b>Tip:</b> Adjust the <code>LIMIT</code> value to fetch a different number of top-performing products as needed.
</blockquote>

<hr style="border:1px solid #2E86C1;">
