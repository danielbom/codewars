-- https://www.codewars.com/kata/sql-basics-create-a-function-dates/train/sql
-- My solution
create function agecalculator(born date) returns integer as $$
  begin
    return date_part('year', age(born));
  end;
$$ language plpgsql;

-- Dentzil, guliing, almugu24
create function agecalculator (date) returns integer
as 'select EXTRACT(year from age($1))::integer;'
language sql;

