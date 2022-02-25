-- https://www.codewars.com/kata/easy-sql-ordering/train/sql
-- My solution
select *
from companies
order by employees desc

-- ...
select id,ceo,motto,employees
from companies
order by 4 desc