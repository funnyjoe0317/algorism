-- Write your PostgreSQL query statement below
select distinct author_id AS id
-- 중복된 author_id를 제거하고, 결과 열 이름을 id로 지정합니다.
from Views

where author_id = viewer_id
-- 저자가 자신의 글을 본 경우만 선택합니다.
ORDER BY author_id asc;
-- 결과를 author_id를 기준으로 오름차순으로 정렬합니다
-- ORDER BY: 결과를 특정 기준에 따라 정렬할 때 사용하는 구문입니다.

--------------------------------------------------------------
select name, area, population
from World
where area >= 3000000 or population >=25000000;
-----------------------------------------------------
-- Write your PostgreSQL query statement below
select name
from Customer

where  referee_id != 2 or referee_id is null;
---------------------------------------------