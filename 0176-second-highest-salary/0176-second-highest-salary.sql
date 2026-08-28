With Highestsalary as (
    SELECT MAX(salary) as salary
     FROM Employee 
) 
SELECT MAX(salary) as SecondHighestSalary
From Employee
Where salary < (select salary from Highestsalary)