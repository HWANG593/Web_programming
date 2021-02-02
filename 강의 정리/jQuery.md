## jQuery

#### jQuery란?

>HTML 문서 안의 스크립트 코드를 단수화하도록 설계된 자바스크립트 라이브러리이다.
>
>웹 브라우저마다 다르게 작성해야 되는 자바스크립트 코드를 **jQuery**라이브러리를 사용하여 최대한 쉽게 작성할 수 있도록 지원하는 것을 목표로 한다.

* 기능
  * DOM 요소 선택, 탐색 및 수정
  * CSS 셀렉터에 기반한 DOM 조작
  * 특수효과 및 애니메이션
  * AJAX
  * JSON 파싱

<br>

#### jQuery 라이브러리 사용

>  코드 안의 jQuery()함수는 식별이 어렵고 불편하기 때문에 ```$()```로 표시한다

* jQuery 라이브러리 선언
  * jQuery 라이브러리를 포함하는 <script> 태그를 작성한다.
  * \<script src = "http://code.jquery.com/jquery-xxx.js">\</script>

<br>

* jQuery에서 제공되는 메서드들은 두 가지 방식으로 호출된다.
  * jQuery(자바스크립트객체).xxx()
  * jQuery.xxx()

<br>

* jQuery() 함수의 주요 아규먼트
  * jQuery( selector [,context])
  * jQuery( element )
  * jQuery( elementArray )
  * jQuery( object )
  * jQuery( selection )
  * jQuery()
  * jQuery( html [, ownerDocument] )
  * jQuery( html, attributes )
  * jQuery( callback )

<br>

* $() 사용 예시

  * $('h1') : 모든 h1태그를 찾아서 jQuery로 포장한다.

  * $('CSS선택자').xxxx()
    
    * $('button').click(함수)
  * $(함수) : 로드 이번트 발생시 호출될 함수 등록 ( == $(document.onload(함수))
  * $.xxxx() : jQuery 객체가 제공하는 클래스 메서드
* $('HTML 태그 문자열')
  
  * $('CSS선택자',context().xxxx())
  
    ​						DOM객체					이렇게 주면 context()는 전체에서 찾는다.

<br>

#### API

* jQuery는 API사용 방법이 일관성이 있어 API를 익히기 쉽다,
  * html() : innerHTML     - 변수는 만들어지지만 첫번째 DOM 객체만 출력
  * text() : textContent     - 모든 DOM 객체 출력
  * val() : value                  - 변수는 만들어지지만 첫번째 DOM 객체만 출력

<br>

| $    | getter()                | setter(str)                                 | setter(함수)                  | setter(객체)         |
| ---- | ----------------------- | ------------------------------------------- | ----------------------------- | -------------------- |
| html | html()                  | html("...")                                 | html(함수)                    |                      |
| text | text()                  | text("...")                                 | text(함수)                    |                      |
| val  | val()                   | val("...")                                  | val(함수)                     |                      |
| css  | css("CSS속성명")        | css("CSS속성명", "CSS 속성값)"              | css("CSS속성명", 함수)        | css(JavaScript객체)  |
| attr | attr("HTML태그 속성명") | attr("HTML태그 속성명", "HTML 태그 속성값") | attr("HTML태그 속성명", 함수) | attr(JavaScript객체) |

* **setter(함수)** 사용시 첫번째 아규먼트에는 **index**, 두번째 아규먼트에는 **해당 태그의 content**가 들어간다.
* index는 찾아진 DOM객체 들의 순서대로 0부터 값을 가진다.
* getter는 첫번째에 대해서만 꺼내진다.

<br>

#### jQuery 이벤트 핸들러

* $('...').on('이벤트이름',함수)

  $('...').on(자바스크립트 객체,함수)

  $('...').off() 이벤트핸들러를 해제

<br>

* $('...').이벤트이름(함수)

  * 제공하고 있는것 ex) click, mouseover 등등

