# AJAX 프로그래밍

### XML(Extensible Markup Language)

#### XML 문서

* XML 선언부를 제외하고는 기존 HTML5의 기본 구조와 사용 방법이 거의 유사
* XML 문서 선언부
  * 반드시 맨 앞에 명세, XML 문서 유형을 지정
  * XML 문서 구조를 정의한 DTD(또는 XML Schema) 선언, 스타일을 정의한 CSS 연결에 대한 선언도 명세
* 하나의 최상위 엘리먼트의 <시작태그>로 시작해서 </종료태그>로 끝남
* 최상위 엘리먼트를 포함하여 XML 문서의 모든 태그들은 자유롭게 정의
* 엘리먼트의 시작 태그 안의 속성도 자유롭게 정의

<br>

### JSON

* JSON 이란?
  * JSON( JavaScript Object Notation )은 인터넷에서 자료를 주고 받을 때 그 자료를 표현하는 방법이다. 자료의 종류에 큰 제한은 없으며, 특히 컴퓨터 프로그램의 변수 값을 표현하는데 적합하다.
  * 형식은 JavaScript 구문을 따르지만, 프로그래밍 언어나 플랫폼에 독립적이므로 C,C++,C#, 자바, 파이썬 등등 많은 언어에서 이용할 수 있다.
* JSON의 장점
  * JSON은 텍스트로 이루어져 있으므로, 사람과 기계 모두 읽고 쓰기 쉽다.
  * 프로그래밍 언어와 플랫폼에 독립적이므로, 서로 다른 시스템 간에 객체를 교환하기에 좋다.
  * JSON은 개방형 표준이며, 읽기 및 쓰기가 쉽고 가볍다.

<br>

### XML과 JSON 비교

```javascript
// JSON 형식

{
	"students" : {
		"student" : [
			{"name" : "홍길동", "gender" : "남"},
			{"name" : "홍길순", "gender" : "여"},
		]
	}
}


// XML 형식

<students>
	<student>
		<name>홍길동</name> <gender>남</gender>
	</student>
	<student>
		<name>홍길순</name> <gender>여</gender>
	</student>
</students>
```

<br>

---

<br>

### AJAX

#### AJAX ( Asynchronous JavaScript and XML)

* 재로드(refresh 재갱신)하지 않고 웹페이지의 일부만을 갱신하여 웹 서버와 데이터를 교환하는 방법
* **빠르게 동적 웹페이지를 생성하는 기술**
* 비동기통신

<br>

#### AJAX의 동작 과정

	1. 이벤트 발생에 의해 이벤트 핸들러 역할의 JavaScript 함수를 호출한다.
	2. 핸들러 함수에서 XMLHttpRequest 객체를 생성한다. 요청이 종료되었을 때 처리할 기능을 콜백 함수로 만들어 등록한다.
	3. XMLHttpRequest 객체를 통해 서버에 요청을 보낸다.
	4. 요청을 받은 서버는 요청 결과를 적당한 데이터로 구성하여 응답한다.
	5. XMLHttpRequest 객체에 의해 등록된 콜백함수를 호출하여 응답 결과를 현재 웹 페이지에 반영한다.

<br>

#### XMLHttpRequest 객체

* 서버 측과의 비동기 통신을 제어하는 것은 XMLHttpRequest 객체의 역할이다.
* XMLHttpRequest 객체를 이용함으로써 지금까지 브라우저가 실행해 온 서버와의 통신 부분을 JavaScript가 제어할 수 있게 된다.
* XMLHttpRequest 객체 생성 : **new XMLHttpRequest()**

<br>

#### open() 과 send() 메서드

* **open( HTTP 메서드, URL[ ,비동기 모드 통신 여부 ])**
  * HTTP 메서드 : 요청 방식(GET, POST, PUT, DELETE)
  * URL : AJAX로 요청하려는 서버의 대상 페이지
  * 비동기 모드 통신 여부 : true(비동기통신), false(동기통신)

* send([요청 파라미터])
  * POST의 경우 Query 문자열을 인수로 지정
  * ArrayBufferView, Blob, Document, DOMstring, FormData, null 이 올 수 있다.

<br>

#### jQuery의 AJAX 지원 API

<br>

#### AJAX 프로그래밍 핵심 내용

* JSON(XML) 형식으로 응답하는 뷰를 준비해야 한다.

  * 템플릿을 거치지 않고 뷰가 직접 응답

* JavaScript만 사용해서 AJAX 요청을 구현하는 방법

  ```javascript
  var xhr = new XMLHttpRequset()
  xhr.onload = 함수
  xhr.open("GET", 대상URL, true)
  xhr.send()
  ```

<br>

#### $.ajax() 메서드

