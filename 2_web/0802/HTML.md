# Web

### 왜 web을 배우는가?

- 웹 어플리케이션 개발을 하기 위해서

- SW 개발 방법 및 학습 과정을 익히기 위해서(SW 개발의 기반이 되는 web)



### 웹 표준

**`W3C`**

> World Wide Web 협회
>
> HTML5

**`WHATWG`**

> HTML Living Standard
>
> (Apple, Goolge, Microsoft, Mozilla) -> 고유 브라우저를 가지고 있다.



# HTML

- Hyper Text Markup Language
- 웹 페이지를 작성하기 위한(구조를 잡기 위한) 언어, **`웹 컨텐츠의 의미와 구조를 정의`**

> **`Hyper Text` Markup Language**

- Hyper
  - 텍스트 등의 정보가 동일 선상에 있는 것이 아니라 **`다중으로 연결`**되어 있는 상태

- Htper Text

  - 참조(하이퍼링크)를 통해 사용자가 **`한 문서에서 다른 문서로 접근`**할 수 있는 텍스트

  - http/html

    

> **Hyper Text `Markup` Language**

```html
<h1>HTML</h1>

	<p>...</p>

<h2>Hyper Text</h2>

	<p>...</p>
```

- **`역할`**, **`의미`**를 부여



> **Hyper Text Markup `Language`**

- 태그 등을 이용하여 문서나 데이터의 **`구조`**를 명시하는 언어
- 프로그래밍 언어와는 다르게 단순하게 **`데이터를 표현하기만`** 한다.
  - 저장, 조건, 반복 불가



# HTML 기본구조

```html
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
    
</body>
</html>
	
```

>  **head 요소**

- 문서 제목, 문자코드(인코딩)와 같이 **`해당 문서의 정보`**를 담고 있으며,
- 브라우저에 나타나지 않는다.
- 메타데이터 : 데이터에 대한 데이터



> **body 요소**

- 브라우저 화면에 나타나는 정보로 실제 내용에 해당한다.



> **DOM(Document Object Model) 트리**

- 부모, 형제 관계

```html
<body>
	<h1> 웹 문서 </h1>
	<ul>
		<li>HTML</li>
		<li>CSS</li>
	</ul>
</body>
```

- DOM은 문서의 구조화된 표현(Structured Representation)을 제공하며,
- 프로그래밍 언어가 DOM구조에 접근할 수 있는 방법을 제공하여 그들이 문서 구조, 스타일 내용 들을 변경할 수 있게 도움을 준다.
- DOM은 동일한 문서를 표현하고, 정장하고, 조작하는 방법을 제공
- **`Web Page의 객체 지향 표현`**



> **요소(element)**

- HTML의 요소는 태그와 내용으로 구성되어 있다.

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그(Element, 요소)는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
- 내용이 없는 태그들
  - br, hr, img, input, link, meta
- **`요소는 중첩(nested)될 수 있음`**
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야한다.
  - **`오류를 반환하는 것이 아니라`** 그냥 레이아웃이 깨진 상태로 출력되기 떄문에, 디버깅이 힘들어 질 수 있다.



> **속성(attribute)**

```html
<a herf="https://google.com"></a>
```

- 속성명, 속성값
- 태그별로 사용할 수 있는 속성은 다르다.
- 공백은 No!!!, ""(쌍따옴표) 사용!!!
  - 필수적인 것은 아니지만, 이렇게 사용하도록 하자!!!
- 속성을 통해 태그의 부가적인 정보를 설정할 수 있다.
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 **`하나의 쌍으로`** 존재(아닌것들고 있다.)
- **`태그와 상관없이 사용 가능한 속성`**(HTML Global Attribute)들도 있다.



> **HTML Global Attribute**

- 모든 HTML 요소가 공통으로 사용할 수 있는 속성**`(몇몇 요소에는 아무 효과가 없을 수 있다.)`**
  - id, class
  - hidden
  - lang
  - style
  - tanbindex
  - title

- <https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes>



```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Hello, HTML</title>
</head>
<body>
    <!-- 이것은 주석입니다. -->
    <h1>
        My first HTML
    </h1>
    <p>
        This is main contents.
    </p>
    <span>This is inline elements</span>
    <a href="https://google.com">Go google!!</a>
</body>
</html>
	
```



> **시맨틱 태그**

- HTML5에서 의미론적 요소를 담은 태그의 등장 (원래는 `div`의 역할)

