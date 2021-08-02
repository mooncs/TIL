# CSS

Cascading System Sheets

### 왜 css를 배우는가?

- 스타일, 레이아웃 등을 통해 문서(HTMl)를 표시하는 방법을 지정하는 언어



### CSS 구문

```css
h1{
    color: blue;
    font-size: 15px;
}
```

- 선택자(Selector)
  - h1
- 선언(Declaration), 속성과 값의 쌍
  - color: blue
- 속성(Property)
  - font-size
- 값(Value)
  - 15px



- CSS 구문은 선택자와 함께 열린다.
- 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에은 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미한다.
  - 속성(Property) : 어떤 스타일 기능을 변경할지 결정
  - 값(Value) : 어떻게 스타일 기능을 변경할지 결정



### CSS 정의 방법

> **인라인, inline**

```css
<h1 style="color: blue; font-size: 100px;">Hello</h1>
```

- 해당 태그에 직접 `style`속성을 활용



> **내부 참조, embedding**

```css
<style>
	h1 {
        color: blue;
        font-size: 15px;
	}
</style>
```

- 해당 태그에 내에 `style`속성을 활용



> **외부 참조, link file**

```css
<head>
	<link rel="stylesheet" href="mtstyle.css">
</head>
```

- 외부 CSS 파일을 \<head>내 \<link>를 통해 불러오기



### CSS Selectors

> **선택자(Selectors)**

- HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요하다.

- 기본 선택자

  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자

- 결합자(Combinators)

  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자

- 의사 클래스/요소(pseudo class)

  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자




```css
<body>
	<h1 class="green">SSAFY</h1>
	<h2>선택자 연습</h2>
	<div>
		<p>지역 목록</p>
		<ul>
			<li>서울</li>
			<li id="purple">인천</li>
			<li>강원</li>
			<li>경기</li>
		</ul>
	</div>
	<h3>HELLO</h3>
	<h4>CSS</h4>
</body>
```



```css
<style>
	/* 전체 선택자*/
	* {
    	color:red;
	}

	/* 요소 선택자*/
	h2 {
     	color:orange;
	}

	h3,
	h4 {
    	font-size: 10px;
	}
</style>
```



```css
<style>
	/* class 선택자*/
	.green {
	 	color:green;
	}
	
	/* id 선택자*/
	#purple {
	 	color:purple;
	}
	
	/* 자식 결합자*/
	.box > p {
	 	font-size: 30px;
	}
	
	/* 자손 결합자*/
	.box p {
	 	color:blue;
	}
</style>
```



> **CSS 선택자 정리**

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스(class) 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 모든 항목을 선택
- 아이디(id) 선택자
  - \# 문자로 시작하며, 해당 아이디가 적용된 모든 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용(unique)
  - 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장



> **CSS 적용 우선순위 (cascading order)**

- CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다.

  1. 중요도(Importance)
     - !important
  2.  우선순위(Specificity)
     - 인라인 > id 선택자 > class 선택자, 속성 선택자, pseudo-class > 요소선택자, pseudo-element
  3.  소스 순서

  ​	

> **QUIZ**

```css
<p>1</p>
<p class="blue">2</p>
<p class="blue green">3</p>
<p class="green blue">4</p>
<p id="red" class="blue">5</p>
<h2 id="red" class="blue">5</h2>
<p id="red" class="blue" style="color: yellow;">7</p>
<h2 id="red" class="blue" style="color: yellow;">8</h2>
```

```css
h2 {
	color: darkviolet !important;
}

p {
	color: orange;
}

.blue {
	color: blue;
}

.green {
	color: green;
}

#red {
	color: red;
}
```



> **CSS 상속**

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  - 상속 되는 것 예시
    - Text 관련요소(font, color, text-align), opacity, visibility 등
  - 상속 되지 않는 것 예시
    - Box model 관련요소(width, height, margin, padding, border, box-sizing, display), 
    - position 관련요소(position, top/right/bottom/left, z-index) 등
    - https://developer.mozilla.org/ko/docs/Web/CSS/inheritance

```css
<body>
	<p>안녕하세요<span>김주훈</span>입니다.</p>
</body>
```

