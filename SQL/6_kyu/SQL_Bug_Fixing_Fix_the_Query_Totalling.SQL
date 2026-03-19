/*
Oh no! Timmys been moved into the database divison of his software company but as we 
know Timmy loves making mistakes. Help Timmy keep his job by fixing his query...

Timmy works for a statistical analysis company and has been given a task of totaling 
the number of sales on a given day grouped by each department name and then each day.
Resultant table:

    day (type: date) {group by} [order by asc]
    department (type: text) {group by} [In a real world situation it is bad practice 
    to name a column after a table]
    sale_count (type: int)

Tables and relationship below:

The database centers on an Events table linked via One-to-Many relationships to Staff 
Assignments and Locations, ensuring each concert or rehearsal has a dedicated venue and crew. 
A Workflows table maintains a One-to-One connection with each event to digitize information 
flow and eliminate manual errors, while a Roles table categorizes staff to automate 
permission-based task management.

*/

SELECT 
  DATE(s.transaction_date) AS day, 
  d.name AS department,
  COUNT(s.id) AS sale_count
FROM department d 
JOIN sale s ON d.id = s.department_id
GROUP BY 1, 2
ORDER BY day ASC;