# **2차원 배열**

## 2차원 배열의 선언

- 1차원 List를 묶어놓은 List
- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언
- 2차원 List의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 한다.
- Python에서는 데이터 초기화를 통해 변수선언과 초기화가 가능하다.

```python
N, M = map(int, input().split())
arr = [ list(map(int, input().split())) for _ in range(N) ]

arr2 = [ [0] * M for _ in range(N) ]
# arr2 =[[0]*M]*N	# 이것은 사용 불가!!!
```

```python
arr2 = [[0]*M]*N
arr2[0][1] = 10
# -> 결과가 [[0, 10, 0], [0, 10, 0]]
```

# **2차원 배열의 접근**

## 배열 순회

- n x m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법

- 행 우선 순회

```python
# i행의 좌표
# j열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[i])):
        Array[i][j]		# 필요한 연산 수행
```

- 열 우선 순회

```python
# i행의 좌표
# j열의 좌표
for j in range(len(Array[0])):
    for i in range(len(Array)):
        Array[i][j]		# 필요한 연산 수행
```

- 지그재그 순회

```python
# i행의 좌표
# j열의 좌표
for i in range(len(Array)):
    for j in range(len(Array[0])):
        Array[i][j + (m-1-2*j) * (i%2)]		# 필요한 연산 수행
        # 홀수이면 i%2가 1이되어서 m-1-2j가 살아남고 앞의 j를 더하면 최종적으로 m-1-j
        # 짝수이면 i%2가 0이 되어서 그냥 j
```

```python
for i in range(N):
    if i%2 ==0:
        for j in range(M-1):
    else:
        for j in range(M-1, 0, -1):
```

- 델타를 이용한 2차 배열 탐색

  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법

  ```python
  arr[0...n-1][0...n-1]
  dx[] <- [0, 0, -1, 1] 	# 상하좌우
  dy[] <- [-1, 1, 0, 0]
  
  for x in range(len(arr)):
      for y in range(len(arr[x])):
          for i in range(4):
              testX <- x + dx[mode]
              testY <- y + dy[mode]
              test(arr[testX][testY])
  ```

  |              |   i-1, j+0   |              |
  | :----------: | :----------: | :----------: |
  | **i+0, j-1** |  **(i, j)**  | **i+0, j+1** |
  |              | **i+1, j+0** |              |

  ```python
  di[] <- [0, 1, 0, -1]		# 우하좌상
  dj[] <- [1, 0, -1, 0]
  
  N, M = map(int, input().split())
  arr = [ list(map(int, input().split())) for _ in range(N) ]
  
  for i in range(N):
      for j in range(M):
          for k in range(4):
              ni = i + di[k]
              nj = j + dj[k]
              # 영역을 벗어나지 않는다면,
              if 0 <= ni < N and 0 <= nj < M: 
  	            arr[ni][nj]
                  
  for i in range(N):
      for j in range(M):
          for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
              ni = i + dr
              nj = j + dc
              # 영역을 벗어나지 않는다면,
              if 0 <= ni < N and 0 <= nj < M: 
  	            arr[ni][nj]
  ```

# **2차원 배열의 활용**

- 전치 행렬

```python
# i행의 좌표, len(arr)
# j열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]]		# 3*3행렬

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

# **부분집합**

## 부분집합 합 문제

- 유한 개의 정수로 이루어진 집합이 있을때, 이 집합의 부분집합 중에서 그 집ㅎ바의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제
- 예를 들어, [-7, -3, -2, 5, 8]이라는 집합이 있을 때, [-3, -2, 5]는 이 집합의 부분 집합이면서 (-3)+(-2)+5=0이므로 이 경우의 답은 참이 된다.
- 완전검색 기법으로 부분집합 합 문제를 풀기 위해서는, 우선 집합의 모든 부분집합을 생성한 후에 각 부분집합의 합을 계산해야 한다.



## 부분집합의 수

- 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2ⁿ개이다.
- 이는 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 같다.

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i					# 0번째 원소
    for j in range(2):
        bit[1] = j				# 1번째 원소
        for k in range(2):
            bit[2] = k			# 2번째 원소
            for l in range(2):
                bit[3] = l		# 3번째 원소
                print(bit)		# 생성된 부분집합 출력
```

