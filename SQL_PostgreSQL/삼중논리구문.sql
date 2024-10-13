-- Write your PostgreSQL query statement below
select t.x, t.y, t.z, 
    case
        when x+y > z and z+x >y and z+y > x then 'Yes'
        ELSE 'No'
    end as triangle

from Triangle t

Triangle =
| x  | y  | z  |
| -- | -- | -- |
| 13 | 15 | 30 |
| 10 | 20 | 15 |