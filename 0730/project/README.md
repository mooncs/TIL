# pjt02



### 프로젝트 목표

- Python 기본 문법 실습
- 데이터 구조에 대한 분석과 이해
- 요청과 응답에 대한 이해
- API의 활용과 문서 분석





### 1. problem_a [&#128190;](./problem_a.py)

> **A. 영화 개수 카운트 기능 구현**
>
> - popular를 기준으로 가져온 영화 목록의 개수를 출력합니다.

`문제 풀이 방법`

1.   tmbd.py에서 TMDBHelper import하기
2.   TMDBHelper 인스턴스를 생성하고
3.   원하는 url을 가져온다.
4.   해당 url의 정보를 가져와서, 필요한 부분을 사용한다.

```
# requests와 TMDBHelper를 사용할 것이므로 import를 하고 시작한다.
import requests
from tmdb import TMDBHelper
```



```
# TMDBHelper class 인스턴스 생성
# key값을 별도로 넣지 않으면, default값인 None이 들어가기 때문에 개인의 key값을 넣어준다.
    tmdb_helper = TMDBHelper(api_key)
```



```
# 원하는 url을 가져오기 위해 인스턴스 메서드인 get_request_url이용
# method의 default값이 '/movie/popular'이기 때문에, 추가적인 language='ko', region='KR'만 입력
url = tmdb_helper.get_request_url(language='ko', region='KR')
```



```
# 완성된 url을 가지고 필요한 정보를 불러오고, 
# 불러온 정보의 형태가 궁금하다면 print하거나 url에 들어가서 형태를 확인하고 사용
data = requests.get(url)
popular_data = data.json()
# pprint(popular_data)		# pprint를 사용하려면 from pprint import pprint 적용
```



```
# 최종적으로 인기작의 갯수가 몇 개인지를 반환한다.
return len(popular_data['results'])
```





### 2. problem_b [&#128190;](./problem_b.py)

> **B. 특정 조건에 맞는 영화 출력**
>
> - popular를 기준으로 가져온 영화 목록 중 평점이 8 이상인 영화들의 목록을 출력합니다.

`문제 풀이 방법`

1.   problem_a와 동일하게 '/movie/popular'형태의 url을 get_request_url통해 가져온다.
2.   추천작 영화 전체의 정보를 변수로 정의
3.   빈리스트와 반복문을 활용하여, 조건을 총족시키는 영화의 정보를 빈리스트에 추가한다. 

```
# 인기작 영화 전체의 정보를 popular_lst로 정의
popular_lst = popular_data.get('results')
```



```
# 필요한 정보를 찾기 위해 빈리스트와 반복문 활용
vote_average = []
for i in range(len(popular_lst)):
```



```
# 추천작의 평점이 8점 이상인 영화의 정보를 결과 리스트에 추가
if popular_lst[i].get('vote_average') >= 8:
	result.append(popular_lst[i])
```





### 3. problem_c [&#128190;](./problem_c.py)

> **C. 평점 순 정렬**
>
> - 영화목록을 평점순으로 출력하는 함수를 완성합니다.

`문제 풀이 방법`

1.   problem_b와 동일하게 인기영화의 정보를 가져온다.
2.   가져온 리스트를 sorted()와 itemgetter를 통해 평점순으로 정렬한다.
3.   정렬된 리스트에서 처음부터 5번째까지의 영화 정보를 반환한다.

```
# 가져온 리스트 형태의 데이터를 sorted()와 itemgetter 통해 평점순으로 정렬한다.
new_pop_lst = sorted(popular_lst, key=itemgetter('vote_average'), reverse=True)
# from operator import itemgetter 적용
```



```
# 정렬된 리스트에서 처음부터 5번째까지의 영화 정보를 반환한다.
    return new_pop_lst[:5]
```





### operator.itemgetter, 다중 수준 정렬

operator.itemgetter는 주로 sorted 함수의 key 매개변수에 적용되어 다중 수준의 정렬을 가능하게 해주는 모듈이다.

> sorted( 리스트변수명, key=itemgetter(정렬기준) )

위와 같은 형태로 사용이 가능하다.





