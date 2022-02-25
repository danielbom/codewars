-- https://www.codewars.com/kata/sql-concatenating-columns/train/sql
-- My solution
select concat_ws(' ', prefix, first, last, suffix) as title
from names

-- ...
Create Table ab as
  SELECT prefix || ' ' || first || ' ' || last || ' ' || suffix as title from names;
Select * from ab;

-- ...
SELECT format('%s %s %s %s', prefix, first, last, suffix) AS title
  FROM names

-- ...
SELECT concat(names.prefix, ' ', names.first, ' ', names.last, ' ', names.suffix) as title
  FROM names

select coalesce(n.prefix || ' ' || n.first || ' ' || n.last || ' ' || n.suffix) as title
from names as n;

-- ...
select trim(replace(concat(prefix, ' ', first, ' ', last, ' ', suffix), '  ', ' ')) as "title"
from names

-- ...
select array_to_string(array[prefix,first,last,suffix],' ') as title
from names

