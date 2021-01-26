### 5. 객체

#### 객체 생성 방법

* **객체 리터럴**
  * 배열 객체 : [1, 'abc', true, 3.4], [ ] 
  * 객체 : { 속성명 : 속성값, 속성명 : 속성값, ... , }, { }
    * 속성명 :  문자로 시작, 문자, 숫자, _ 를 사용할 수 있다.  예약어는 사용할 수 없다.
    * 속성값 : 숫자, 문자열, 논리값, 배열, 객체, 함수
    * 속성값이 함수인 아이를 메서드라고 한다. 

```
obj = {속성명1 : 100, 속성명2 : '둘리', 속성명3 : function(){...}}

// 호출은 . 연산자
obj.속성명1 = 200
obj.속성명2 + "승리"
obj.속성명3()

obj['속성명1'] = 200
obj['속성명2'] + "승리"
```



* **클래스(생성자함수)**
  * new Array(), new Date()



* **내장 객체**

>개발자가 객체를 생성하지 않아도 JavaScript 엔진이 자동으로 생성해주는 객체
>
>ex) window , document , navigator , screen , DOM객체들 등등



#### DOM(Document Object Model) 프로그래밍

* 브라우저가 웹 페이지(HTML)를 해석하고 렌더링할 때 인식된 각각의 태그들을 JavaScript객체로 생성하며 이 객체들을 DOM 객체라고 한다.
* 생성되는 DOM 객체들은 부모 자식 관계를 적용하여 트리구조로 구성한다.

```javascript
<body>
	<h1>text1</h1>
	<ol>
		<li>text2</li>
		<li>text3</li>
	</ol>
</body>


/*
각각의 태그들은 DOM객체로 형성된다.
최상위에는 document가 있다.

document.body
document.body.h1

트리형태

			document
			  body
		h1			 ol
	  text1		  li    li
	  			 text2  text3
*/

// document.body.ol.li.text1 이거 너무 불편해
// id, class 등으로 찾는다.
```



* 브라우저가 HTML문서를 읽어오는걸 타싱 그다음 렌더링



#### DOM 객체를 찾는 방법

>찾아지는 애가 없으면 DOM객체 배열은 빈 배열을, DOM 객체는 Null을 리턴한다.

* document.getElementsByTagName("tag명") 	// 같은 태그를 다 찾아서 DOM 객체배열로
* document.getElementById("id속성값") 	// DOM객체가 리턴된다,
* document.getElementsByClassName("class속성값") 	// 같은 클래스 DOM 객체 배열로
* document.querySelectorAll("CSS선택자") 	// DOM 객체 배열로, 최근 만들어져 유용
* document.querySelector("CSS선택자") 	// DOM객체 리턴, 무조건 하나일 때



* DOM 객체 타입
  * Element 타입, Attribute 타입, Text 타입



#### DOM 객체를 통한 동적처리 구현 방법

* 컨텐츠 변경하기

  * 변수에 dom객체를 담는다
  * 변수.innerHTML = "\<p>새로운내용\</p> "		(HTML 태그가 있을 때)
  * 변수.textContent = "새로운내용"					   (Content만 있을 때)	

  

* 스타일 바꾸기

  * 변수.style.CSS속성명 = CSS속성값
  * 예시) 변수.style.color = 'red'   변수.style.border = 30px
  * 변수.style.background-color = "yellow"	        (```-```기호는 못쓴다)
  * 변수.style.backgroundColor = "yellow"             (```-```기호는 빼고 그 다음 문자를 대문자로)



* 이벤트 핸들러 등록하기

  * 인라인 이벤트 모델 : 태그마다 속성으로 정의

    * <태그명 on이벤트명 = "이벤트 핸들러코드">

    

  * 고전 이벤트 모델(전역적 방식) : \<script>태그 안에 정의

    * 변수 = DOM객체
    * 변수.on이벤트명 = function(){...} 

    

  * 표준 이벤트 모델 : \<script> 태그 안에 정의

    * 변수 = DOM 객체
    * dom.addEventListener("이벤트명",function(){...})













