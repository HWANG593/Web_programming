# Django

## Django(장고) 프로그래밍

<br>

### 웹의 기본 이해

> 웹은 보통 **월드 와이드 웹(WWW)**이라고도 하며, 인터넷이라는 연결을 통해 여러 컴퓨터가 연결되어 서로 정보를 나누는 연결망들을 의미한다. 이 웹이라는 것을 어떤 관점에서 보냐에 따라 다음과 같은 개념이 생긴다.

<br>

#### 정보를 제공하는 컴퓨터와 정보를 받아가는 컴퓨터

* 서버(serever)  

  정보를 제공하기 위해 고정된 주소(도메인, 고정 IP 등)를 차지하며 방문하는 컴퓨터들에게 필요한 정보를 제공한다. 보통 우리가 접속하는 웹 사이트들이 이에 해당한다.  

* 클라이언트(clients)  

  정보를 제공받기 위해 서버를 찾아 접속하는 컴퓨터이다. 보통은 고정된 주소 없이 인터넷 연결을 통해 서버에 접근한다. 일반적으로 우리가 웹 브라우징을 위해 쓰고 있는 컴퓨터들이 이에 해당한다.

<br>

#### 웹 프로그램의 구조 별 개념

* 프론트엔드 (Front-end)

  **사용자들이 보는 화면의 모습을 결정**, 보통 HTML CSS JavaScript로 구성되고 클라이언트의 웹 브라우저에서 코드가 실행되거나 그려진다.  

* 백엔드 (Back-end)

  **사용자가 접속하면 그에 맞는 데이터를 보내주기 위해 여러가지 처리를 담당하는 로직을 구성**한다. Django기반의 Python이나 데이터베이스 등이 여기에 속한다.  프론트엔드 코드 조각들을 여기서 가지고 있다가, 사용자에게 적절하게 처리해서 보내주는 역할도 한다.

<br>

#### 서버 - 클라이언트 간통신 방향 별 개념

* 요청 (Request)

  **클라이언트가 서버로 원하는 정보를 받기 위해 필요한 정보를 보내는 과정**, 보통은 클라이언트의 IP와 접속하고 있는 브라우저 프로그램이나 모바일 여부, 요청하는 URL과 방식, 그리고 필요한 경우 서버가 처리하기 위한 데이터들을 보낸다.

* 응답 (Response)

  **요청을 받은 서버가 받은 데이터를 처리하여 사용자에게 정보를 내려주는 것**, 응답에는 여러가지 형태의 데이터가 내려갈 수 있는데, 우리가 보통 웹 사이트에 접속했을 때 보여지는 화면들은 응답에 HTML, CSS, JavaScript 코드가 포함되어 그걸 웹 브라우저가 해석하고 실행하여 화면에 그려주게 되는 케이스가 속한다.(JSON, XML 등)

<br>

---

<br>

### HTTP 프로토콜(통신 규약)

<br>

#### HTTP(Hypertext Transfer Protocol)

* 상호간에 정의한 규칙을 의미하며 특정 기기 간에 데이터를 주고받기 위해 정의
* "나는 이렇게 줄테니 넌 이렇게 받고 난 너가 준거 그렇게 받을게" - 규칙 정의
* 웹에서는 브라우저와 서버 간에 데이터를 주고받기 위한 방식으로 **HTTP 프로토콜**을 사용한다.

<br>

#### HTTP 프로토콜의 특징

* HTTP 프로토콜은 상태가 없는(stateless) 프로토콜이다.
* 즉, 데이터를 주고 받기 위한 각각의 데이터 요청이 서로 독집적으로 관리가 된다
* 이는 이전 데이터 요청과 다음 데이터 요청이 서로 관련이 없다는 것이다.
* 따라서 서버는 세션과 같은 별도의 추가 정보를 관리하지 않아도 되고, 다수의 요청 처리 및 서버의 부하를 줄일 수 있는 성능 상의 이점이 생긴다.
* HTTP 프로토콜은 일반적으로 TCP/IP 통신 위에서 동작하며 기본 포트는 **80**번이다.

<br>

#### HTTP Request & HTTP Response

