-- 검색 조건 : 주소가 부산
SELECT rowid, *
FROM classmates
WHERE address='부산';

-- 검색 조건 : 나이가 30 이상
SELECT name
FROM classmates
WHERE age >= 30;

-- 검색 조건 : 주소가 부산이면서 나이가 30 이상
SELECT name
FROM classmates
WHERE address='부산' AND age >= 30;