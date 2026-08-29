# Write your MySQL query statement below
SELECT id , 
    CASE 
        When p_id is NULL then "Root"
        When id not in (Select Distinct p_id from Tree Where p_id is NOT NULL)
        then "Leaf"
        Else "Inner"
    End as type
from Tree ; 