- 대표적인 태그들은 다음과 같다.

  - header : 문서 전체나 섹션의 헤더(머릿말 부분)
  - nav : 내비게이션
  - aside : 사이드에 위치한 공간, 메인 컨텐츠와 관련성이 적은 컨텐츠
  - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer : 문서 전체나 섹션의 푸터(마지막 부분)

- 컨텐츠의 의미를 명확하게 전달해준다.

  - 읽기가 쉬워지고, 접근성이 좋아진다.

    

- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐만 아니라 **`의미`**를 가지는 태그들을 활용하기 위한 노력
- Non semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있다.
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 해준다.
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 할 필요가 있다.



> **시맨틱 웹**

- 웹 상에 존재하는 수많은 웹 페이지들에 메타데이터를 부여하여,
- 기존의 단순한 데이터 집합이었던 웹페이지를 **`'의미'`**와 **`'관련성'`**을 가지는 거대한 데이터베이스로 구축하고자 하는 발상에서 시작
- 안 지켜도 에러가 나는 것은 아니지만, 적절하게 잘 사용을 하는 것이 유용



# HTML 문서 구조화

> **인라인/블록 요소**

- 인라인 요소
  - 자기 데이터 요소만큼만 차지
- 블록 요소
  - 한 칸을 다 차지



> **그룹 컨텐츠**

- \<p>
  -  문단
- \<hr>
  - 헤드라인
- \<ol>, \<ul>
  - order list, unorder list
- \<pre>, \<blockquote>
  - 주석, 인용문
- \<div>



> **텍스트 관련 요소**

- \<a>
  -  하이퍼 텍스트, 링크
- \<b> vs \<strong>
  - 텍스트를 굵게, 둘 다 출력은 동일
  - b는 표현상으로(그냥) 굵게, strong은 강조!!  ->  **`웹 접근성`**(시각, 이동성, 청각, 인지)
- \<i> vs \<em>
  - 텍스트를 기울게, 둘 다 출력은 동일
- \<span>, \<br>, \<img>
  - span, div와 역할은 동일(div는 블록, span은 인라인)
  - br, 다음 줄로 넘어가도록
  - img, 이미지 태그



> **table**

- \<tr>, \<td>, \<th>

- \<thead>, \<tbody>, \<tfoot>

- \<caption>
- 셀 병합 속성 : colspan, rowspan
- scope 속성
- \<col>, \<colgroup>



> **form**

- \<form>은 서버에서 처리될 데이터를 제공하는 역할
- \<form>의 기본 속성
  - action, 데이터를 어디로 보낼지
  - method, 어떤 http method를 선택할지



> **input**

- 다양한 타입을 가지는 입력 데이터 필드 (사용자 입력 부분)
- \<label> : 서식 입력 요소의 캡션
- \<input> 공통 속성
  - name, placholder
  - required
  - autofocus
- \<input> 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지해야 한다.
  - <https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input



> 마크업 해보기

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
    <header>
    	<a href="https://coronaboard.kr/">
        <img src="covid.jpg" alt="main img" width="300">
      </a>
    	<h1>학생 건강 설문></h1>
    </header>
    <section>
    	<form action="#">
        	<div>
                <label for="name">이름을 기재해주세요.</label><br>
                <input type="text" id="name" name="name" autofocus>
                <!-- autofocus, 입력이 바로 가능하도록 커서를 입력창 선택상태로 -->
            </div>
            <hr>
            
            <div>
                <label for="region">지역을 선택해주세요.</label><br>
                <select name="region" id="region" required>
                <!-- required, 필수적으로 선택 -->
                    <option value="">선택</option>
                    <option value="서울">서울</option>
                    <option value="대전">대전</option>
                    <option value="광주" disabled>광주</option>
                    <option value="구미" disabled>구미</option>
                    <option value="부산">부산</option>
                    <!-- disabled, 비활성화 -->
                </select>
            </div>
            <hr>
            
            <div>
                <p>오늘의 체온을 선택해주세요.</p>
                <input type="radio" id="normal" name="body-heat" value="normal" checked>
                <!-- checked, 기본적으로 check해두겠다. -->
                <!-- radio는 하나만 체크, checkbox는 여러개 선택 가능 -->
                <label for="normal">37도 미만</label><br>
                <input type="radio" id="warning" name="body-heat" value="warning">
                <label for="warning">37도 이상</label>
            </div>
            <hr>
            
            <input type="submit" value="제출">
            <!-- submit, 서버로 데이터를 제출 -->
        </form>
    </section>
    <footer>
        Google 설문지를 통해 비밀번호를 제출하지 마시오.
    </footer>
</body>

</html>	
```
