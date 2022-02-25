-- https://www.codewars.com/kata/easy-sql-cube-root-and-natural-log/train/sql
-- My solution
select cbrt(number1) as cuberoot,
  ln(number2) as logarithm
from decimals

-- ...
/*  SQL  */
select power(number1, (1/3.0)) as cuberoot, ln(number2) as logarithm
from decimals

-- ...
select ||/number1 as cuberoot, ln(number2) as logarithm
from decimals