### 4. problem_d [&#128190;](./problem_d.py)

> **D. 제목 검색, 영화 추천**
>
> - 제공된 영화 제목을 기준으로 추천영화 목록을 출력합니다.

`문제 풀이 방법`

1.   추천작을 검색하는 url을 완성하기 위해서는 영화의 id가 필요하다.
2.   get_movie_id를 이용하여 영화의 id를 우선적으로 가져온다.
3.   영화의 id가 None이면 None을 반환
4.   영화의 id가 있으면 get_request_url와 f-string을 활용하여 url을 가져온다.
5.   추천작의 영화 제목을 담을 빈리스트를 생성하고, 반복문을 통해 추천작의 정보를 모아서 반환한다.

```
tmdb_helper = TMDBHelper('83b326269660ac3171fddfc110d21cc7')
# 추천작을 검색하는 url을 사용하기 위해서는 영화의 id가 필요하다.
# get_movie_id를 이용하여 영화의 id를 우선적으로 가져온다.
movie_title = tmdb_helper.get_movie_id(title)
```



```
# 영화의 id가 None이면 None을 반환
if movie_title == None:
	return movie_title
```



```
# 영화의 id가 있으면 get_request_url와 f-string을 활용하여 url을 가져온다.
else:
	url = tmdb_helper.get_request_url(f'/movie/{movie_title}/recommendations', language='ko')
```



```
# 추천작의 영화 제목을 담을 빈리스트를 생성하고, 반복문을 통해 추천작의 정보를 모아서 반환한다.
reco_title = []
for i in range( len(reco_lst) ):
	reco_title.append( reco_lst[i].get('title') )
	
return reco_title
```





### 5. problem_e [&#128190;](./problem_e.py)

> **E. 배우, 제작진 리스트 출력**
>
> - 영화에 출연한 배우들과 제작진의 정보가 저장된 딕셔너리를 출력합니다.

`문제 풀이 방법`

1.   배우와 제작진의 정보를 불러오는 url을 완성하기 위해서는 영화의 id가 필요하다.
2.   problem_d와 같은 과정을 통해 영화의 id를 우선적으로 가져온다.
3.   마찬가지로 영화의 id가 None이면 None을 반환
4.   영화의 id가 있으면 get_request_url와 f-string을 활용하여 url을 가져온다.
5.   데이터의 형태를 잘 확인하고 필요한 정보를 가져온다.
6.   조건에 맞는 배우와 제작진을 담을 빈리스트와 최종결과를 담을 빈 딕셔너리를 생성하고, 
7.   반복문을 통해 해당 정보를 모아서 반환한다.

```
# 영화의 id가 있으면 get_request_url와 f-string을 활용하여 url을 가져온다.
else:
	url = tmdb_helper.get_request_url(f'/movie/{movie_title}/credits')
```



```
# 데이터의 형태를 잘 확인하고 필요한 정보를 가져온다.
# 이전까지는 'results'를 통해 영화 정보에 접근했지만, 배우의 정보는 'cast'에 제작진의 정보는 'crew'를 통해 접근가능하다.
cast_lst = credit_data.get('cast')
crew_lst = credit_data.get('crew')
```



```
# 조건에 맞는 배우와 제작진을 담을 빈리스트와 최종결과를 담을 빈 딕셔너리를 생성하고, 
# 반복문을 통해 해당 정보를 모아서 반환한다.
act = []
direct = []
result = {}
```



```
# 배우 목록에서 cast_id 값이 10보다 작은 배우의 이름을 리스트에 저장
for i in range(len(cast_lst)):
	if cast_lst[i].get('cast_id') < 10:
		act.append(cast_lst[i].get('name'))
```



```
# 제작진 목록에서 department 값이 Directing인 감독의 이름을 리스트에 저장
for i in range(len(crew_lst)):
	if crew_lst[i].get('department') == 'Directing':
		direct.append(crew_lst[i].get('name'))
```



```
# cast와 crew를 key로 가지고, 각각 배우 리스트와 제작진 리스트를 value값으로 가지는 딕셔너리 생성 및 반환
result['cast'] = act
result['crew'] = direct

return result
```

