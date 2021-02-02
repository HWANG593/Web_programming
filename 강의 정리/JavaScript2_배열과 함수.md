### 3. 배열

> 파이썬의 리스트와 비슷하다.
>
> 묶을 수 있는 데이터의 갯수에 제한이 없고, 데이터 타입도 제한이 없다.
>
> 자바스크립트의 배열도 객체로 취급된다.

<br>

#### 배열 생성 방법

* 배열 리터럴 방법
  * [1,2,3,4,5]
  * ['aaa', 100, true, 3.4]
  * \[ ] : element가 없는 배열
  * [,,,,,,,] : 방은 지정했지만 값은 없다. 즉, undefined가 여러개 출력됌

<br>

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

<br>

#### 배열 사용 방법

* 배열의 크기 : 배열을 구성하는 엘리먼트의 갯수
  * 배열객체의 length라는 속성(변수)의 값을 사용한다.

<br>

* 배열의 요소(원소, 엘리먼트)를 접근 (L-value, R-value 모두 가능)
  * [0부터 시작하는 인덱스]

<br>

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

<br>

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

<br>

#### 함수의 아규먼트 활용

* 함수의 호출과 인수
  * 함수 호출 시 매개변수와 리턴 값의 존재여부에 따라 다양한 형식으로 호출이 가능하다
  * JavaScript에서는 메서드 호출 시 아규먼트 개수와 함수 정의 시 선언된 매개변수 개수의 일치를 체크하지 않는다.
  * 매개변수에 아규먼트를 전달하지 않으면 변수의 값은 **undefined**가된다.
  * 매개변수보다 더 많은 인수가 전달된 경우 **arguments**라는 함수의 내장변수를 사용한다.

<br>

#### 함수 사용 방법

* 고계(고차) 함수(High-Order Function) : **함수를 데이터로 다루는 함수**
  * Javascript에서는 함수도 데이터 타입의 한 종류이다.
  * 즉, 함수도 다른 수치타입이나 문자열 타입 등과 같이 함수의 인수나 리턴값으로 될 수 있다.
  * 함수 호출 시 인수로 또 다른 함수를 전달할 수 있다.
  * 리턴 값으로 함수를 전달할 수 있다.
