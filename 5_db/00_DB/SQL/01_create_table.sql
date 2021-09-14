CREATE TABLE classmates (
id INTEGER PRIMARY KEY, 
name TEXT
);

CREATE TABLE classmates (
name TEXT,
age INTEGER, 
address TEXT
);

-- SQLite는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면,
-- 값이 자동으로 증가하는 PK 옵션을 가진 rowid 컬럼을 정의

CREATE TABLE classmates (
id INTEGER PRIMARY KEY, 
name TEXT NOT NULL,
age INTEGER NOT NULL,
address TEXT NOT NULL
);


CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

-- title과 content라는 컬럼을 가진 articles라는 이름의 table 생성
CREATE TABLE articles (
title TEXT NOT NULL,
content TEXT NOT NULL
);