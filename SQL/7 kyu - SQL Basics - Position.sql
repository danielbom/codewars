-- https://www.codewars.com/kata/sql-basics-position/train/sql
-- My solution
select id, name, position(',' in characteristics) as comma
from monsters
order by comma
