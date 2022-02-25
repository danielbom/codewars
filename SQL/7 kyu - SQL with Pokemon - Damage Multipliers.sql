-- https://www.codewars.com/kata/sql-with-pokemon-damage-multipliers/train/sql
-- My solution
select p.pokemon_name as pokemon_name,
  m.multiplier * p.str as modifiedStrength,
  m.element
from pokemon p join multipliers m on (p.element_id = m.id)
where m.multiplier * p.str >= 40
order by m.multiplier * p.str desc;