- 실습

  ```python
  arr = [1, 2, 3, 4]
  bit = [0, 0, 0, 0]
  for i in range(2):
      bit[0] = i					# 0번째 원소
      for j in range(2):
          bit[1] = j				# 1번째 원소
          for k in range(2):
              bit[2] = k			# 2번째 원소
              for l in range(2):
                  bit[3] = l		# 3번째 원소
                  print(bit, end=' ')
                  for p in range(4):
                      if bit[p]:
                          print(arr[p], end=' ')
                  print()
  ```

# **비트연산자**

## 비트연산자

- `&` 비트 단위로 AND 연산을 한다.
- `|` 비트 단위로 OR 연산을 한다.
- `<<` 피연산자의 비트 열을 왼쪽으로 이동시킨다.
- `>>` 피연산자의 비트 열을 오른쪽으로 이동시킨다.

|      |  &   |  \|  |  ^   |
| :--: | :--: | :--: | :--: |
| 0 0  |  0   |  0   |  0   |
| 0 1  |  0   |  1   |  1   |
| 1 0  |  0   |  1   |  1   |
| 1 1  |  1   |  1   |  0   |



## << 연산자

- 1 << n : 2ⁿ 즉, 원소가 n개일 경우의 모든 부분집합의 수를 의미한다. n번 비트가 1인 값



## & 연산자

- i & (1 << j) : i의 j번째 비트가 1인지 아닌지를 리턴한다. 

> 보다 간결하게 부분집합을 생성하는 방법

```python
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)	# n : 원소의 개수

for i in range(1<<n):		# 1<<n : 부분 집합의 개수
    for j in range(n):	# 원소의 수만큼 비트를 비교한다. 비트의 값을 검사
        if i & (1<<j):		# 비트가 1인지 0인지 검사하는 방법, i의 j번째 비트가 1이면 j번째 원소를 출력
            print(arr[j], end=', ')
    print()
print()
```

```python
# i & (1<<j)
#    10110
#  & 00010		 # 1<<1, 1(j)번 비트가 1인 값
-----------
#    00010		 # j번 비트가 1인 값
# if 00000		 # j번 비트가 0인 값
```



# **검색(Search)**

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
  - 탐색 키(search key) : 자료를 구별하여 인식할 수 있는 키
- 검색의 종류
  - 순차 검색(seauential search)
  - 이진 검색(binary search)
  - 해쉬(hash)



## 순차검색

- 일렬로 되어 있는 자료를 순서대로 검색하는 방법

  - 가장 간단하고 직관적인 방법
  - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목을 찾을 때 유용하다.
  - 알고리즘이 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우에는 수행시간이 급격히 증가하여 비효율적이다.

- 2가지 경우

  - 정렬되어 있는 경우

    - 자료가 오름차순으로 정렬된 상태에서 검색을 실시한다고 가정
    - 자료를 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색 대상의 키 값보다 크면 찾는 원소가 없다는 것이므로 더 이상 검색하지 않고 검색을 종료한다.
    - 정렬이 되어있으므로, 검색 실패를 반환하는 경우 평균 비교 회수가 반으로 줄어든다.

    ```python
    def search(A, N, key):
        for i in range(N-1):
            if A[i] == key:
                return i
            elif A[i] > key:
                return -1
    	return -1
    ```

    ```python
    def search(A, N, key):
        i = 0
        while i < N and A[i] < key:
            i += 1
    	if i < N and A[i] = key:
            return i
        else:
            return -1
    ```

    

  - 정렬되어 있지 않은 경우

    - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는 비교하며 찾는다.
    - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
    - 자료구조의 마지막에 이를 때까지 검색 대상을 찾지 못하면 검색 실패

    ```python
    def search(A, N, key):
        for i in range(N-1):
            if A[i] == key:
                return True
        return False
    ```

    ```python
    def search(A, N, key):
        i = 0
        # index 오류가 올 수 있기 때문에, while a[i] != key and i < n 처럼 코드를 짜면 안된다.
        # 앞 쪽부터 차례로 진행되기 때문에
        while i < n and A[i] != key:
            i += 1
       	if i < N:
            return i
        else:
            return -1
    ```



