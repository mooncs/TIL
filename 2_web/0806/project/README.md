# pjt03



## 프로젝트 목표

- HTML을 통한 웹 페이지 마크업 분석
- CSS 라이브러리의 이해와 활용
- 컴포넌트 및 그리스 시스템 활용
- 커뮤니티 서비스 반응형 레이아웃 구성



## 개발도구

1. Visual Studio Code
2. Google Chrome Browser
3. Bootstrap v5



## A. 01_nav_footer

1. 네비게이션 바(Navigation Bar) [&#128525;](https://getbootstrap.com/docs/5.1/components/navbar/) Bootstrap> Components > Nav 활용

   1. 네비게이션 바는 스크롤을 하더라도 항상 상단에 고정되어 있습니다.

   - `class="sticky-top"` 활용

   2. 로고 이미지는 images 폴더 안의 logo.png파일을 사용합니다.

   - `img src="images/logo.png"`

   3. 로고 이미지는 클릭이 가능한 링크이며, 해당 페이지(02_home.html)로 이동해야 합니다.

   - `a href="02_home.html"`

   4. 네비게이션 바 내부의 네비게이션 리스트(Home, Community, Login)는 오른쪽에 배치합니다.

   - 992px을 기준으로 네비게이션 바 형태가 변형하기 때문에 01_nav_footer.css에 `media query`사용

   ```css
   @media (min-width: 992px) {
     #navbarNav {
       display: flex;
       justify-content: flex-end;
     }  
   }
   ```

   - 768px 기준으로 수정

   ```css
   @media (min-width: 768px) {
     #navbarNav {
       display: flex;
       justify-content: flex-end;
     }  
   }
   ```

   

   5. 네비게이션 리스트의 각 항목들은 클릭이 가능한 링크이며, 해당 페이지로 이동해야 합니다.

   - 3번과 동일하게 수행, img태그 대신 a태그 활용

   6. Viewport의 가로 크기가 768px 미만일 경우에는 네비게이션 리스트(Home, Community, Login)가 햄버거 버튼으로 교체되며, 클릭했을 시 세부 항목을 볼 수 있습니다.

   - 992px을 기준으로 수행해서, 추후 변경 예정...

   7. 네비게이션 리스트(Home, Community, Login)의 항목들 중에서 Home을 강조합니다.

   - `class="active"`활용

   8. 네비게이션 리스트의 Login 항목은 클릭 시 요소가 Modal 컴포넌트를 통하여 나타납니다.

   -  [&#128525;](https://getbootstrap.com/docs/5.1/components/modal/) Bootstrap> Components > Modal 활용
   - fixed-top과 sticky-top과 함께 쓰면 비활성화 되므로 nav바깥에 정의

   9. Modal 컴포넌트에서 form요소 내부의 비밀번호는 표시되지 않습니다.

   - \<form>을 이용하여 로그인 내용을 작성하고, 비밀번호의 경우 `input type="password"`를 통해 표시되지 않도록 한다.

2. 푸터(Footer)

   1. 푸터는 스크롤을 하더라도 항상 하단에 고정되어 있습니다

   - `class="fixed-bottom"`활용

   2. 푸터에 작성된 내용은 수평으로 정렬되어 있습니다. (왼쪽, 오른쪽 여백이 같습니다.)

   - `class="d-flex justify-content-center align-items-center"`활용

   

### 소감

> 우선적으로 우측 정렬에 있어서 많은 시간을 소비하였다.
>
> 모달과 sticky-top과 동시 사용이 불가능하다는 것을 알게 되었고, README를 쓰다가 768px 기준임을 알게 되었다...
>
> -> 수정완료





## B. 02_home

1. Header

   1. Header는 Carousel 컴포넌트로 구성합니다. 이미지는 최소 3장이며, 자동으로 전환됩니다.

   -  [&#128525;](https://getbootstrap.com/docs/5.1/components/carousel/) Bootstrap> Components > Carousel 활용

2. Section

   1. Section 내부의 개별 요소(article)들은 이미지, 제목, 설명을 포함하는 Card 컴포넌트로 구성합니다.

   -  [&#128525;](https://getbootstrap.com/docs/5.1/components/card/) Bootstrap> Components > Cards 활용

   2. 각 요소들은 좌우 일정한 간격으로 떨어져 있습니다. 
   3. Section 내부의 요소(article)들은 Viewport의 가로 크기가 576px미만일 경우에는 한 열(row)에 1개씩 표시됩니다.
   4. Section 내부의 요소(article)들은 Viewport의 가로 크기가 576px이상일 경우에는 한 열(row)에 2개 이상 자유롭게 표시합니다.

   - `class="row row-cols-1 row-cols-sm-3 g-4"` 활용

   

### 소감

> A 문제에 비해서는 살짝 편하게 푼 느낌...? 대부분 Bootstrap사이트 참조 및 활용을 해서 편한 문제였다...?





## C. 03_community

1. 게시판 목록

   1. 게시판 목록 내부의 각 항목들(Boxoffice, Movies, Genres, Actors)은 List group 컴포넌트를 활용합니다.

   -  [&#128525;](https://getbootstrap.com/docs/5.1/components/list-group/) Bootstrap> Components > List group활용

   2. 게시판 목록 내부의 각 항목들은 클릭이 가능한 링크이며, 모두 동작은 하지 않습니다.

   - `<a href="#" class="list-group-item list-group-item-action" style="color: blue;"></a>` 활용

   3. Viewport의 가로 크기가 992px 이상일 경우에는 게시판 목록 내부의 항목들(Boxoffice, Movies, Genres, Actors)은 div.main영역의 내부에서 좌측1/6 만큼의 너비를 가집니다.
   4. Viewport의 가로 크기가 992px 미만일 경우에는 게시판 목록 내부의 항목들(Boxoffice, Movies, Genres, Actors)은 div.main영역의 내부에서 전체만큼의 너비를 가집니다.

   - `<aside class="col-12 col-lg-2 mt-3">`를 활용하여 992px(lg) 기준으로 차이가 생기게 하였다.

2. 게시판

   1. 게시판은 Viewport의 가로크기에 따라 전혀 다른 요소를 표시합니다.
   2. Viewport의 가로 크기가 992px 이상일 경우에는 게시글들이 표(table)요소로 표시되며, div.main영역의 내부에서 우측 5/6 만큼의 너비를 가집니다.
   3. Viewport의 가로 크기가 992px 미만일 경우에는 게시글들이 글(article)요소들의 집합으로 표시되고 가로선으로 구분합니다. div.main영역의 내부에서 전체만큼의 너비를 가집니다.

   - `<section class="col-12 col-lg-10">`를 활용하여 992px(lg) 기준으로 차이가 생기게 하였다.
   - 03_community.css에 `media query`사용하여 992px 기준으로 다른 요소를 표시하도록 하였다.

   ```css
   @media (max-width: 992px) {
     table {
       display:none;
     }
   }
   @media (min-width: 992px) {
     article {
       display:none;
     }  
   }
   ```

   4. 게시판 탐색기(paginator)는 게시판 아래에 위치하며, 게시판과 같은 가로폭을 가집니다.

   -  [&#128525;](https://getbootstrap.com/docs/5.1/components/pagination/) Bootstrap> Components > Pagination활용

   5. 게시판 탐색기(paginator)는 자신의 영역 안에서 좌우 중앙 정렬되어 있습니다.

   - `<ul class="pagination justify-content-center offset-4 col-4">` 활용

   6. 게시판 탐색기(paginator) 내부의 요소들은 클릭이 가능한 링크이며, 모두 동작은 하지 않습니다.

   - `<a class="page-link" href="#"></a>`활용

   

### 소감

> 처음에 크기별로 다른 요소를 보여야 한다는 점에서 멘붕이 왔지만 어찌저찌 해결을 하였고,
>
> 그 외로 위치 및 정렬을 하는 것과 내용을 구성하는데 있어서도 생각보다 어려웠다.



## 총평

웹을 다배웠다하기에는 아직 턱 없이 부족하다라는 것을 깨닫는 계기가 되었습니다...ㅎ