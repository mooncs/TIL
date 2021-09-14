--  users 테이블에서 나이가 20대인 사람만 조회
SELECT * FROM users WHERE age LIKE '2_';
SELECT * FROM users WHERE age>=20 AND age<30;
SELECT COUNT(*) FROM users WHERE age LIKE '2_';

-- users 테이블에서 지역 번호가 02인 사람만 조회
SELECT * FROM users WHERE phone LIKE '02-%';

--  users 테이블에서 성은 '박' 이름이 ‘준’으로 끝나는 사람만 조회
SELECT * FROM users WHERE first_name LIKE '%준' AND last_name='박';

--  users 테이블에서 중간 번호가 5114인 사람만 조회
SELECT * FROM users WHERE phone LIKE '%-5114-%';