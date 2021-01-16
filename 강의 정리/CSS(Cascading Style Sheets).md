### CSS(Cascading Style Sheets)

#### CSS란?

> HTML 태그에 의해서 웹 페이지가 출력(렌더링)될 때 스타일을 조정할 수 있는 기술

* 구조적으로 짜여진 문서**(HTML, XML)**에 **Style(글자, 여백, 레이아웃)**을 적용하기 위해 사용하는 언어이다.
* CSS 스타일 시트는 **HTML** 문서의 요소에 적용되는 **CSS** 스타일 정의를 포함하며 CSS 스타일은 요소 표시 방법 및 페이지에서의 요소 위치를 지정한다.
* **W3C**의 표준이며 **HTML** 구조는 그대로 두고 **CSS** 파일만 변경해도 전혀 다른 웹사이트 처럼 꾸밀 수 있다.

```html
<h1 style = 'color : orange ; background-color : green'>올라프</h1>

<style>
	h1{								# h1 CSS 선택자
		color : orange				# CSS 속성 
		background-color : green
	}
	
</style>
```



#### CSS를 사용한 웹 페이지 개발

* 웹 표준에 기반한 웹 사이트를 개발할 수 있다.
* 클라이언트 기기에 알맞는 반응형 웹 페이지를 개발할 수 있다.
* 이미지의 사용을 최소화시켜 가벼운 웹 페이지 개발을 가능하게 한다.



#### CSS 사용의 이점

* 확장성 : 표현을 더욱 다양하게 확장하거나 표현 기능의 변경 가능
* 편의성 : 훨씬 간편하게 레이아웃 등의 스타일 구성
* 재사용성 : 독립된 스타일 모듈 작성, 여러 HTML 문서에 공통으로 활용
* 생산성 : 역할 분담에 따른 전문화, 모듈 단위의 협업과 생산성의 향상



#### CSS의 작성 방법

* 인라인 방법 - **HTML**엘리먼트에 **Style**이라는 속성으로 정의하는 방법

  * <tag style = "property: value">

* 전역적 방법 - **\<style>** 이라는 태그에 웹 페이지의 태그들에 대한 스타일을 정의하는 방법

  * \<style type = "text/css">
    selector {

    ​		property :value;

    }
    \</style>

* 외부 파일 연결 방법 - 독립된 파일(확장자.css)을 만들어서 **HTML** 문서에 연결하는 방법
  * \<link rel = "stylesheet" type="text/css" href="style.css"/>



#### CSS 스타일 선언 형식

* 선택자(selector) : 스타일을 적용할 대상을 지정
* 스타일 속성(property) 블록 : 선택된 영역에 적용할 색상, 크기 등 ({})로 둘러싸며 (;)로 구분

```css
h1 								/* 선택자 */
{								/* 스타일 속성 블록 시작 */
	color : blue;				/* 스타일 속성 : 스타일 속성 선언 */
	background : gray;
}								/* 스타일 속성 블록 종료 */
```



#### Cascade Style Sheet

* CSS 선택자(selector)란

  * 스타일을 적용하기 위해 대상을 선택하는 방법

  

* 전체 선택자(*)
  * 페이지에 있는 모든 요소를 대상으로 스타일을 적용할 때 사용
  * 다른 선택자와 함께 모든 하위 요소에 한꺼번에 스타일을 적용하려고 할 때 주로 사용
  * 예) *{margin : 0; padding : 0;}



* 태그 선택자(div, img, h1 등)
  * 문서 안의 특정 태그에 스타일이 모두 적용됨
  * 예) p{font-size : 12px; font-family : "돋음";}



* 클래스 선택자(.class)
  * 문서 안에서 여러번 반복할 스타일이면 클래스 선택자로 정의, .뒤에 클래스 이름 지정
  * 예) .redtext{color : red;}



* id 선택자(#id)

  * 문서 안에서 한번만 사용한다면 id 선택자로 정의하며 파운드(#) 다음에 id 이름 지정
  * 예) #pic2{clear : both; float:left;}

  

* 하위 선택자(descendant selector)

  * 부모 요소에 포함된 모든 하위 요소에 스타일이 적용된다.
  * 하위 선택자를 정의할 때는 상위 요소와 하위 요소를 나란히 작성한다.
  * 예) section p{color : blue;}



* 자식 선택자(child selector)
  * 부모 요소의 자식 요소에만 스타일이 적용된다.
  * 예) section > p{color : blue;}



* 인접 형제 선택자(adjacent selector)

  * 문서 구조상 같은 부모를 가진 형제 요소 중 첫 번째 동생  요소에만 스타일이 적용된다.

  * 같은 부모 요소를 가지는 요소들을 형제 관계라고 부른다. 먼저 나오는 요소를 '형 요소'

    나중에 나오는 요소를 '동생 요소'라고 한다.

  * 예) h1 + p{text-decoration : underline;}



* 형제 선택자(sibling selector)
  * 형제 요소들 중에서 모든 동생 요소들에 스타일이 적용된다.
  * 예) h1 ~ p{text-decoration : underline;}



