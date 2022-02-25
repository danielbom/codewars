-- https://www.codewars.com/kata/best-selling-books-sql-for-beginners-number-5/train/sql
-- My solution
select *
from books
order by copies_sold desc
fetch first 5 rows only

-- ...
SELECT name, author, copies_sold
FROM books
ORDER BY copies_sold DESC 
LIMIT 5