* HTTP 프로토콜로 데이터를 주고받기 위해서는 Client는 Request를 보내고 Server에게서 Response를 받아야 한다.
* 요청과 응답을 이해하기 위해서는 클라이언트와 서버를 이해해야 한다.
* 클라이언트란 요청을 보내는 쪽을 의미하며 웹 관점에서는 브라우저를 의미한다.
* 서버란 요청을 받는 쪽을 의미하며 데이터를 보내주는 원격지의 컴퓨터를 의미한다.

<br>

#### URL(Uniform Resource Locators)

* URL은 **서버에 자원을 요청하기 위해 입력하는 영문 주소**이며 구조는 아래와 같다.
* http://www.domain.com:1234/path/to/resource?a=b&x=y
  * http : 프로토콜
  * www.domain.com : host
  * 1234 : 포트번호
  * path/to/resource : resource path 경로
    * resource path가 생략되면 기본파일(index.html)을 달라는 의미로 해석된다.
  * a=b&x=y : query

<br>

#### HTTP 요청 메서드

* 앞에서 살펴본 URL을 이용하면 서버에 특정 데이터를 요청할 수 있다. 여기서 요청하는 데이터에 특정 동작을 수행하고 싶으면 HTTP 요청 메서드(HTTP Request Methods)를 이용한다.

| HTML 사용 시 요청 방식          | 방식                               |
| ------------------------------- | ---------------------------------- |
| GET : 존재하는 자원에 대한 요청 | PUT : 존재하는 자원에 대한 변경    |
| POST : 새로운 자원을 생성       | DELETE : 존재하는 자원에 대한 삭제 |

<br>

#### HTTP 상태 코드

* 2xx - 성공 , 3xx - 리다이렉션 , 4xx - 클라이언트 에러 , 5xx - 서버에러

  ​									HTTP Request(URL + 요청메서드)  ㅡ>

  ​			브라우저      																				서버

​									<ㅡ HTTP Response(상태 코드 + 응답 Body)

<br>

---

<br>

## Django(장고)

> 장고는 파이썬으로 작성된 **오픈 소스 웹 애플리케이션 프레임워크**로, 모델-뷰-컨트롤러 패턴을 따르고 있다.
>
> 고도의 데이터베이스 기반 웹사이트를 작성하는데 있어 수고를 더는 것이 주된 목표이다.

<br>

### 라이브러리와 프레임워크

#### 라이브러리(API)란

* **재사용이 필요한 기능으로 반복적인 코드 작성을 없애기 위해 언제든지 필요한 곳에서 호출하여 사용할 수 있도록 class나 Function으로 만들어진 것**
* 사용여부는 코드 작성자의 선택 사항이며 새로운 라이브러리 제작 시에도 엄격한 규칙은 없다.
* 프로그램 제작 시 필요한 기능이며 자동차로 치면 (바퀴, 헤드라이트, 에어백 등) 부품에 해당한다.

<br>

#### 프레임워크란

* 원하는 기능 구현에만 집중하여 빠르게 개발할 수 있도록 기본적으로 필요한 기능을 갖추고 있는 것으로 위에서 설명한 라이브러리가 포함되어 있다.
* **프레임워크만으로는 단독으로는 실행되지 않으며, 기능을 추가해야한다.**
* **프레임워크에 의존하여 개발해야하고, 프레임워크가 정의한 규칙을 준수해야 한다.**
* 프로그램 기본 구조(뼈대)역할이며 자동차로 치면 (자동차 프레임)에 해당한다

<br>

#### 장고 프로그램 개발 패턴

#### SW 개발 패턴 : **MVC(Model View Controller) 패턴**

>사용자 인터페이스로부터 비즈니스 로직을 분리하여  애플리케이션의 시각적인 요소나 그 이면에서 실행되는 비즈니스 로직을 서로 영향없이 쉽게 유지 보수할 수 있는 애플리케이션을 만들 수 있다.

* Model : 애플리케이션에서 처리하는 데이터 ( 처리 데이터 )
* View : 사용자 인터페이스 요소 ( 응답 로직 ) - HTML
* Controller : 데이터와 비즈니스 로직 사이의 상호동작을 관리 ( 요청 로직 ) - Python

 **ㅡ> 확장성과 유지보수성 향상**

<br>

#### 장고 프레임 워크 : **MTV(Model Template View)**

