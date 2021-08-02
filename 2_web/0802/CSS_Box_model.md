### CSS Box model

> **네모 세상**

- 모든 HTML 요소는 box 형태로 되어있다.
- 하나의 박스는 네 부분의 영역으로 이루어져 있다.
  - content
  - padding
  - border
  - margin



> **Margin**

- 테두리 바깥의 외부 여백
- 배경색을 지정할 수 없다.

```htm
.margin{
	margin-top: 10px;
	margin-right: 20px;
	margin-bottom: 30px;
	margin-left: 40px;
}

.margin-1{
	margin:10px;
	/* 상하좌우 모두 10px */
}

.margin-2{
	margin:10px20px;
	/* 상하 / 좌우 */
}

.margin-3{
	margin:10px20px30px;
	/* 상 / 좌우 / 하 */
}

.margin-4{
	margin:10px20px30px40px;
	/* 상 / 우 / 하 / 좌 */
}
```



> **Border**

- 테두리 영역

```
.border{
	border-width:2px;
	border-style:dashed;
	border-color:black;
}

.border{
	border:2pxdashedblack;
	/* 순서 상관없다. */
}
```



> **Padding**

- 테두리 안쪽의 내부 여백
- 요소에 적용된 배경색
- 이미지는 padding까지 적용

```
.margin-padding{
	margin:10px;
	/* 상하좌우 모두 10px */
	padding:30px;
}
```



> **Content**

- 글이나 이미지 등 요소의 실제 내용



> **박스 실습**

```html
<body>
    <div class="box1">div</div>
    <div class="box2">div</div>
</body>
```

```html
<style>
    .box1{
        width: 500px;
        border-width: 2px;
		border-style:dashed;
		border-color:black;
        padding-left: 50px;
		margin-bottom: 30px;
    }
    
    .box2{
        width: 500px;
        border: 2px soild black;
        padding: 20px 30px;
        margin: 0 auto;
    }
</style>
```



```html
<body>
    <div class="box">content-box</div>
    <div class="box box-sizing">border-box</div>
</body>
```

```html
<style>
    .box{
        width: 100px;
        margin: 10px auto;
        padding: 20px;
        border: 1px soild black;
        color: white;
        text-align: centet;
        background-color: blueviolet;
    }
    
    .box-sizing{
        box-sizing{
            box-sizing: border-box;
            margin-top: 50px;
        }
    }
</style>
```



> **Box-sizing**

- 기본적으로 모든 요소의 `box-sizing`은 `content-box`
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 `box-sizing`을 `border-box`로 설정



> **Box model**

- 마진 상쇄
  - block A의 top과 block B의 bottom에 적용된 각각의 margin이 둘 중에서 큰 마진 값으로 결합(겹쳐지게)되는 현상



## CSS Display

> **Display**

- display : block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있다.

- display : inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다.



> **블록 레벨 요소와 인라인 레벨 요소**

