-- COUNT
-- users 테이블의 레코드 총 개수 조회
SELECT COUNT(*) FROM users;

SELECT COUNT(*) AS '총원' FROM users;

-- AVG, SUM, MIN, MAX
-- 해당 column이 INTEGER일 때만 사용 가능
-- 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users
WHERE age >= 30;

-- 계좌 잔액(balance)이 가장 높은 사람과 그 액수를 조회
SELECT first_name, MAX(balance) FROM users;
-- 계좌 잔액이 가장 많은 사람 전부 불러오기
SELECT * FROM users
WHERE balance = 1000000;

--  나이가 30 이상인 사람의 계좌 평균 잔액을 조회
SELECT AVG(balance) FROM users
WHERE age >= 30;

-- AVG, SUM, MIN, MAX
SELECT AVG(balance), COUNT(*), SUM(balance), MAX(balance), MIN(balance) FROM users;