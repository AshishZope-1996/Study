<h1 style="color:#2E86C1; text-align:center; font-size:2.5em; font-weight:bold; margin-bottom:0; letter-spacing:1px;">
    <span style="color:#2874A6;">Scenario-Based SQL Interview Questions</span>
</h1>
<hr style="border:1px solid #2E86C1;">

<!-- Section 1 -->
<h2 style="color:#2874A6;font-weight:bold;">1. Write a Query to Find Duplicate Rows in a Table</h2>

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
<h2 style="color:#2874A6;font-weight:bold;">2. Explain the Difference Between INNER JOIN and OUTER JOIN with Examples</h2>

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
<h2 style="color:#2874A6;font-weight:bold;">3. Write a Query to Fetch the Second-Highest Salary from an Employee Table</h2>

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

<h2 style="color:#2874A6;font-weight:bold;">4. How Do You Use GROUP BY and HAVING Together? Provide an Example.</h2>

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

<h2 style="color:#2874A6;font-weight:bold;">5. Write a Query to Find Employees Earning More Than Their Managers</h2>

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

<h2 style="color:#2874A6;font-weight:bold;">6. What is a Window Function in SQL? Provide Examples of ROW_NUMBER and RANK.</h2>

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

<h2 style="color:#2874A6;font-weight:bold;">7. Write a Query to Fetch the Top 3 Performing Products Based on Sales</h2>

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

<h2 style="color:#2874A6;font-weight:bold;">8. Explain the Difference Between UNION and UNION ALL</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
    <code>UNION</code> and <code>UNION ALL</code> are used to combine the results of two or more <code>SELECT</code> queries. The key difference is that <code>UNION</code> removes duplicate rows from the result set, while <code>UNION ALL</code> includes all rows, even duplicates.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
    Suppose you have two tables, <code>customers_2023</code> and <code>customers_2024</code>, both with a <code>customer_id</code> column.
</p>

<p><b style="color:#2874A6;">Using UNION:</b> Removes duplicates.</p>

```sql
SELECT customer_id FROM customers_2023
UNION
SELECT customer_id FROM customers_2024;
```

<p><b style="color:#2874A6;">Using UNION ALL:</b> Includes duplicates.</p>

```sql
SELECT customer_id FROM customers_2023
UNION ALL
SELECT customer_id FROM customers_2024;
```

<p>
    <b style="color:#2874A6;">Comparison Table:</b>
</p>

<table style="width:100%; border-collapse:collapse;">
    <tr style="background-color:#D6EAF8;">
        <th style="border:1px solid #2E86C1; padding:8px;">Feature</th>
        <th style="border:1px solid #2E86C1; padding:8px;">UNION</th>
        <th style="border:1px solid #2E86C1; padding:8px;">UNION ALL</th>
    </tr>
    <tr>
        <td style="border:1px solid #2E86C1; padding:8px;">Duplicates</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Removes duplicates</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Keeps all rows, including duplicates</td>
    </tr>
    <tr>
        <td style="border:1px solid #2E86C1; padding:8px;">Performance</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Slower (due to duplicate removal)</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Faster (no duplicate check)</td>
    </tr>
    <tr>
        <td style="border:1px solid #2E86C1; padding:8px;">Use Case</td>
        <td style="border:1px solid #2E86C1; padding:8px;">When you want unique results</td>
        <td style="border:1px solid #2E86C1; padding:8px;">When you want all results, including duplicates</td>
    </tr>
</table>

<p>
    <b style="color:#2874A6;">Explanation:</b>
    <ul>
        <li><b>UNION</b> combines result sets and removes any duplicate rows.</li>
        <li><b>UNION ALL</b> combines result sets and includes all rows, even if they are duplicates.</li>
        <li>Both require the same number of columns and compatible data types in each <code>SELECT</code> statement.</li>
    </ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
    <b>Tip:</b> Use <code>UNION ALL</code> for better performance when you are sure there are no duplicates or you want to keep them.
</blockquote>

<hr style="border:1px solid #2E86C1;">

<h2 style="color:#2874A6;font-weight:bold;">9. How Do You Use a CASE Statement in SQL? Provide an Example.</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
    The <code>CASE</code> statement in SQL allows you to perform conditional logic within your queries. It works like an IF-THEN-ELSE statement, letting you return different values based on specified conditions.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
    Suppose you have an <code>employees</code> table with a <code>salary</code> column, and you want to categorize employees as 'High', 'Medium', or 'Low' earners based on their salary.
</p>

```sql
SELECT
    name,
    salary,
    CASE
        WHEN salary >= 100000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM
    employees;
```

