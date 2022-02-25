-- https://www.codewars.com/kata/sql-right-and-left/train/sql
-- My solution
select left(project, commits) as project,
  right(address, contributors) as address
from repositories

-- ...
SELECT SUBSTRING(project, 0, commits+1) AS project
    ,SUBSTRING(address, LENGTH(address) - contributors + 1) AS address
  FROM repositories
  