-- 고객 ID와 거래 없이 방문한 횟수를 조회
SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans

-- Visits 테이블에서 데이터를 가져오고, 테이블에 별칭 v를 부여
FROM Visits v

-- Transactions 테이블과 LEFT JOIN을 수행하여 visit_id가 일치하는 행을 결합, Transactions 테이블에 별칭 t를 부여
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id

-- 거래가 없는 방문(Transactions 테이블에 일치하는 거래가 없는 경우)을 필터링
WHERE t.transaction_id IS NULL

-- 고객별로 데이터를 그룹화하여, 각 고객의 거래 없는 방문 횟수를 집계
GROUP BY v.customer_id;
