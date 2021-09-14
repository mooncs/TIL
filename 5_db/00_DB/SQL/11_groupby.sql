-- users에서 각 성(last_name)씨가 몇 명씩 있는지 조회
SELECT last_name, COUNT(*) FROM users
GROUP BY last_name;