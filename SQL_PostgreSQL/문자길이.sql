-- Write your PostgreSQL query statement below
select tweet_id
from Tweets

WHERE LENGTH(content) > 15;