* Model : 데이터베이스에 저장되는 데이터의 영역
* Template(View) : 사용자에게 보여지는 영역
* View(Controller) : 프로그램 로직이 동작하여 적절한 처리 결과를 Template에게 전달하는 역할

<br>

#### 장고의 처리 흐름

![Django_flow](https://github.com/HWANG593/Web_programming/blob/master/images/Django_flow.png?raw=true)

* 웹 클라이언트의 요청을 받아 장고에서 MTV 모델에 따라 처리하는 과정이다
  * 클라이언트로부터 요청을 받으면 URLconf 모듈을 이용하여 URL을 분석한다.
  * URL 분석 결과를 통해 해당 URL에 매칭되는 뷰들을 실행한다.
  * 뷰는 자신의 로직을 실행하고, 데이터베이스 처리가 필요하면 모델을 통해 처리하고 그 결과를 반환 받는다.
  * 뷰는 자신의 로직 처리가 끝나면 템플릿을 사용하여 클라이언트에게 전송할 HTML 파일을 생성한다.
  * 뷰는 최종 결과로 HTML 파일을 클라이언트에게 보내 응답한다.

<br>

#### 장고 개발환경 구축 (가상 환경)

* **가상환경은 하나의 PC에서 프로젝트 별로 독립된 파이썬 실행 환경(runtime/interpreter)을 사용할 수 있도록 해준다.**

* 가상 환경을 사용하지 않으면 패키지의 버전 충동을 일으킬 소지가 생기기 때문에, 가상 환경을 구성하여 사용하는 것이 권장된다.

<br>

### HttpRequest와 HttpResponse

>장고는 request와 response 객체로 서버와 클라이언트가 정보를 주고 받는다.
>
>이를 위해 장고는 django.http 모듈에서 HttpRequest와 HttpResponse API를 제공한다.

<br>

#### 서버 - 클라이언트 통신 절차

* 특정 페이지가 요청(request)되면, 장고는 요청 시 메타데이터(여러 다양한 정보)를 포함하는 HttpRequest 객체를 생성
* 장고는 urls.py에서 정의한 특정 View 함수에 첫 번째 인자로 해당 객체(request)를 전달
* 해당 View는 결과값을 HttpResponse 혹은 JsonResponse 객체에 담아 전달

<br>

#### HttpRequest 객체

* 주요 속성(Attribute)
  * HttpRequest.body	    :	request의 body 객체
  * HttpRequest.headers   :	request의 headers 객체
  * HttpRequest.COOKIES  :	모든 쿠키를 담고 있는 딕셔너리 객체
  * HttpRequest.method	:	request의 메소드 타입
  * HttpRequest.GET		   :	GET 파라미터를 담고 있는 딕셔너리 같은 객체
  * HttpRequest.POST		 :	POST 파라미터를 담고 있는 딕셔너리 같은 객체	

<br>

* 주요 메소드(Methods)
  * HttpRequest.read
  * HttpRequest.get_host()
  * HttpRequest.get_port()

<br>

#### HttpResponse 객체

> HttpResponse(data, content_type) 
>
> response를 반환하는 가장 기본적인 함수로서 주로 html을 반환

* string 전달하기
  * HttpResponse("Here's the text of the Web page.")

<br>

* html 태그 전달하기
  * response = HttpResponse()
  * response.write("\<p>Here's the text of the Web page.\</p>")

<br>

#### HttpRedirect

>별다른 response를 하지는 않고, 지정된 URL페이지로 redirect 함
>
>첫번째 인자로 URL을 반드시 지정해야 하며, 경로는 절대경로 혹은 상대경로를 이용할 수 있다.

<br>

#### Render

* render(request(필수), template_name(필수), context=None, content_type=None, status=None, using=None)
* render는 HttpResponse 객체를 반환하는 함수로 template를 context와 엮어 HttpResponse로 쉽게 반환해주는 함수이다.
* template_name에는 불러오고 싶은 템플릿명을 적는다
* **context에는 View에서 사용하던 변수(dictionary 자료형)를 html 템플릿에서 전달하는 역할**을 함
* key 값이 템플릿에서 사용할 변수이름, value값이 파이썬 변수 값이된다.

<br>

#### views.py

```django
from django.shortcuts import render

def my_view(request):
	name = 'joey'
	return render(request,'app/index.html',{'name':name})
```

<br>

#### JsonResponse



<br>

<br>

### Django 템플릿

>Django의 템플릿 언어를 사용하면 강력함과 편리함으로 인해 작업을 수월하게 할 수 있다.
>
>변수, 필터, 태그, 주석 등 4가지 기능을 제공한다.
>
>**템플릿 변수 : {{ 변수명 }} - 값표현  			템플릿 태그(로직) : {% 로직 %} - 로직 구현**

<br>

#### 템플릿 변수

* 템플릿 변수를 사용하면 뷰에서 템플릿으로 객체를 전달할 수 있다. 
* {{ 변수 }}와 같이 사용한다.
* ```점(.)```은 변수의 속성에 접근할 때 사용한다.
* {{ section.title }} : 뷰에서 보내온 section 객체의 title 속성을 출력한다.
* 변수명으로 데이터 값 추출이 안되는 경우에는 공백으로 처리된다.

<br>

#### 템플릿 필터

* 변수의 값을 특정 형식으로 변환할 때 사용한다.
* 변수 다음에 **파이프( | )**를 넣은 다음 적용하고자 하는 필터를 명시한다.
* 여러 개의 필터를 연속적으로 사용할 수 있다.  ex) {{ text | escape | linebreaks}}
* 텍스트 컨텐츠를 escape한 다음, 행 바꿈을 \<p> 태그로 바꾸기 위해 사용

