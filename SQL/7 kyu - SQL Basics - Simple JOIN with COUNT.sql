-- https://www.codewars.com/kata/sql-basics-simple-join-with-count/train/sql
-- My solution
select p.id, p.name, count(t.id) as toy_count
from people p join toys t on (p.id = t.people_id)
group by p.id

-- ...
SELECT
  P.id,
  P.name,
  (SELECT COUNT(*) FROM toys WHERE people_id = P.id) AS toy_count
FROM people AS P