-- https://www.codewars.com/kata/sql-basics-create-a-function/train/sql
-- My solution
create function increment(in int, out int) as
    $$ select $1 + 1 $$
    language sql;

-- Other ways
CREATE FUNCTION increment(i integer) RETURNS integer
  AS 'select $1 + 1;'
  LANGUAGE sql;

CREATE OR REPLACE FUNCTION increment(i integer) RETURNS integer
  AS $$ BEGIN RETURN i + 1; END; $$
  LANGUAGE plpgsql;

create function increment(integer) returns integer
  as 'select $1 + 1;'
  language sql
  immutable
  returns null on null input;

create function increment(in int, out int) as
    $$ select $1 + 1 $$
    language sql;