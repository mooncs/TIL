# pjt01



### 프로젝트 목표

- Python 기본 문법 실습
- 파일 입출력에 대한 이해
- 데이터 구조에 대한 분석과 이해
- 데이터를 가공하고 JSON 형태로 저장





### 1. problem_a [&#128190;](./problem_a.py)

> **A. 제공되는 영화 데이터의 주요내용 수집**
>
> - 원하는 정보를 추출하여 새로운 dictionary 반환하기

`문제 풀이 방법`

1.  json형태의 파일을 열고, 예쁘게 출력해주는 open(), load(), pprint() 함수는 주어져 있기 때문에, 
2.  가져온 딕셔너리에서 필요한 정보를 추출하고,
3.  새로운 딕셔너리에 값을 추가한다. 

```
# movie.get('id')와 같은 형식을 통해 필요한 정보를 추출한다.
def movie_info(movie):
	id = movie.get('id')
```

```
# 새로운 딕셔너리 result를 만들고, 추출한 정보를 바탕으로 key와 value값을 넣어준다.
def movie_info(movie):    
    result = {
        'id' : movie.get('id'),
        'title' : movie.get('title')
        }
```





### 2. problem_b [&#128190;](./problem_b.py)



> **B. 제공되는 영화 데이터의 주요내용 수정**
>
> - 특정 정보를 찾아, 새로운 정보로 업데이트 하기

`문제 풀이 방법`

1.  problem_a와 달리 두 가지의 json파일을 사용해 정보를 불러온다.
2.  두 가지 파일에서 동일한 장르 id를 가진 정보를 찾고
3.  새로운 딕셔리에 장르 id 대신에 장르 name을 넣고 딕셔너리를 반환한다.

```
# movie.get('genre_ids')를 이용해서 movie.json에서 장르 id를 가져온다.
genre_ids = movie.get('genre_ids')
```



```
# 장르 name을 담을 빈 리스트를 정의
genre_names = []
# 장르 id의 길이가 다 다르므로, 장르 id의 길이만큼 반복할 반복문 작성
for i in range(len(genre_ids)):
	# genres.json에 있는 정보를 불러와서
	for genre in genres:
		# movie.json의 장르 id와 genres.json의 장르 id을 비교
		if genre_ids[i] == genre.get('id'):
			# id가 동일하면 해당 장르의 name을 리스트에 담는다.
			genre_names.append(genre.get('name'))
```



```
# problem_a와 동일하게 새로운 딕셔너리를 반환하는데, genre_ids 대신에 genre_names값을 추가한다.
result = {
        'genre_names' : genre_names
    }
```





### 3. problem_c [&#128190;](./problem_c.py)

> **C. 다중 데이터 분석 및 수정**
>
> - problem_b를 활용하여, 다양한 데이터에서 특정 정보를 찾아 새로운 정보로 업데이트 하기

`문제 풀이 방법`

1.  여러 가지 영화 정보를 가지고 problem_b와 같은 과정을 반복한다.

```
# 먼저 새로운 영화 정보 딕셔너리들을 담을 빈 리스트를 정의한다.
movies_info = []
```



```
# movies.json 안에 있는 영화의 갯수만큼 반복
for movie in movies:
	# 장르 id를 받아오고
	genre_ids = movie.get('genre_ids')
	# 장르 id 갯수만큼 반복문 수행
    for i in range(len(genre_ids)):
    	# problem_b와 다르게 리스트 내포를 활용한 코드 작성
    	genre_names = [genre.get('name') for genre in genres if genre_ids[i] == genre.get('id')]
```



```
# append 함수를 통해 새로운 정보를 가진 영화 딕셔너리 result를 리스트에 추가한다.
movies_info.append(result)
```





### 4. problem_d [&#128190;](./problem_d.py)

> **D. 알고리즘을 통한 데이터 출력**
>
> - 특정 json 파일을 열어 원하는 정보를 추출하고 정보의 대소를 비교하기

`문제 풀이 방법`

1.  movies 폴더 안에 있는 json 파일들을 불러와야 하기에, f-strinf과 open(), load() 함수를 활용한다.
2.  비교한 revenue와 영화title을 담을 리스트를 정의하고
3.  revenue를 비교하여 제일 큰 revenue를 가진, 영화의 title을 리스트에 담아 출력한다.

```
for movie in movies:
	# movies폴더의 json파일명이 movie_id와 같기 때문에 id를 불러온다.
	movie_id = movie.get('id')
	# 불러온 movie_id를 적절한 위치에 f-string을 통해 위치시키고, 해당 파일을 연다.
	m_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
	# m_info를 통해 json파일의 정보를 읽어온다.
	m_info = json.load(m_json)
```



```
# 영화 이름을 넣을 revenue[0]='', revenue를 넣을 revenue[1]=0으로 세팅
revenue = ['', 0]
```



```
# revenue를 비교하여 리스트에 있는 revenue보다 크다면 해당 영화의 title과 revenue를 리스트에 갱신한다.
if m_info.get('revenue') > revenue[1]:
            revenue[0] = m_info.get('title')
            revenue[1] = m_info.get('revenue')
```



```
# 제일 revenue가 큰 영화의 title을 반환
return revenue[0]
```





### 5. problem_e [&#128190;](./problem_e.py)

> **E. 알고리즘을 통한 데이터 출력**
>
> - 특정 json 파일을 열어 원하는 정보를 추출하고 특정 정보를 가진 데이터 반환하기

`문제 풀이 방법`

1.  problem_d와 같은 과정을 통해 movies 폴더 안에 있는 json 파일들을 불러온다.
2.  문자열이 12와 같은지 비교를 하고, 같은 정보를 가진 영화의 정보를 빈 리스트에 담아 반환한다.

```
# 문자열 인덱싱을 통해 비교
if m_info.get('release_date')[5:7] == '12' :
	m_same_month.append(m_info.get('title'))
	
# 문자열 split을 통해 비교
if m_info.get('release_date').split('-')[1] == '12' :
	m_same_month.append(m_info.get('title'))
```



```
def dec_movies(movies):
    m_same_month = []
    for movie in movies:
        movie_id = movie.get('id')
        m_json = open(f'data/movies/{movie_id}.json', encoding='UTF8')
        m_info = json.load(m_json)
        if m_info.get('release_date').split('-')[1] == '12' :
            m_same_month.append(m_info.get('title'))
            
    return m_same_month
```

