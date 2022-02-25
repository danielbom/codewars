-- https://www.codewars.com/kata/sql-basics-simple-having/train/sql
-- My solution
select age, count(age) as total_people
from people
group by age
having count(age) >= 10