* 그룹 선택자(group selector)
  * 같은 속성을 적용해야할 경우 똑같은 스타일을 두번 정의하지 않고 한번에 묶어서 정의한다.
  * 쉼표로 선택자 구분
  * 예) a, p{color : #fffff;}



* 속성 선택자(property selector)
  * 태그에 정의된 속성과 속성의 값을 가지고 대상을 정하는 선택자이다.

|     표기     | 설명                                                         |
| :----------: | ------------------------------------------------------------ |
|    [속성]    | 지정한 '속성'을 가지고 있는 요소를 찾아 스타일을 적용        |
| [속성 ~= 값] | '속성'과 '값'을 체크해 여러 개의 값 중 하나만 일치해도 스타일을 적용 |
| [속성 ^= 값] | '속성'의 '값'이 지정한 문자로 시작하는 속성값에 대해서만 스타일을 적용 |
| [속성 $= 값] | '속성'의 '값'이 지정한 문자로 끝나는 속성에 대해서만 스타일을 적용 |
| [속성 *= 값] | 속성 값 중에 '값'의 일부가 포함되어 있는 속성에 스타일을 지정 |



* 가상 선택자(pseudo selector)
  * 웹 문서의 소스에는 실제로 존재하지 않지만 필요에 의해 임의로 가상의 선택자를 지정하여 사용하는 것을 말한다.

|     표기      | 설명                                                         |
| :-----------: | ------------------------------------------------------------ |
| :first-letter | 첫 번째 문자에 스타일을 적용한다.                            |
|  :first-line  | 첫 번째 행에 스타일을 적용한다.                              |
| :first-child  | 첫 번째 자식 요소에 스타일을 적용한다.                       |
|  :last-child  | 마지막 자식 요소에 스타일을 적용한다.                        |
|    :before    | 특정 요소의 내용 앞에 지정한 내용을 만든다.                  |
|    :after     | 특정 요소의 내용 뒤에 지정한 내용을 만든다.                  |
|    :hover     | 사용자가 대상 요소를 가리키고 있을 때 스타일을 적용한다.(롤 오버 등) |
|    :focus     | 대상 요소가 포커스 되었을 때 스타일을 적용한다.              |



#### 주요 CSS 속성들

* GENERAL : Class, ID, div, span, color, cursor, display, overflow, visibility

* TEXT : letter-spacing, line-height, text-align, text-decoration, text-indent, text-transform,

  ​            vertical- align, word-spacing

* FONT : font-style, font-variant, font-weight, font-size, font-family

* BOX MODEL : height, width, margin-top, margin-bottom, margin-right, margin-left, 

  ​                         padding-top, padding-bottom, padding-right, padding-left

* BORDER : border-width, border-style, border-color

* BACKGROUND : background-color, background-image, background-repeat

  ​                              background-attachment, background-position

* POSITION : clear, float, left, top, position, z-index
* LIST : list-style-type, list-style-position, list-style-image



#### CSS3에서 추가된 속성들

* 새로운 CSS3 속성을 부분적으로만 지원할 수 있기 때문에 대부분의 CSS3 프로퍼티를 사용하려면 프로터피 앞에 브라우저를 식별할 수 있는 접두어를 붙여야 하는 것도 있다.

| 접두어   | 브라우저              |
| -------- | --------------------- |
| -webkit- | 사파리, 크롬 등       |
| -moz-    | 모질라, 파이어폭스 등 |
| -o-      | 오페라                |
| -ms-     | 인터넷 익스플로러     |



* **border-radius**

```css
div.rounded {
	background-color : #666;
	color : #fff;
	width : 400px;
	padding : 10px;
	-webkit-border-radius : 20px;
	-moz-border-radius : 20px;
	border-radius : 20px;
}
```



* **box-shadow**

| 속성        | 내용                                           |
| ----------- | ---------------------------------------------- |
| 가로 오프셋 | 양수 값은 오른쪽, 음수 값은 왼쪽에 그림자 생김 |
| 세로 오프셋 | 양수 값은 아래쪽, 음수 값은 위쪽에 그림자 생김 |
| blur radius | 그림자의 번지는 정도, 0이 최소값               |
| 그림자 색상 | 16진수나 RGB값, 색상 이름 모두 사용 가능       |

```css
<style type = "text/css">
a img:hover{
	box-shadow : 0px 5px 10px rgba(0,0,0,0.6);
	-moz-box-shadow : 0px 5px 10px rgba(0,0,0,0.6);
	-webkit-box-shadow : 0px 5px 10px rgba(0,0,0,0.6);
}
</style>
```



* **text-shadow**

```css
<style>
body{
	background : #066;
	font-family : Arial Black;
	font-size : 50px;
}

.text1{
	color:#fff;
	text-shadow : 0px 1px 8px #fff;
}

.text2{
	color:#fff;
	text-shadow : 1px -3px 8px #6F0;
}

.text3{
	color:#000;
	text-shadow : 1px 1px 4px #fff;
}
</style>

######################################################################
<style>
body{
	background : #000;
	font-family : Arial Black;
	font-size : 50px;
}

.text3{
	color : #000;
	text - shadow : 0px 0px 4px #ccc,
					0px -5px 4px #ff3,
					2px -10px 6px #fd3,
					-2px -15px 11px #f80,
					2px -19px 18px #f20;
}
</style
```



* **gradient**
  * background : linear-gradient(direcition, color1, color2, ..., color3);

| direction | 내용                  |
| --------- | --------------------- |
| to bottom | 위에서 아래로(기본값) |
| to top    | 아래에서 위로         |
| to left   | 오른쪽에서 왼쪽으로   |
| to right  | 왼쪽에서 오른쪽으로   |
| ndeg      | n도의 방향            |



* **opacity**
  * 칼라나 이미지의 투명도를 설정하는 속성으로 0.0~1.0 사이의 값을 설정한다.

```css
<style>
.noopa{
	background-color : #fff;
	color : #000;
}

.opa{
	background-color : #fff;
	opacity : 0.5;
	color : #000;
}
</style>
```



