-- 1. TABLE 이름 변경
-- ALTER TABLE table_name RENAME To new_name;
ALTER TABLE articles RENAME To news;

-- 2. 테이블에 새로운 column 추가
-- ALTER TABLE table_name ADD COLUMN column_name data_type;
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
-- 기존의 데이터에는 없는 columns이기 때문에 error발생
-- 해결 1. NOT NULL 설정 없이 추가하기
ALTER TABLE news ADD COLUMN created_at TEXT;
-- 해결 2. 기본 값(DEFAULT) 설정하기
ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL DEFAULT '소제목';

-- 3. column 이름 수정
-- ALTER TABLE table_name RENAME COLUMN current_name TO new_name;
ALTER TABLE news RENAME COLUMN created_at TO subtitle;