-- https://www.codewars.com/kata/basics-length-based-select-with-like/train/sql
-- My solution
select first_name, last_name
from names
where first_name like '______%'

-- ...
select first_name, last_name
from names
where first_name ~ '.{6,}' -- like it :P

-- ...
-- Replace with your SQL Query
select 
first_name
--,substring(first_name,6,1)
,last_name
from names
where substring(first_name,6,1) like '_'