- 블록 레벨 요소와 인라인 레벨 요소 구분 (HTML 4.1까지)
- 대표적인 블록 레벨 요소( https://developer.mozilla.org/ko/docs/Web/HTML/Block-level_elements )
  - div / ul, ol, li / p / hr / form 등
- 대표적인 인라인 레벨 요소( https://developer.mozilla.org/ko/docs/Web/HTML/Inline_elements )
  - span / a / img / input, label / b, em, i, strong 등



> **속성에 따른 수평 정렬**

- margin-right: auto;	text-align: left;
- margin-left: auto;	text-align: right;
- margin-right: auto; margin-left: auto;	text-align: center;



> Display

- display: inline-block
  - block과 inline 레벨 요소의 특징을 모두 갖는다.
  - inline처럼 한 줄에 표시 가능하며,
  - block처럼 width, height, margin 속성을 모두 지정할 수 있다.

- display: none
  - 해당 요소를 화면에 표시하지 않는다. (공간조차 사라진다.)
  - 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.
- 이외 다양한 display 속성은 https://developer.mozilla.org/ko/docs/Web/CSS/display 에서 확인

```html
<body>
    <h1>나는 block입니다</h1>
    <div>block</div>
    <p>나는 <span>인라인</span>속성입니다.</p>
    <hr>
    <h2>display none vs viisibility hidden</h2>
    <div>1</div>
    <div class="none">2</div>
    <div class="hidden">3</div>
    <div>4</div>
</body>
```

```html
<style>
	div {
	width: 100px;
	height: 100px;
	border: 2px solid black;
	background-color: crimson;
	}
</style>
```



## CSS Position

> CSS position

- 문서 상에서 요소를 배치하는 방법을 지정한다.
- `static` : 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따른다.(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치된다.
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동이 가능하다.(음수 값도 가능)
  - relative
  - absolute
  - fixed

> **static**

```html
div {
	height: 100px;
	width: 100px;
	background-color: #9775fa;
	color: black;
	line-height: 100px;
	text-align: center;
}
```





> **relative**

- relative : 상대 위치
  - 자기 자신의 static 위치를 기준으로 이동
  - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같다.

```html
.relative {
	position: relative;
	top: 100px;
	left: 100px;
}
```



> **absolute**

- absolute : 절대 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않는다.
  - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없는 경우 body에 붙는 형태)

```html
.parent {
	position: relative;
}

.absolute-child {
	position: absolute;
	top: 50px;
	left: 50px;
}
```



> **fixed**

- fixed : 고정 위치
  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않는다.
  - 부모요소와 관계없이 viewpoint를 기준으로 이동
  - 스크롤 시에도 항상 같은 곳에 위치한다.

```html
.fixed {
	position: fixed;
	bottom: 0;
	right: 0;
}
```



> **absolute vs relative**

```html
<body>
    <div class="parent">
        <div class="absolute">형</div>
        <div class="sibling">동생</div>
    </div>
    <hr>
    <div class="parent">
        <div class="relative">형</div>
        <div class="sibling">동생</div>
    </div>
</body>
```

```html
<style>
	/* 공통 스타일링 */
    div {
        box-sizing: border-box;
        width: 100px;
        height: 100px;
        border: 1px solid black;
    }
    
    .parent {
        position: relative;
        width: 300px;
        height: 300px;
    }
</style>
```

```html
<style>
	/* 차이점 확인해보기 */
    .absolute{
        position: absolute;
        top: 100px;
        left: 100px;
        background-color: crimson;
    }
    
    .sibling{
        background-color: deepskyblue;
    }
    
    .relative {
        position: relative;
        top: 100px;
        left: 100px;
        background-color: crimson;
    }
</style>
```



> **absolute의 특징**

- 원래 위치해 있었던 과거 위치에 있던 공간은 더 이상 존재하지 않는다.
- 즉, 다른 모든 것과 별개로 독자적인 곳에 놓인다.
- 페이지의 다른 요소의 위치와 간섭하지 않는 격리된 사용자 인터페이스 기능을 만드는데 활용
  - 팝업 정보 상자, 제어 메뉴, 롤오버 패널, 페이지 어느 곳에서나 끌어서 놓기 할 수 있는 유저 인터페이스 페이지 등



## 학습 가이드라인

- MDN web docs
  - https://developer.mozilla.org/ko/



> **Emmet**

- HTML & CSS를 작성할 때 보다 빠른 마크업을 위해서 사용되는 오픈소스

- 단축키, 약어 등을 사용

- 대부분의 텍스트 에디터에서 지원

  https://emmet.io/

  https://docs.emmet.io/cheat-sheet/



## 마무리

- 웹과 브라우저의 변화, 그리고 표준
- HTML 기본 구조
  - 요소, 태그, DOM트리
- HTML 다양한 태그들
  - 그룹, 텍스트 관련 요소
  - \<table>, \<form> 등
- HTML은 보이는 것 이상의 의미를 가지기도 한다.
  - 메타태그, 시멘틱태그 등을 통한 SEO
  - 웹 접근성

