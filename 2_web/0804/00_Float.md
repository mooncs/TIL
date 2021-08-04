## CSS Layout

> **CSS page layout technniques**

- Display
- Position
- Float
- Flexbox
- Grid system
- Table layout
- Multiple-column layout



## Float

- 한 요소(element)가 정상 흐름(normal flow)으로부터 빠져 **`텍스트 및 인라인(inline)요소`**가 그 주위를 감싸 요소의 좌, 우측을 따라 배치되어야 하는 것을 지정한다. (블록 요소는 아니다!!)
- 본래는 이미지 좌, 우측 주변으로 텍스트를 둘러싸는 레이아웃을 위해 도입 (ex. 신문형식)
- 더 나아가 이미지가 아닌 다른 요소들에도 적용해 웹 사이트의 전체 레이아웃을 만드는데까지 발전



> **Float속성**

- none : 기본값
- left : 선택한 요소를 왼쪽으로 띄움
- right : 선택한 요소를 오른쪽으로 띄움



> **Float clear**

- 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성
- 보통 content속성과 함께 짝지어, 요소에 장식용 콘텐츠를 추가할 때 사용
- 기본값은 inline

```css
.clearfix::after {
    content: "";
    display: block;
    clear: both;
}
```

- 선행 floating 요소 다음일 수 있는지 또는 그 아래로 내려가야(해제되어, cleared) 하는지를 지정
- clear 속성은 부동 및 비부동 요소 모두에 적용된다.
- float된 것의 **`부모에 작성`**한다.(class="clearfix")



> **::after**

- CSS에서 ::after는 선택한 요소의 맨 마지막 자식으로 의사요소를 하나 생성한다. 보통 content 속성과 함께 짝지어, 요소에 장식용 컨텐츠를 추가할 떄 사용한다. (기본값은 인라인이다.)
- 위 코드는 아래요소를 위로 못올라오게 하기위해 display: block;을 설정
- https://developer.mozilla.org/ko/docs/Web/CSS/::after



> **Float 정리**

- flexbox 및 grid 레이아웃과 같은 기술이 나오기 이전에 Float는 열 레이아웃을 만드는데 사용되었다.
- flexbox와 grid의 출현과 함께, 결국 원래 텍스트 블록 내에서 **`float 이미지를 위한 역할`**로 돌아갔다.
  - MDN에서는 더 새롭고 나은 레이아웃 기술이 나와있으므로, "레거시 레이아웃 기술"로 분류하기도 한다.
- 웹에서 여전히 사용하는 경우도 있다.(ex. naver nav bar)

