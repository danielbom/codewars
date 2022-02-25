-- https://www.codewars.com/kata/sql-with-street-fighter-total-wins/train/sql
-- My solution
select name, sum(won) as won, sum(lost) as lost
from fighters
where move_id not in (
  select id
  from winning_moves
  where move like 'Hadoken' or
    move like 'Shouoken' or
    move like 'Kikoken'
)
group by name
order by sum(won) desc
limit 6;

-- ...
SELECT name, sum(won) as won, sum(lost) as lost FROM fighters
INNER JOIN winning_moves ON fighters.move_id=winning_moves.id
WHERE NOT move IN ('Hadoken', 'Shouoken', 'Kikoken')
GROUP BY name
ORDER by won DESC
LIMIT 6;

-- ...
SELECT  name, sum(won) as won, sum(lost) as lost 
FROM Fighters f 
INNER JOIN winning_moves w ON f.move_id = w.id
WHERE w.move NOT IN ('Hadoken', 'Shouoken','Kikoken')
GROUP BY name
ORDER BY won DESC
FETCH FIRST 6 ROWS ONLY;