SELECT  w2.id 
from Weather as w1
JOIN Weather as w2 
    ON DATEDIFF(w2.recordDate,w1.recordDate) = 1
Where w1.temperature < w2.temperature