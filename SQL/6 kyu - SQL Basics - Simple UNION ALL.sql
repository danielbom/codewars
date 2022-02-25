-- https://www.codewars.com/kata/sql-basics-simple-union-all/train/sql
-- My solution
select 'US' as location, *
  from ussales
  where price > 50
union all
select 'EU' as location, *
  from eusales
  where price > 50
  order by location desc

