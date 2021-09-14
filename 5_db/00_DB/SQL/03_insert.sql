INSERT INTO classmates(name, age)
VALUES('이지은', 29);

INSERT INTO classmates(name, age, address)
VALUES('아이유', 29, '서울특별시');

-- 모든 것을 다 쓰려면 굳이 column명을 명시하지 않아도 된다.
INSERT INTO classmates
VALUES('이지은', 29, '서울특별시');

INSERT INTO classmates
VALUES(1, '이지은', 29, '서울특별시');

INSERT INTO classmates(name, age, address)
VALUES('강동옥', 28, '부산광역시');

-- 여러개를 한 번에 추가할 수 있다.
INSERT INTO classmates VALUES
('짱구', 5, '떡잎마을'),
('철수', 5, '떡잎마을'),
('훈이', 5, '떡잎마을'),
('유리', 5, '떡잎마을'),
('맹구', 5, '떡잎마을');

--  articles 테이블에 값을 추가 (title은 ‘1번제목’, content는 ‘1번내용’)
INSERT INTO articles VALUES('1번제목', '1번내용');

insert into classmates(address, age, name) values('서울', 20, '홍길동');