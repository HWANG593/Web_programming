# JavaScript

## 자바스크립트

> 웹 페이지의 동적인 처리를 구현하는 프로그래밍 언어이다.
>
> HTML 파일 안에 구현하는 프로그래밍 언어로서 인터프리터 언어이다.
>
> \<script> 태그의 컨텐트로 작성하거나 HTML 태그에 정의된 속성의 값으로 작성한다.

### 자바스크립트 구문

* 파이썬 , R 과 비슷한 구문을 많이 가지고 있다.
* 세 언어 모두 인터프리터 언어로 분류된다.



### 자바스크립트의 정의방법

* JavaScript 코드는 가급적 \<body> 태그의 마지막 부분 즉, \</body> 태그의 바로 위에 삽입한다.

 

### API(Application Programming Interface)

> 프로그래밍 할 때 자주 구현되는 기능들을 미리 구현해 놓은 프로그램
>
> 프로그래밍 언어마다 자기만의 API를 가진다. 
>
> 개발 환경 구축 시 함께 설치되는 API를 표준 API라고 한다. 
>
> 개발자가 필요에 의해 추가로 설치하는 API들을 확장 API 또는 third-party API 라고 한다.

* C언어 : 함수
* Java 언어 : 클래스(메서드)
* Python, Javascript, R 언어 : 함수, 클래스(메서드)



### 목차

1. 변수 정의 방법과 처리 가능한 데이터 타입

2. 연산자와 제어문

3. 배열(array) - 파이썬 리스트

4. 함수 정의 방법, 함수 사용 방법(호출)

5. 함수는 일급 객체이다.

6. 객체 생성 방법 - 클래스를 가지고 객체를 생성하는 방법

   ​						  - {중괄호}를 사용해서 객체를 생성하는 방법 - 객체리터럴

7. 이벤트 처리하는 방법, DOM 객체를 통해서 HTML 태그를 제어하는 방법
8.  jQuery : Javascript의 대표적인 API - 간단한 자바스크립트 구현을 지원



### 1. 변수 정의 방법과 처리 가능한 데이터 타입

* number (숫자 타입)
* string (문자열 타입)
* boolean (논리 타입) : true, false
* null
* undefined



### 2. 연산자와 제어문

#### 주요 연산자

* 수치 연산자
  * 덧셈(+), 뺄셈(-), 곱셈(*), 나눗셈(/), 나머지(%), 증감 연산자(++,--), 단항 연산자(-)
  * 문자열 연산자의 (+) : 문자열을 합하여 하나의 문자열 생성
  * 문자열 + 숫자 : 숫자를 문자열로 변환해서 문자열(+) 연산이 된다.

* 비교 연산자
  * <, >, <=, >=, ==, ===, !=, !==

* 조건 연산자
  * and 연산자(&&), or 연산자(||), not연산자(!)
* 비트 연산자
  * 비트 AND(&), 비트 OR(|), 비트 XOR(^), 비트 좌우 이동(<< , >>)
* 타입 점검 연산자
  * typeof, instanceof
* 삭제 연산자
  * delete
  * 

#### 조건제어문 if

```
if (조건식)
	수행문장;
	
if (조건식){
	수행문장
	수행문장
	   :
}

if (조건식)
	수행문장;
else if (조건식)
	수행문장;
else
	수행문장;
```



#### 다중분기문 switch

* switch 문에  사용되는 비교식은 데이터 타입의 제한이 없다.



#### 반복제어문

>for ... in 반복문 사용이 가능하다 (for-each 문이라고도 한다.)
>
>for ... in 명령은 지정된 배열이나 객체 내의 요소/멤버에 대해 선두부터 마지막까지 순서대로 반복 문장을 수행한다.

* **for문**
* 초기식, 조건식, 증가식으로 구성되는 for문



* **for - in**
* 배열이나 객체를 가지고 반복을 처리하는 for문 
* for(인덱스(키)를 저장할 변수 정의 in 배열 또는 객체)