<p>
    <b style="color:#2874A6;">Explanation:</b>
    <ul>
        <li><b>CASE</b> checks each condition in order and returns the corresponding value for the first true condition.</li>
        <li>If none of the conditions are met, the <b>ELSE</b> value is returned.</li>
        <li>The result is a new column (<code>salary_category</code>) that classifies each employee based on their salary.</li>
    </ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
    <b>Tip:</b> Use <code>CASE</code> for conditional transformations, custom groupings, or to replace IF/ELSE logic in your SQL queries.
</blockquote>


<hr style="border:1px solid #2E86C1;">


<h2 style="color:#2874A6;font-weight:bold;">10. Write a Query to Calculate the Cumulative Sum of Sales</h2>
10. Write a query to calculate the cumulative sum of sales.

<p><b style="color:#B9770E;">Answer:</b><br>
    To calculate the cumulative sum (running total) of sales, you can use the <code>SUM()</code> window function with the <code>OVER</code> clause, ordering by the relevant column (such as date or transaction ID).
</p>

<p><b style="color:#B9770E;">Example:</b><br>
    Suppose you have a table called <code>sales</code> with columns <code>sale_date</code> and <code>sale_amount</code>.
</p>

```sql
SELECT
    sale_date,
    sale_amount,
    SUM(sale_amount) OVER (ORDER BY sale_date) AS cumulative_sales
FROM
    sales;
```

<p>
    <b style="color:#2874A6;">Explanation:</b>
    <ul>
        <li><b>SUM(sale_amount) OVER (ORDER BY sale_date)</b> calculates the running total of <code>sale_amount</code> up to the current row, ordered by <code>sale_date</code>.</li>
        <li>This provides a cumulative sum for each row in the result set.</li>
        <li>You can partition the results (e.g., by customer or product) using <code>PARTITION BY</code> if needed.</li>
    </ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
    <b>Tip:</b> Cumulative sums are useful for tracking running totals, trends over time, or progress toward goals.
</blockquote>


<hr style="border:1px solid #2E86C1;">

<h2 style="color:#2874A6;font-weight:bold;">11. What is a CTE (Common Table Expression), and How Is It Used?</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
    A <b>Common Table Expression (CTE)</b> is a temporary result set defined within the execution scope of a single SQL statement. CTEs make complex queries easier to read and maintain by allowing you to break them into logical building blocks. They are defined using the <code>WITH</code> keyword and can be referenced like a table or view within the main query.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
    Suppose you want to find employees who earn more than the average salary. You can use a CTE to calculate the average salary first, then reference it in your main query.
</p>

```sql
WITH avg_salary_cte AS (
    SELECT AVG(salary) AS avg_salary
    FROM employees
)
SELECT
    name,
    salary
FROM
    employees,
    avg_salary_cte
WHERE
    employees.salary > avg_salary_cte.avg_salary;
```

<p>
    <b style="color:#2874A6;">Explanation:</b>
    <ul>
        <li>The <code>WITH</code> clause defines a CTE named <code>avg_salary_cte</code> that calculates the average salary.</li>
        <li>The main query selects employees whose salary is greater than the average, referencing the CTE as if it were a table.</li>
        <li>CTEs can simplify queries, especially when you need to reuse a subquery or perform recursive operations.</li>
    </ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
    <b>Tip:</b> Use CTEs to improve query readability and maintainability, especially for complex or multi-step data transformations.
</blockquote>


<hr style="border:1px solid #2E86C1;">


<h2 style="color:#2874A6;font-weight:bold;">12. Write a Query to Identify Customers Who Have Made Transactions Above $5,000 Multiple Times</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
    To find customers who have made transactions greater than $5,000 more than once, filter the transactions above $5,000 and group by <code>customer_id</code>, then use the <code>HAVING</code> clause to select those with a count greater than 1.
</p>

<p><b style="color:#B9770E;">Example:</b><br>
    Suppose you have a table called <code>transactions</code> with columns <code>customer_id</code> and <code>transaction_amount</code>.
</p>

```sql
SELECT
    customer_id,
    COUNT(*) AS high_value_transactions
FROM
    transactions
WHERE
    transaction_amount > 5000
GROUP BY
    customer_id
HAVING
    COUNT(*) > 1;
```

<p>
    <b style="color:#2874A6;">Explanation:</b>
    <ul>
        <li><b>WHERE transaction_amount &gt; 5000</b> filters for transactions above $5,000.</li>
        <li><b>GROUP BY customer_id</b> groups the results by customer.</li>
        <li><b>COUNT(*)</b> counts the number of high-value transactions per customer.</li>
        <li><b>HAVING COUNT(*) &gt; 1</b> selects only those customers who have made such transactions more than once.</li>
    </ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
    <b>Tip:</b> Adjust the threshold or grouping as needed to match your business requirements.
</blockquote>

<hr style="border:1px solid #2E86C1;">

