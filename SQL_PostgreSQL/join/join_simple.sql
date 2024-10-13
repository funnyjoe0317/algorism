-- Write your PostgreSQL query statement below
select e.name, u.unique_id
from Employees e

left join EmployeeUNI u
-- 이거를 사용하면 없는것들이 null로 알아서 뽑힘
on e.id = u.id