* 모든 AJAX 메서드가 내부적으로는 사용하는 기본 메서드
* AJAX 요청을 기본적인 부분부터 직접 설정하고 제어할 수 있어 다른 AJAX 메서드로 할 수 없는 요청도 수행 가능
* $.ajax() 메서드의 기본 형식
  * $.ajax({ url:URL주소 \[,type: 요청방식]\[,data: 요청내용]\[,timeout: 응답제한시간]\[,dataType: 응답데이터유형]\[,async: 비동기여부]\[,success: 성공콜백함수]\[,error:실패콜백함수]});

| 선택항목 : 항목값         | 의미                                                         |
| ------------------------- | ------------------------------------------------------------ |
| url : URL 주소            | 요청이 보내질 서버의 URL 주소(필수 항목, 기본값: 현재 페이지)<br />예)"sample.php", "sample.html", "sample.xml" |
| type : 요청방식           | 요청을 위해 사용할 HTTP 메소드<br />예) "get"(기본값), "post" |
| data : 요청내용           | 서버로 전달되는 요청 내용(jQuery 객체 맵이나 문자열)         |
| timeout : 응답제한시간    | 요청 응답 제한 시간 (밀리초)<br />예) 20000                  |
| dataType: 응답데이터 유형 | (서버로부터) 반환될 응답 데이터의 형식<br />예) "xml", "html", "json", "jsonp", "script", "text" |
| Async : 논리값            | 요청이 비동기식으로 처리되는지 여부(기본값 : true)           |
| success : function(data)  | 요청 성공 콜백함수(data: 서버 반환 값)                       |
| error : function()        | 요청 실패 콜백함수                                           |

<br>

#### $.getJSON() 메서드

* GET 요청 방식으로 서버로부터 JSON 형식의 데이터를 요청
* **$.getJSON( url [,data] [,function(data)] );**

| 인자           | 의미                                                         |
| -------------- | ------------------------------------------------------------ |
| url            | 요청이 보내질(주로 서버)의 URL주소(필수 항목, 기본값 : 현재 페이지)<br />예) "sample.json" |
| data           | 서버로 전달되는 요청 내용(jQuery 객체 맵이나 문자열)         |
| function(data) | 요청 성공 콜백 함수(data:서버 반환 값)                       |

<br>

#### $.load() 메서드

* 서버로부터 데이터를 받아오는 가장 간단한 메서드로 많이 이용
* 서버로부터 데이터를 받아 메서드를 실행하는 대상 엘리먼트에 직접 추가
  * 복잡한 선택사항을 설정하지 않고도 빠르고 간단하게 웹페이지의 동적 갱신이 가능
* 요청이 성공하면 메서드가 실행되는 대상 엘리먼트 내용이 서버에서 응답 받은 HTML5 마크업 데이터로 대체
* **$.load( url \[,data][,function(data)])**

| 인자           | 의미                                                         |
| -------------- | ------------------------------------------------------------ |
| url            | 요청이 보내질(주로 서버)의 URL주소(필수 항목, 기본값 : 현재 페이지)<br />예) "sample.json" |
| data           | 서버로 전달되는 요청 내용(jQuery 객체 맵이나 문자열)         |
| function(data) | 요청 성공 콜백 함수(data:서버 반환 값)                       |

<br>

```javascript
// $.ajax() : 모든 Ajax 메소드의 기본이 되는 메소드

$.ajax({
		url:'service.php',
		success: function(data) {
			$('#area').html(data);
		}
});


// $.getJSON() : JSON 형식으로 응답 받는 ajax() 메소드

$.getJSON('sample.json', function(data){
		$('#area').html('<p>'+data.age+'</p>');
});

// $.load() : 서버로부터 데이터를 받아서 일치하는 요소 안에 HTML을 추가

$('#area').load('sample.html', function(){
    ;
})
```

<br>

#### Same Origin Policy(SOP)

* 브라우저에서 보안상의 이슈로 **동일 사이트의 자원(Resource)만 접근**해야 한다는 제약
* **AJAX는 이 제약에 영향을 받으므로 Origin 서버가 아니면 AJAX로 요청한 컨텐츠를 수신할 수 없다.**

<br>

#### Cross Origin Resource Sharing(CORS)

* 초기에는 Cross Domain이라고 하였다.(동일 도메인에서 포트만 다른 경우, 로컬 파일인 경우 등으로 인해 Origin이라는 용어로 통일됨)
* **Origin이 아닌 다른 사이트의 자원을 접근하여 사용한다는 의미이다.**
* Open API의 활성화와 공공 DB의 활용에 의해서 CORS의 중요성이 강조되고 있다.
* HTTP Header에 CORS와 관련된 항목을 추가한다.

```
response.addHeader("Access-Control-Allow-Origin","*");
```

