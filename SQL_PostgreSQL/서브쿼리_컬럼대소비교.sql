-- 최종적으로 id 값을 반환하는 구문입니다.
SELECT id

-- 서브쿼리로부터 데이터를 가져옵니다. 서브쿼리에서는 이전 행의 온도와 날짜를 계산합니다.
FROM (
    -- Weather 테이블에서 id, temperature, 그리고 recordDate를 가져옵니다.
    SELECT id, temperature, recordDate,
           -- LAG 함수: 이전 행의 temperature 값을 가져옵니다 (recordDate를 기준으로 정렬).
           LAG(temperature, 1) OVER (ORDER BY recordDate) AS pre_temp,
           -- LAG 함수: 이전 행의 recordDate 값을 가져옵니다 (recordDate를 기준으로 정렬).
           LAG(recordDate, 1) OVER (ORDER BY recordDate) AS pre_day
    FROM Weather -- Weather 테이블에서 데이터를 가져옵니다.
) lag_temp -- 서브쿼리 결과에 lag_temp라는 별칭을 부여합니다.

-- 조건문: 현재 행의 temperature가 이전 행의 temperature보다 큰 경우를 선택합니다.
WHERE lag_temp.temperature > lag_temp.pre_temp
    -- 조건문: 이전 날짜가 현재 날짜보다 1일 전인지 확인합니다.
    AND lag_temp.pre_day = lag_temp.recordDate - INTERVAL '1 day';
