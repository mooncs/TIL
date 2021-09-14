-- default는 ASC
-- users 에서 나이 순으로 오름차순 정렬하여 상위 10개만 조회
SELECT * FROM users
ORDER BY age ASC LIMIT 10;

-- 나이 순, 성 순으로 오름차순 정렬하여 상위 10개만 조회
SELECT * FROM users ORDER BY age, last_name LIMIT 10;

-- 계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회
SELECT last_name, first_name FROM users
ORDER BY balance DESC LIMIT 10;