# Django2

## Django 프로그래밍

### Django 모델(Model)

* Django에서 Model은 데이터 서비스를 제공한다. 
* Django의 Model은 각 Django App 안에 기본적으로 생성되는 models.py 모듈 안에 정의하게 된다.
* models.py 모듈 안에 하나 이상의 모델 클래스를 정의할 수 있으며, 하나의 모델 클래스는 DB에서 하나의 테이블에 해당된다.

<br>

#### Django Model class

* 모델의 필드는 클래스 속성(Attribute)로 표현되고 테이블의 컬럼에 해당한다.
* Primary Key(기본키)가 지정되지 않으면, 모델에 Primary Key 역할을 하는 ID필드가 자동으로 추가되며 DB 생성시 자동으로 값이 1씩 증가되는 id 컬럼이 생성된다.

```python
class 모델이름(models.Model):
	필드이름1 = models.필드타입(필드옵션)
	필드이름2 = models.필드타입(필드옵션)
```

* 필드를 정의하기 위해 인스턴스 변수가 아닌 **클래스 변수**로 정의하며, **변수에는 테이블의 컬럼의 메타 데이터를 정의**한다.

<br>

#### 필드 타입

| FieldType     | 설명                                                         |
| ------------- | ------------------------------------------------------------ |
| CharField     | 제한된 문자열 필트 타입, 최대 길이를 max_length 옵션에 지정해야 한다. |
| TextField     | 대용량 문자열을 갖는 필드                                    |
| IntegerField  | 32비트 정수형 필드, 정수 사이즈에 따라 BigIntegerField, SmallIntegerField |
| BooleanField  | true/false 필드, Null을 허용하기 위해서는 NullBooleanField를 사용 |
| DataTimeField | 날짜와 시간을 갖는 필드, 날짜만 가질 경우 DateField, 시간만 가질 경우 TimeField를 사용 |
| DecimalField  | 소숫점을 갖는 decimal 필드                                   |
| BinaryField   | 바이너리 데이터를 저장하는 필드                              |
| FileField     | 파일 업로드 필드                                             |
| ImageField    | FileField의 파생클래스로서 이미지 파일인지 체크한다.         |

* 위와 같은 필드 타입 클래스 이외에, Django 프레임워크는 테이블 간 or 필드 간 **관계(Relationship)**을 표현하기 위해 **ForeignKey, ManytoManyField, OneToOneField** 클래스를 제공하고 있다.
* 특히 **ForeignKey**는 모델 클래스 간의 Many-To-One 혹은 One-To-Many 관계를 표현하기 위해 사용된다.

<br>

#### 필드 옵션

* 모델의 필드는 필드 타입에 따라 여러 옵션(혹은 Argument)를 가질 수 있다,
* 예) CharField는 문자열 최대 길이를 의미하는 max_length라는 옵션을 갖는다.
* 필드 옵션은 일반적으로 생성자에서 아규먼트로 지정한다.

| 필드 옵션                      | 설명                                                         |
| ------------------------------ | ------------------------------------------------------------ |
| null(Field.null)               | null=True 이면, Empty 값을 DB에 NULL로 저장한다. DB 테이블에서 Null이 허용되는 필드가 된다. |
| blank(Field.blank)             | blank=Flase이면, Required 필드가 된다. blank=True이면 Optional 필드이다. |
| primary_key(Field.primary_key) | 해당 필드가 Primary Key임을 표시한다.<br />Primary Key로 설정되는 필드가 없으면 id라는 필드가 생성 |
| unique(Field.unique)           | 해당 필드가 테이블에서 Unique함을 표시 해당 컬럼에 대해 Unique Index를 생성한다. |
| default(Field.default)         | 필드의 디폴트 값을 지정한다.                                 |

<br>

#### DB Migration

* Django에서 Model 클래스를 생성하고 난 후, 해당 모델에 상응하는 DB 테이블을 데이터 베이스에서 생성할 수 있다.
* Python 모델 클래스의 수정 및 생성을 DB에 적용하는 과정을 **Migration**이라 한다.
* Django가 기본적으로 제공하는 ORM(Object-Relational-Mapping) 서비스를 통해 진행된다.

<br>

#### ORM (Object Relation Mapping)

* 하나의 모델 클래스는 하나의 데이터베이스 테이블에 해당한다.

<br>

### C.R.U.D. (Create Read Update Delete)

> SQL언어로는 INSERT, SELECT, UPDATE, DELETE
>
> Django는 Django API(Python)으로 작업

#### Django Database

* Django를 통해 Database를 연동 (CRUD)하는 구현 과정
  1. models.py에 모델 클래스를 생성한 후 Model이라는 클래스를 상속한다.
     만드려는 DB테이블의 컬럼 사양에 맞춰서 클래스 변수를 정의한다.
  2. Django에서 제공하는 명령을 수행시켜서 모델 클래스에 알맞는 DB테이블을 생성한다.
  3. 모델 클래스를 통해서 CRUD를 구현한다
     * C(insert) - 모델클래스의 객체를 생성한 후에 save() 메서드 호출
     * R(select) - 모델클래스 .objects.all() ,filter(...), order_by(...), first(), last(), count()
     * U(update) - 행 객체를 얻어 변경할 필드를 수정한 후 save() 메서드 호출
     * D(delete) - 행 객체를 얻은 후 delete() 메서드 호출

<br>

#### TIP

RDBMS에서 테이블 생성 시 컬럼단위로 컬럼명과 타입을 설정

charFeild -> VARCHAR 가변길이

IntegerFeild -> INTEGER 고정길이



Migrate는 모델 클래스를 테이블로 만들 때 쓰는 것

테이블을 만들어 놓은 상황이라면 안해도됌