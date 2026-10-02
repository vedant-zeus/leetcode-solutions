# Write your MySQL query statement below
SELECT name as Customers 
From Customers as c 
Left join Orders as o
    on c.id = o.customerId
Where o.customerId IS NULL
    