## 이진 검색

- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법

  - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행한다.

- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 한다.

- 검색과정

  - 자료의 중앙에 있는 원소를 고른다.
  - 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다.
  - 목표 값이 중앙 원소의 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색을 수행하고, 크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
  - 찾고자 하는 값을 찾을 때까지 앞의 과정을 반복

  ```python
  def binarySearch(a, key):
      start = 0
      end = len(a)-1
      while start <= end:
          middle = (start + end) // 2
          if a[middle] == key:	# 검색 성공
              return True
          elif a[middle] > key:
              end = middle - 1
          else:
              start = middle + 1
      return False	# 검색 실패
  ```

  ```python
  def binarySearch(a, start, end, key):
      if start > end:	# 검색 실패
          return False
      else:
          middle = (start + end) // 2
          if a[middle] == key:	# 검색 성공
              return True
          elif a[middle] > key:
              return binarySearch(a, start, middle - 1, key)
          else:
              return binarySearch(a, middle + 1, end, key)
  ```

# **인덱스**

- 인덱스라는 용어는 Database에서 유래했으며, 테이블에 대한 동작 속도를 높여주는 자료 구조를 일컫는다. Database 분야가 아닌 곳에소는 Look up table등의 용어를 사용하기도 한다.
- 인덱스를 저장하는데 필요한 디스크 공간은 보통 테이블을 저장하는데 필요한 디스크 공간보다 작다. 왜냐하면 보통 인덱스는 키-필드만 갖고 있고, 테이블의 다른 세부 항목들은 갖고 있지 않기 때문이다.
- 배열을 사용한 인덱스
  - 대량의 데이터를 매번 정렬하면, 프로그램의 반응은 느려질 수 밖에 없다. 이러한 대량 데이터의 성능 저하 문제를 해결하기 위해 배열 인덱스를 사용할 수 있다.

# **선택정렬(Selection Sort)**

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식
  - 앞서 살펴본 셀렉션 알고리즘을 전체 자료에 적용한 것이다.
- 정렬과정
  - 주어진 리스트 중에서 최소값을 찾는다.
  - 그 값을 리스트의 맨 앞에 위치한 값과 교환한다.
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위 과정을 반복한다.
- 시간복잡도
  - O(n²)

```python
# 최소값을 찾는 법
min_idx = 0
for i in range(1, N-1):
    if arr[i] < arr[min_idx]:
        min_idx = i
```

```python
# 구간의 시작이 변한다.
def selection_sort(arr, n):
    for i in range(0, N-1):		 # 작업 구간의 시작 i
        min_idx = i				# 맨 앞을 제일 작은 것이라 가정
        for j in range(i+1, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
```

## 버블 정렬

```python
# 구간의 끝이 변한다.
for i in range(N-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
```

# **셀렉션 알고리즘(Selection Algorithm)**

- 저장되어 있는 자료로부터 k번째로 큰/작은 원소를 찾는 방법을 셀렉션 알고리즘이라고 한다.
  - 최소값, 최대값 혹은 중간값을 찾는 알고리즘을 의미하기도 한다.
- 선택 과정
  - 정렬 알고리즘을 이용하여 자료 정렬하기
  - 원하는 순서에 있는 원소 가져오기
- k번째로 작은 원소를 찾는 알고리즘
  - 1번부터 k번까지 작은 원소들을 찾아 배열의 앞쪽으로 이동시키고, 배열의 k번째를 반환한다.
  - k가 비교적 작을 때 유용하며, O(kn)의 수행시간을 필요로 한다.

```python
def selection(list, k):
    for i in range(0, k):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list[k-1]
```



