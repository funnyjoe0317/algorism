-- 각 기계의 ID와 평균 처리 시간을 구하는 쿼리입니다.
SELECT new_activity.machine_id, 
       -- 각 기계에서 프로세스별로 걸린 시간을 평균 내고, 그 결과를 소수점 셋째 자리까지 반올림합니다.
       ROUND(AVG(end_time - start_time)::numeric, 3) AS processing_time

-- 서브쿼리에서 계산된 데이터를 가져옵니다. 서브쿼리에서는 각 프로세스의 시작 및 종료 시간을 추출합니다.
FROM (
    -- 각 기계(machine_id)와 프로세스(process_id) 별로 그룹화하여, 해당 프로세스의 시작 및 종료 시간을 계산하는 서브쿼리
    SELECT
        machine_id, 
        process_id, 
        -- 활동 유형이 'end'인 경우, 해당 프로세스의 종료 시간을 추출합니다.
        MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time,
        -- 활동 유형이 'start'인 경우, 해당 프로세스의 시작 시간을 추출합니다.
        MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time
    -- Activity 테이블에서 데이터를 가져옵니다.
    FROM Activity 
    -- 각 기계와 프로세스별로 그룹화하여 시작 시간과 종료 시간을 계산합니다.
    GROUP BY machine_id, process_id
) AS new_activity
-- 기계별로 그룹화하여 평균 처리 시간을 구합니다.
GROUP BY new_activity.machine_id;
