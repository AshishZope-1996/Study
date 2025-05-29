# 📊 SQL Interview Preparation Guide

---

## 📑 Table of Contents

| Section                                   | Page |
|--------------------------------------------|:----:|
| [⚡ Quick Facts](#quick-facts)                |  1   |
| [🧠 Core Concepts](#core-concepts)            |  2   |
| [💻 SQL Syntax Cheatsheet](#sql-syntax-cheatsheet) |  3   |
| [❓ Sample Interview Questions](#sample-interview-questions) |  4   |
| [🚀 Advanced Topics](#advanced-topics)        |  5   |
| [🎯 Tips for Success](#tips-for-success)      |  6   |
| [🔗 Resources](#resources)                    |  7   |

---

**Answer:**  
&nbsp;&nbsp;&nbsp;&nbsp;To find duplicate rows in a table, you typically group by the columns that define a duplicate and use the `HAVING` clause to filter groups with more than one occurrence.

**Example:**  
&nbsp;&nbsp;&nbsp;&nbsp;Suppose you have a table called `employees` with columns `first_name`, `last_name`, and `email`. To find duplicates based on `first_name` and `last_name`:

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

**Explanation:**  
&nbsp;&nbsp;&nbsp;&nbsp;- `GROUP BY` groups rows with the same `first_name` and `last_name`.  
&nbsp;&nbsp;&nbsp;&nbsp;- `COUNT(*)` counts the number of occurrences for each group.  
&nbsp;&nbsp;&nbsp;&nbsp;- `HAVING COUNT(*) > 1` filters only those groups that have duplicates.

> **Tip:**  
> &nbsp;&nbsp;&nbsp;&nbsp;Adjust the columns in the `GROUP BY` clause to match the definition of a duplicate in your specific table.

---

## 🧠 Core Concepts

- **SELECT**: Retrieve data from tables.
- **WHERE**: Filter records.
- **JOIN**: Combine rows from multiple tables.
- **GROUP BY**: Aggregate data.
- **ORDER BY**: Sort results.
- **Subqueries**: Nested queries.
- **Indexes**: Improve query performance.
- **Normalization**: Organize data to reduce redundancy.

---

## 💻 SQL Syntax Cheatsheet

```sql
-- Select statement
SELECT column1, column2 FROM table WHERE condition;

-- Join example
SELECT a.name, b.salary
FROM employees a
JOIN salaries b ON a.id = b.emp_id;

-- Group By example
SELECT department, COUNT(*) 
FROM employees
GROUP BY department;
```

**Example: Calculate Sales Growth by Product**
```sql
SELECT
    p.product_id,
    q1.sales AS q1_sales,
    q2.sales AS q2_sales,
    (q2.sales - q1.sales) / NULLIF(q1.sales, 0) * 100 AS growth_rate
FROM
    (SELECT product_id, SUM(sales) AS sales
     FROM sales
     WHERE quarter = 'Q1'
     GROUP BY product_id) q1
JOIN
    (SELECT product_id, SUM(sales) AS sales
     FROM sales
     WHERE quarter = 'Q2'
     GROUP BY product_id) q2
    ON q1.product_id = q2.product_id;
```

---

## ❓ Sample Interview Questions

### 🟢 Basic

- What is SQL? What are its types?
- Explain the difference between `INNER JOIN` and `LEFT JOIN`.
- How do you find duplicate records in a table?

### 🟡 Intermediate

- Write a query to get the second highest salary from an Employee table.
- What is normalization? Explain different normal forms.
- How do you optimize a slow query?

### 🔴 Advanced

- Explain window functions with examples.
- What are CTEs (Common Table Expressions)?
- How do transactions work in SQL?

---

## 🚀 Advanced Topics

---

## 🎯 Tips for Success

- Practice writing queries by hand.
- Explain your thought process clearly.
- Optimize queries for performance.
- Be ready to discuss real-world scenarios.

---

## 🔗 Resources

- [LeetCode SQL Practice](https://leetcode.com/problemset/database/)
---

> **Good luck!** 🚀  
> _“The best way to learn SQL is to write SQL.”_
