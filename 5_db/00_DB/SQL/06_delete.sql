-- 조건이 없으면 table의 모든 데이터가 삭제된다.
DELETE FROM classmates;

DELETE FROM classmates
WHERE rowid=1;

-- 조건에 맞는 모든 데이터가 삭제된다.
DELETE FROM classmates
WHERE address='광주';