```javascript
일반(전통)for : for(초기식; 조건식; 증감식)
					반복수행문장
for(변수정의와 초기화식; 반복처리를 계속할지 결정하는 조건식; 변수의 값을 변화시키는 식)
for(var num=1; num<11; num+=1)	//둘다 10번 반복 num변수 실제로는 안씀 그냥 루프용
for(var num=10; num>0; num-=1)	//둘다 10번 반복	num변수 실제로는 안씀 그냥 루프용
for(var num=10; num<20; num-=1)	//몇 번 반복하는지가 주목적이면 원하는대로 표현해

for(var num=1; num<=50; num+=1) //1부터 50까지의 값을 1씩 증가시키면서 처리해라!
for(var num=1; num<=50; num+=2) //1부터 50까지의 값을 2씩 증가시키면서 처리해라!


향상된 for, for-in, for-each : 
for(변수정의 in 배열 또는 객체)
		반복수행문장

a = [10,20,30,40,50] //array 배열
					  
for(var i in a){	// a가 갖고있는 element만큼 반복하면서 i에 element의 index 전달
	window.alert(i)	// why?  a자리에 아무객체나 다 올수 있어서
	window.alert(a[i]) // a의 값을 꺼내오고 싶다.
	}

//실행 결과
0,1,2,3,4		// 인덱스
10,20,30,40,50	// 실제 값
```



* **while문**

```javascript
while(조건식)
	반복문장;
	
while(true)
	무한반복문장;
```



* **do-while문**



#### 분기제어문

> 중첩된 반복문에서 사용될 때 레이블을 사용하여 외부 반복문에 대한 제어가 가능하다.

* break : 반복문을 종료해라

* continue : 다음 반복으로 계속해서 진행해라



#### 예외처리 구문

* try - catch - finally 구문을 사용하여 실행 오류 발생시의 대비 코드 구현이 가능하다.



### 3. 배열

> 파이썬의 리스트와 비슷하다.
>
> 묶을 수 있는 데이터의 갯수에 제한이 없고, 데이터 타입도 제한이 없다.
>
> 자바스크립트의 배열도 객체로 취급된다.



#### 배열 생성 방법

* 배열 리터럴 방법
  * [1,2,3,4,5]
  * ['aaa', 100, true, 3.4]
  * \[ ] : element가 없는 배열
  * [,,,,,,,] : 방은 지정했지만 값은 없다. 즉, undefined가 여러개 출력됌



* API를 이용하는 방법 - Array

  * new Array(1,2,3,4,5)
  * new Array('aaa', 100, true, 3.4)

  * new Array()
  * new Array(8) : 8개의 공간을 가진 Array를 만들겠다. 그러나 값은 정해지지 않았다.

```javascript
var array_example1 = new Array("hello","world");
var array_example2 = ["hello","world"];
var array_example3 = [];

array_example3.push("5")
array_example3.push("7")
array_example3[2] ="2"
array_example3[3] ="12"

var array_example4 = [];
array_example4.push(0)	//[0]
array_example4.push(0)	//[0,2]
array_example4.push(7)	//[0,2,7]
array_example4.pop()	//[0,2]

var array_example5 = ["world","hello"];
array_example5.reverse()	//["hello","world"]

var array_example7 = [3,4,6,1];
array_example7.sort();	//[1,3,4,6]
```



#### 배열 사용 방법

* 배열의 크기 : 배열을 구성하는 엘리먼트의 갯수
  * 배열객체의 length라는 속성(변수)의 값을 사용한다.



* 배열의 요소(원소, 엘리먼트)를 접근 (L-value, R-value 모두 가능)
  * [0부터 시작하는 인덱스]



### 4. 함수

> JavaScript의 함수는 일급 객체를 만족한다.

* 일급 객체로 취급된다.
  * 함수를 변수에 담아서 사용할 수 있다.
  * 함수 호출 시 아규먼트로 전달이 가능하다.
  * 함수를 리턴값으로 전달이 가능하다.
