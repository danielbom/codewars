-- https://www.codewars.com/kata/easy-sql-bit-length/train/sql
-- My solution
select id,
  bit_length(name) as name,
  birthday,
  bit_length(race) as race
from demographics

-- ...
/*  SQL  */
SELECT id, 
  octet_length(name)*8 AS name, 
  birthday, 
  octet_length(race)*8 AS race
FROM demographics;