-- https://www.codewars.com/kata/sql-regex-replace/train/sql
-- My solution
select project, commits, contributors, regexp_replace(address, '\d', '!', 'g') as address
from repositories

-- ...
select r.project,
       r.commits,
       r.contributors,
       regexp_replace(r.address , '\d','!','g') as address
  from repositories r
 -- order by 4

-- ...
SELECT project, commits, contributors,
  REGEXP_REPLACE(address, '[[:digit:]]', '!', 'g') AS address
FROM repositories
