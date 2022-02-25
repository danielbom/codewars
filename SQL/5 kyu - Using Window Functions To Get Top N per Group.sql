-- https://www.codewars.com/kata/using-window-functions-to-get-top-n-per-group/train/sql
-- Copy from and my solution https://github.com/wenima/codewars/blob/master/kyu5/sql/src/top_n_per_group_window.sql

with posts_per_category as (
  select c.id as category_id,
    c.category,
    p.title,
    p.views,
    p.id as post_id,
    rank() over (
      partition by p.category_id
      order by p.views desc, p.id
    ) as rnk
  from categories c left join posts p on c.id = category_id
)

select category_id, category, title, views, post_id
from posts_per_category
where rnk <= 2
order by category, views desc, post_id;