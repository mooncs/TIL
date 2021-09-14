-- 전체 조회
SELECT * FROM classmates;

-- 컬럼 지정 조회
SELECT rowid, name FROM classmates;

-- 개수 제한, linit
SELECT id, name FROM classmates LIMIT 2;

-- OFFSET 같이 사용 가능, OFFSET뒤 자료부터 가져온다.
SELECT id, name FROM classmates LIMIT 2 OFFSET 2;

-- 데이터베이스에 존재하는 도시의 이름을 중복 없이 가져와
SELECT DISTINCT address
from classmates;

--  users 테이블에서 age가 30 이상인 유저의 모든 컬럼 정보를 조회
SELECT * FROM users
WHERE age >= 30;

--  users 테이블에서 age가 30 이상이고 성이 ‘김’인 사람의 나이와 성만 조회
SELECT age, last_name FROM users
WHERE age >= 30 AND last_name='김';