<br>

* 몇몇 필터는 ```(:)```문자를 통해 인자를 취한다.
* 필터 인자는 {{bio | truncatewords : 30 }}과 같이 사용하는데, bio 변수의 처음 30단어를 보여준다.
* 필터 인자에 공백이 포함된 경우에는 반드시 따옴표로 묶는다.
* 장고는 30개 정도의 내장 템플릿 필터를 제공하는데, 자주 사용되는 템플릿 필터는 다음과 같다.

<br>

* defalut
  * 변수가 false 또는 비어있는 경우, 지정된 default를 사용한다.
  * {{ value|default : 'nothing' }}
  * value가 제공되지 않았거나 비어있는 경우, 위에서는 'nothing'을 출력한다.

<br>

* length
  * 값의 길이를 반환한다. 문자열과 목록에 대하여 사용할 수 있다.
  * {{ value|length }}
  * value가 ['a','b','c','d']라면, 결과는 4가 된다.

<br>

* upper
  * 값을 대문자 형식으로 변환한다.
  * {{ story.headline|upper }}
  * story.headline의 값을 대문자 형식으로 변환한다.

<br>

#### 템플릿 태그

> HTML 자체는 로직을 구현할 수 없지만, 템플릿 태그를 사용하면 if문, for문 사용이 가능하다.
>
> **{% tag %} 또는 {% tag %}...contents...{% endtag %}**

<br>

* {% csrf_token %}

  * 사이트 간 요청 위조(또는 크로스 사이트 요청 위조) Cross-site request forgery는 웹사이트 취약점 공격의 하나로, 사용자가 자신의 의지와는 무관하게 공격자가 의도한 행위(수정, 삭제, 등록 등)를 특정 웹사이트에 요청하게 하는 공격을 말한다.
  * 문제를 해결하기 위해선 changepassword 페이지의 form 전달 값에 특정한 값을 추가하면 된다. 예를 들어 사용자로 부터 captcha 값을 입력받게 하여, 정상적인 페이지에서의 요청인지 확인하면 되는것이다. 
  * Django에서는 crsf token을 발행하여 간단하게 처리한다.

<br>

* for
  * 배열의 각 원소에 대하여 반복처리

```django
<ul>
{% for student in student_list %}
	<li>{{student.name}}</li>
{% endfor %}
</ul>
```

<br>

* if/else
  * 변수가 true이면 블록의 컨텐츠를 표시, if 태그 내에 템플릿 필터 및 각종 연산자를 사용할수 있다

```django
{% if student_list %}
	총 학생 수 : {{student_list|length}}
{% else %}
	학생이 없어요!
{% endif %}
```

<br>

* block 및 extends
  * 중복되는 html 파일 내용을 반복해서 작성해야 하는 번거로움을 줄여준다.