<h2 style="color:#2874A6;font-weight:bold;">13. Explain the Difference Between DELETE and TRUNCATE Commands</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
    Both <code>DELETE</code> and <code>TRUNCATE</code> are used to remove data from a table, but they differ in how they operate and their effects on the table and its data.
</p>

<p>
    <b style="color:#2874A6;">Comparison Table:</b>
</p>

<table style="width:100%; border-collapse:collapse;">
    <tr style="background-color:#D6EAF8;">
        <th style="border:1px solid #2E86C1; padding:8px;">Feature</th>
        <th style="border:1px solid #2E86C1; padding:8px;">DELETE</th>
        <th style="border:1px solid #2E86C1; padding:8px;">TRUNCATE</th>
    </tr>
    <tr>
        <td style="border:1px solid #2E86C1; padding:8px;">Removes Rows</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Removes specified rows (can use WHERE clause)</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Removes all rows (cannot use WHERE clause)</td>
    </tr>
    <tr>
        <td style="border:1px solid #2E86C1; padding:8px;">Transaction Logging</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Row-by-row logging (slower for large tables)</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Minimal logging (faster for large tables)</td>
    </tr>
    <tr>
        <td style="border:1px solid #2E86C1; padding:8px;">Can Be Rolled Back</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Yes, if used within a transaction</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Yes, in most databases if used within a transaction</td>
    </tr>
    <tr>
        <td style="border:1px solid #2E86C1; padding:8px;">Resets Identity Column</td>
        <td style="border:1px solid #2E86C1; padding:8px;">No</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Yes</td>
    </tr>
    <tr>
        <td style="border:1px solid #2E86C1; padding:8px;">Triggers</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Activates DELETE triggers</td>
        <td style="border:1px solid #2E86C1; padding:8px;">Does not activate DELETE triggers</td>
    </tr>
</table>

<p>
    <b style="color:#2874A6;">Explanation:</b>
    <ul>
        <li><b>DELETE</b> is used when you need to remove specific rows and can be filtered using a <code>WHERE</code> clause.</li>
        <li><b>TRUNCATE</b> quickly removes all rows from a table and resets identity columns, but cannot be used to delete specific rows.</li>
        <li>Use <code>DELETE</code> for selective removal and <code>TRUNCATE</code> for fast, complete data removal.</li>
    </ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
    <b>Tip:</b> Use <code>TRUNCATE</code> with caution, as it cannot be used if the table is referenced by a foreign key constraint.
</blockquote>
<h2 style="color:#2874A6;font-weight:bold;">14. How Do You Optimize SQL Queries for Better Performance?</h2>

<p><b style="color:#B9770E;">Answer:</b><br>
    Optimizing SQL queries involves improving their efficiency to reduce execution time and resource usage. This can be achieved through indexing, query rewriting, and analyzing execution plans.
</p>

<p><b style="color:#B9770E;">Example Strategies:</b></p>
<ul>
    <li><b>Use Indexes:</b> Create indexes on columns used in <code>WHERE</code>, <code>JOIN</code>, and <code>ORDER BY</code> clauses to speed up data retrieval.</li>
    <li><b>Write Selective Queries:</b> Retrieve only the columns and rows you need using specific <code>SELECT</code> and <code>WHERE</code> clauses.</li>
    <li><b>Avoid SELECT *:</b> Specify only required columns to reduce data transfer and processing.</li>
    <li><b>Use Joins Efficiently:</b> Prefer appropriate join types and ensure join columns are indexed.</li>
    <li><b>Analyze Execution Plans:</b> Use tools like <code>EXPLAIN</code> to understand how queries are executed and identify bottlenecks.</li>
    <li><b>Optimize Subqueries:</b> Replace correlated subqueries with joins or CTEs when possible.</li>
    <li><b>Limit Result Sets:</b> Use <code>LIMIT</code> or <code>TOP</code> to restrict the number of rows returned.</li>
</ul>

<p>
    <b style="color:#2874A6;">Explanation:</b>
    <ul>
        <li>Indexes help the database find data faster, especially for large tables.</li>
        <li>Efficient queries reduce unnecessary data processing and network load.</li>
        <li>Reviewing execution plans helps identify slow operations like full table scans.</li>
    </ul>
</p>

<blockquote style="border-left: 4px solid #F1C40F; background: #FCF3CF; padding: 0.5em 1em;">
    <b>Tip:</b> Regularly monitor query performance and update indexes or rewrite queries as your data grows and changes.
</blockquote>

---

<div align="center" style="margin-top:2em; margin-bottom:2em;">

# 🙏 Thank You!

Thank you for reading these SQL interview notes!  
I hope they help you succeed in your learning and interviews.

If you found this helpful, consider sharing with others or revisiting whenever you need a quick refresher.

**Keep practicing, stay curious, and happy querying!**

</div>

---
