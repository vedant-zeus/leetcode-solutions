# Write your MySQL query statement below
Select query_name , 
    round(SUM(rating/position)/count(*),2)as quality,
    round(count(case when rating < 3 then 1 end)*100/count(*),2) as poor_query_percentage
from Queries
group by query_name