-- Write your PostgreSQL query statement below
--   descending order -> 내림차순 ODD 짝수, 
select id, movie, description, rating
from cinema

where id % 2 != 0 AND description != 'boring'
order by rating DEsc;