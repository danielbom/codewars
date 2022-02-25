-- https://www.codewars.com/kata/sql-basics-simple-null-handling/train/sql
-- My solution
select id,
  coalesce(nullif(name, ''), '[product name not found]') as name,
  price,
  coalesce(nullif(card_name, ''), '[card name not found]') as card_name,
  card_number,
  transaction_date
from eusales
where price > 50
