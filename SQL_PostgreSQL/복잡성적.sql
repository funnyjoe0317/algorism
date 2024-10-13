-- 학생이 각 과목에서 시험에 몇 번 응시했는지를 구하는 쿼리입니다.
SELECT 
    s.student_id,                    -- 학생의 ID
    s.student_name,                  -- 학생의 이름
    sub.subject_name,                -- 과목 이름
    COUNT(e.student_id) AS attended_exams  -- 해당 학생이 해당 과목에서 응시한 시험 횟수를 계산합니다.
                                          -- 시험에 응시하지 않았으면 0이 됩니다.

-- Students 테이블과 Subjects 테이블의 모든 조합을 생성하기 위해 Cross join을 사용합니다.
FROM Students s
CROSS JOIN Subjects sub

-- Students 테이블과 Subjects 테이블의 조합에 대해, Examinations 테이블을 left join 합니다.
-- 이를 통해 각 학생이 각 과목에서 시험을 봤는지 확인합니다.
LEFT JOIN Examinations e
ON s.student_id = e.student_id       -- 학생 ID가 일치해야 하며
AND sub.subject_name = e.subject_name  -- 과목 이름도 일치해야 합니다. 이 조건이 모두 맞으면 시험 기록이 있는 것으로 간주됩니다.

-- 학생, 학생 이름, 그리고 과목 이름에 따라 데이터를 그룹화합니다.
GROUP BY 
    s.student_id,                    -- 학생별로 그룹화
    s.student_name,                  -- 각 학생의 이름도 그룹화 (student_id와 이름이 함께 묶여야 함)
    sub.subject_name                 -- 과목별로 그룹화

-- 결과를 학생 ID와 과목 이름에 따라 정렬합니다.
ORDER BY 
    s.student_id,                    -- 학생 ID 기준으로 먼저 정렬
    sub.subject_name;                -- 그 다음 과목 이름 기준으로 정렬
