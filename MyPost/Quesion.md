
---

<h3 style="color:#1C4980;text-align: center;">Joins</h3>

---

<table cellpadding="8" cellspacing="0" style="width:100%; border:none; color:#1C4980; border-collapse:collapse; font-family:inherit; table-layout:fixed;">
  <thead>
    <tr style="color:#1C4980;">
      <th align="center" style="border:none; color:#1C4980; width:50px; white-space:nowrap; vertical-align:top;">Sr. No.</th>
      <th align="center" style="border:none; color:#1C4980; white-space:normal;text-align: center; vertical-align:top;">Question</th>
      <th align="center" style="border:none; color:#1C4980; width:50px; white-space:nowrap; vertical-align:top;">Pg. No.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">1.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What are the different types of SQL joins (INNER, LEFT, RIGHT, FULL, CROSS, etc.) and when would you use each?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">2.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is the difference between a CROSS JOIN and a FULL OUTER JOIN?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">3.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Write a SQL query to retrieve the first and last names of employees along with the names of their managers (given Employees and Managers tables).</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">4.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Write a SQL query to find the average salary for each department, given tables Employees (with DepartmentID) and Departments (with DepartmentName).</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">5.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Write a SQL query to list all products that have never been ordered (products in a Product table with no matching rows in the Orders table).</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">6.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Write a SQL query to list all employees who are also managers (for example, employees who appear as managers in the same table).</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">7.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is a self-join, and when might you use it? Provide an example scenario.</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">8.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">How would you join more than two tables in a single SQL query? What factors affect the performance when joining multiple tables?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">9.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Explain how an OUTER JOIN works when one side has no matching rows. How does this differ from an INNER JOIN in practice?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
  </tbody>
</table>

-----

<h3 style="color:#1C4980;text-align: center;">Indexing and Keys</h3>

---

<table cellpadding="8" cellspacing="0" style="width:100%; border:none; color:#1C4980; border-collapse:collapse; font-family:inherit; table-layout:fixed;">
  <thead>
    <tr style="color:#1C4980;">
      <th align="center" style="border:none; color:#1C4980; width:50px; white-space:nowrap; vertical-align:top;">Sr. No.</th>
      <th align="center" style="border:none; color:#1C4980;text-align: center; text-align: center; white-space:normal; vertical-align:top;">Question</th>
      <th align="center" style="border:none; color:#1C4980; width:50px; white-space:nowrap; vertical-align:top;">Pg. No.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">1.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is a SQL index and what are different types of indexes (clustered, non-clustered, unique, etc.)?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">1</td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">2.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is the difference between a heap (no clustered index) and a table with a clustered index, and how can you identify a heap table?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">2</td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">3.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is the difference between a PRIMARY KEY and a UNIQUE KEY (or unique index) in SQL?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">4.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What are index “forwarding pointers” in a heap table, and how do they affect query performance?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">5.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is a composite index, and how do you choose the order of columns in it for optimal performance?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">6.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">When should you use a covering index, and how does it improve the performance of a query?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">7.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">How does the existence of an index on a column affect INSERT, UPDATE, and DELETE performance on a table?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">8.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is index selectivity, and why is it important for query optimization?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">9.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">How many clustered indexes can a table have, and why?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">10.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is index fragmentation, and how can it be resolved or mitigated in a large database?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
  </tbody>
</table>

<h3 style="color:#1C4980;text-align: center;">Normalization and Schema Design</h3>

---

<table cellpadding="8" cellspacing="0" style="width:100%; border:none; color:#1C4980; border-collapse:collapse; font-family:inherit; table-layout:fixed;">
  <thead>
    <tr style="color:#1C4980;">
      <th align="center" style="border:none; color:#1C4980; width:50px; white-space:nowrap; vertical-align:top;">Sr. No.</th>
      <th align="center" style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Question</th>
      <th align="center" style="border:none; color:#1C4980; width:50px; white-space:nowrap; vertical-align:top;">Pg. No.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">1.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is database normalization and what are the normal forms (1NF, 2NF, 3NF, BCNF)?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">2.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Given a table with repeating groups of data (e.g. Customer and multiple phone numbers), how would you normalize the table to 3NF?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">3.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Explain how denormalization can be used for performance, and what the trade-offs are (e.g. redundancy vs. speed).</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">4.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What kinds of data anomalies (insertion, update, deletion anomalies) are prevented by normalization?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">5.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">How would you design a table schema to handle a many-to-many relationship, for example between Students and Courses?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">6.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">Explain the concept of denormalization with an example scenario in a large database.</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">7.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">What is a surrogate key vs a natural key, and when would you choose each in table design?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">8.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">How do you implement a 1-to-1 relationship versus a 1-to-many relationship in table design?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">9.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">How do you enforce referential integrity without foreign key constraints? (e.g. using triggers)</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
    <tr>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;">10.</td>
      <td style="border:none; color:#1C4980; white-space:normal; vertical-align:top;">How would you handle schema migrations or changes in a production database environment?</td>
      <td align="center" style="border:none; color:#1C4980; white-space:nowrap; vertical-align:top;"></td>
    </tr>
  </tbody>
</table>
