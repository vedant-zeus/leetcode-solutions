# Write your MySQL query statement below
SELECT customer_number 
FROM Orders 
Group by customer_number
Order by COUNT(customer_number) DESC
LIMIT 1