```django
{% extends "base_generic.html" %}
{% block title %}{{section.title}}{% endblock %}
{% block content %}
	<h1>{{section.title}}</h1>
	
	{% for story in story_list %}
		<h2>
			<a href="{{story.get_absolute_url}}">
				{{story.headline|upper}}
			</a>
		</h2>
		<p>{{story.tease|truncatewords:"100"}}</p>
	{% endfor %}
{% endblock %}
```

<br>

#### 템플릿 코멘트

> HTML 문서 상에서 주석이 필요할 때 사용하며 장고에서는 두 가지 형식의 코멘트를 제공한다.

* 한 줄 {# 주석내용 #} - 개행 허용되지 않음
* 여러 줄 {% comment %}    주석내용    {% endcomment %}

<br>

### Query 문자열

> HTTP Client가 HTTP Server 요청시 서버에서 요청하려는 대상의 URI가 전달되는데 
>
> 이 때 함께 전달될 수 있는 문자열이다.

#### Query

* name = value 형식으로 구성되어야 한다.
* 여러개의 name = value가 사용될 때는 & 기호로 구분되게 구성해야 한다.
* 영문과 숫자는 그대로 전달되지만 한글과 특수문자들은 %기호와 16진수 코드값으로 전달된다(UTF-8)
* 공백문자는 + 기호 또는 %2C로 전달된다.
* Query 문자열을 가지고 HTTP Server에게 정보를 요청할 때에는 두 가지 방식이 있다.
  * GET 방식 : Query문자열이 외부에 보여진다. 요청 URL 뒤에 (?) 기호와 함께 전달된다.
  * POST 방식 : Query문자열이 외부에 보여지지 않는다. Query 문자열의 길이에 제한이 없다.

https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=ABCabc+123%EA%B0%80%EB%82%98%EB%8B%A4

* ? 뒤부터 Query 한글은 3바이트

<br>

#### 장고 강의교안 1 (가상환경부터 리뷰하면서 설명)

* `127.0.0.1` : 모든 컴터에서 자기 컴터 도메인 의미함
  * = localhost 의미함
* 장고 프로그래밍에서 가상환경 만드는건 필수는 아님.
  * 테마(데이터 분석, 웹 서버)에 맞게 가상환경을 만들고, 이에 맞춰 추가 API 설치하는 것이 일반적 
* 경로 탐색에서 `cd \` 처럼 백슬래쉬부터 시작하면 최상위부터 경로 탐색을 시작한다는 의미

* 장고 프로젝트 생성: `cd 명령어 두번` -> `activate` -> DJANGOexam으로디렉토리 이동

 -> `django-admin startproject 프로젝트 이름`

* `settings.py` : 장고 프로그래밍에서 일어나는 환경설정하는 파일
* `urls.py`: urlpatterns에서 path 설정

#### secondapp 코드 설명

* HttpRequest: HTTP 프로토콜기반으로 요청이 왔을 때 요청 관련 정보를 제공하는 객체, **요청 처리**

  * 뷰함수가 호출될 때 아규먼트로 전달된다. (장고 서버가 객체를 생성)

* HttpResponse: HTTP 프로토콜기반으로 온 요청에 대한 응답시 사용하는 객체, **응답 처리**

  * 응답 내용을 담는다. (HTML 태그문자열, 템플릿을 사용한 랜더 객체)

* 템플릿 변수: {{ 변수명 }} => 값 표현

  * 변수는 뷰가 넘겨준 딕셔너리의 key 이름임
  * 꼭 딕셔너리로 전달해야 함

* 템플릿 태그(로직): {% 로직 %} => 로직 구현 

  * 화면에 영향은 없으나 post일때는 토큰이 있어야됨. -> 보안때문에 

* `<a>` 태그로 요청하는건 무조건 get 방식임

* get 방식: URL 직접 입력할 때, 하이퍼링크 요청할 때,  form태그의 method 속성 get일 때

* post 방식: form태그의 method 속성 post일 때

<br>

#### Tip

* URL을 입력해서 요청하는건 GET방식
* View의 def에서 정의된 딕셔너리 키값 (''안에 있는 애들)을 html에서 {{ }}안에 담아서 사용한다
* \<P> p태그는 paragraph