```css
<style>
	p{
        /* 상속됨*/
        color: red;
        /* 상속안됨*/
        border: 1px solid black;
	}
	span{
        border: 1px solid blue;
	}
</style>
```



### CSS 단위

> **크기 단위**

- px(픽셀)
  - 모니터 해상도의 한 화소인 '픽셀'을 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
  - 각각 모니터에 따라 다르다.
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위,, 부모 요소에 대한)상속의 영향을 받는다.
  - 배수 단위, 요소에 지정된 사이즈에 **`상대적인 사이즈`**를 가진다.
  - 10px, 2em  ->  20px
- rem
  - (바로 위,, 부모 요소에 대한)상속의 영향을 받지 않는다.
  - **`최상위 요소(html)의 사이즈`**를 기준으로 배수 단위를 가진다.
- viewport
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역
  - 주로 스마트폰이나 테블릿 디바이스의 화변을 일컫는 용어로 사용된다.
  - 글자 그대로 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정된다.
  - vw(width), vh(height), vmin, vmax

```html
<body>
    <ul class="em">
        <li class="em">1.5em</li>
        <li class="rem">1.5rem</li>
        <li>no class</li>
    </ul>
</body>
 /* html사이즈는 16 */
```

```html
<style>
    .em {
        font-size: 1.5em;
    }
    
    .rem {
        font-size: 1.5em;
    }
</style>
```

```html
<body>
    <ul class="em">
        <li class="em">1.5em</li>
         /* em -> 16x1.5x1.5=36px */
        <li class="rem">1.5rem</li>
         /* rem -> 16x1.5=24px */
        <li>no class</li>
         /* 부모클래스만 적용-> 16x1.5=24px */
    </ul>
</body>
 /* html사이즈는 16 */
```



> **색상 단위**

1. 색상 키워드
   - 대소문자를 구분하지 않는다.
   - red, blue, black과 같은 특정 색을 직접 글자로 나타낸다.
2.  RGB 색상
   - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현
   - '#' + 16진수 표기법
   - rgb() 함수형 표기법
3.  HSL 색상
   - 색상, 채도, 명도를 통해 특정 색을 표현

```html
 /* 모두 검정 */
p { color: black; }
p { color: #000; }
p { color: #000000; }
p { color: rgb(0, 0, 0); }
p { color: hsl(120, 100%, 0); }
```



### Selectors 심화

> **결합자 (Combinators)**

- 자손 결합자
  - selectorA 하위의 모든 selectorB 요소

```html
div span {
	color: red,
}
```

```html
<div>
    <span>이건 빨강입니다!</span>
    <p>이건 빨강이 아닙니다.</p>
    <p>
    	<span>이건 빨강입니다!</span>    
    </p>
</div>
```



- 자식 결합자
  - selectorA 바로 아래 selectorB 요소

```html
div > span {
	color: red,
}
```

```html
<div>
    <span>이건 빨강입니다!</span>
    <p>이건 빨강이 아닙니다.</p>
    <p>
    	<span>이건 빨강이 아닙니다.</span>    
    </p>
</div>
```



- 일반 형제 결합자
  - selectorA 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택

```html
p ~ span {
	color: red,
}
```

```html
<div>
    <span>p태그 앞에 있기 때문에 이건 빨강이 아닙니다.</span>
    <p>여기 문단이 있습니다.</p>
    <b>그리고 코드도 있습니다.</b>
    <span>p태그와 형제이기 때문에 이건 빨강입니다!</span>
    <b>더 많은 코드가 있습니다.</b>
    <span>이것도 p태그와 형제이기 때문에 빨강입니다!</span>
</div>
```



- 인접 형제 결합자
  - selectorA 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

```html
p + span {
	color: red,
}
```

```html
<div>
    <span>p태그 앞에 있기 때문에 이건 빨강이 아닙니다.</span>
    <p>여기 문단이 있습니다.</p>
    <span>p태그와 인접한 형제이기 때문에 이건 빨강입니다!</span>
    <b>그리고 코드가 있습니다.</b>
    <span>p태그와 인접한 형제가 아니기 때문에 이건 빨강이 아닙니다.</span>
</div>
```

