-- 매니저들의 ID, 이름, 보고받는 직원 수, 직원들의 평균 나이를 계산하여 출력하는 쿼리

SELECT 
    e1.employee_id,  -- 매니저의 ID
    e1.name,         -- 매니저의 이름
    COUNT(e2.employee_id) AS reports_count,  -- 매니저가 직접 보고받는 직원 수를 계산
    ROUND(AVG(e2.age)) AS average_age        -- 매니저가 보고받는 직원들의 나이 평균을 반올림
FROM 
    Employees e1    -- e1은 매니저를 나타냄
JOIN 
    Employees e2    -- e2는 매니저에게 보고하는 직원들을 나타냄
ON 
    e1.employee_id = e2.reports_to  -- e1의 employee_id와 e2의 reports_to가 일치하면 매니저와 직원의 관계
GROUP BY 
    e1.employee_id,  -- 매니저별로 그룹화
    e1.name          -- 매니저의 이름으로도 그룹화
ORDER BY 
    e1.employee_id DESC;  -- 매니저의 employee_id 기준으로 내림차순 정렬 (큰 값부터 작은 값으로)