* ​	함수를 호출할 때 함수에 정의된 매개변수만큼 아규먼트를 전달하지 않아도된다.
  * 상황에 따라 자동으로 undefined가 전달된다.
* 함수가 값을 리턴하지 않으면 undefined가 자동으로 리턴된다.
* 가변인수를 지원한다. 함수 호출시 아규먼트의 갯수에 제한이 없는 함수를 만들 수 있다.
  * 가변인수 함수를 정의할 때는 매개변수 정의를 생략한다.
  * 함수 호출 시 자동으로 만들어지는 arguments 라는 배열을 활용한다.
* 기본값을 갖는 매개변수를 정의할 수 있다.



#### 함수 정의 방법

```javascript
// 선언적 함수 정의(명시적 함수 정의)
function 함수명(매개변수1,...., n개) {
			함수의 수행 코드
				  :
			return 리턴값;
}

// 함수 표현식(함수 리터럴)
(var) 변수 = function (매개변수1,...., n개) {	//변수를 함수이름으로 사용할 수 있다.
			함수의 수행 코드
				  :
			return 리턴값;
			}

// 함수의 아규먼트로 함수 전달하기
var myFn = function( fn ) {
                var result = fn();
                console.log( result );
            };
myFn(function() {return "hello world";}); //실행되면 아규먼트 자리 fn에 함수가!
```



#### 함수의 아규먼트 활용

* 함수의 호출과 인수
  * 함수 호출 시 매개변수와 리턴 값의 존재여부에 따라 다양한 형식으로 호출이 가능하다
  * JavaScript에서는 메서드 호출 시 아규먼트 개수와 함수 정의 시 선언된 매개변수 개수의 일치를 체크하지 않는다.
  * 매개변수에 아규먼트를 전달하지 않으면 변수의 값은 **undefined**가된다.
  * 매개변수보다 더 많은 인수가 전달된 경우 **arguments**라는 함수의 내장변수를 사용한다.



#### 함수 사용 방법

* 고계(고차) 함수(High-Order Function) : **함수를 데이터로 다루는 함수**
  * Javascript에서는 함수도 데이터 타입의 한 종류이다.
  * 즉, 함수도 다른 수치타입이나 문자열 타입 등과 같이 함수의 인수나 리턴값으로 될 수 있다.
  * 함수 호출 시 인수로 또 다른 함수를 전달할 수 있다.
  * 리턴 값으로 함수를 전달할 수 있다.





### 5. 변수

#### 변수 정의 방법

```javascript
var v1 = 10			// 선언
v1 = 100			// 할당
var v1 = 1000		// v1 = 1000이된다.


function f1(){
	var v2 = 20		// var를 붙이면 지역 변수
	v2 = 20 		// 전역 변수
	var v2 = 200	// v2 = 200이 된다.
}

<script src="과장님.js"></script>
<script src="대리님.js"></script>
// 과장님과 대리님 모두 v1전역변수를 사용하고 있다면
// 이 아래 스크립트에서 과장님의 v1 변수는 사용할수가 없게된다.

```



* **var** : 선언과 할당을 반복해서 할 수 있다.
* **let** : 선언은 단 한번, 할당은 반복해서 할 수 있다.
* **const** : 선언과 할당 모두 한번만 할 수있다.

```javascript
var num1 = 100;
let num2 = 200;
const num3 = 300;

num1 = '가';
num2 = '나';
num3 = '다';			// 할당 불가능 오류

var num1 = 3.5;
let num2 = 4.7;		// 선언 불가능 오류
const num3 = 5.3;	// 선언과 할당 불가능 오류

```



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

    

  * 고전 이벤트 모덜(전역적 방식) : \<script>태그 안에 정의

    * 변수 = DOM객체
    * 변수.on이벤트명 = function(){...} 

    

  * 표준 이벤트 모델 : \<script> 태그 안에 정의

    * 변수 = DOM 객체
    * dom.addEventListener("이벤트명",function(){...})