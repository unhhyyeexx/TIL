## 조건문



### if 구문

if문은 대표적인 조건문으로 if, else 등의 키워드를 사용하여 구현할 수 있다.

정수, 실수 등 0이 아닌 모든 값을 참으로 취급하여 조건 값이 될 수 있었던 다른 언어와는 달리 스위프트의 if문은 조건의 값이 꼭 Bool타입이어야 한다.

`else if `는 몇 개가 이어져도 상관 없고, `else`블록은 없어도 된다.



### switch 구문

기본 문법이라 할 수 있는 `switch` 문은 다른 언어와 비교했을 때 많이 달라진 문법 중 하나이다,

`break`가 선택사항인데, 즉, `case`내부의 코드를 모두 실행하면 break없이도 switch 구문이 종료된다는 뜻.

`break`를 쓰지 않고 case를 연속 실행하던 트릭을 더 이상 사용하지 못한다 

=> swift에서 `switch`구문의 case를 연속 실행하려면 `fallthrough`키워드를 사용한다 

각 `case`에 들어갈 비교 값은 입력 값과 데이터 타입이 같아야 한다.

또, 비교될 값이 명확히 한정적인 값 (열거형 값 등)이 아닐 때는 `default`를 꼭 작성해줘야 한다.

또한 각 `case`에는 범위 연산자를 사용할 수도, `where`절을 사용하여 조건을 확장할 수도 있다.

```swift
switch 입력값 {
  case 비교값1:
  	실행구문
  case 비교값2:
  	실행구문
  	// 이번 case를 마치고 switch구문을 탈출하지 않는다. 아래 case로 넘어감
  	fallthrough
  case 비교값3, 비교값4, 비교값5: // 한 번에 여러 값과 비교 가능
  	실행구문
  	break	// break키워드를 통한 종료는 선택사항
  default:	// 한정된 범위가 명확지 않다면 default는 필수
  	실행구문
}
```

```swift
let integerValue: Int = 5

switch integerValue {
  case 0:
  	print("Value == zero")
  case 1...10:											// 범위를 사용한 case를 만들 수도 이
  	print("Value == 1!10")
  	fallthrough											// fallthrough 키워드를 사용하여 다음 case도 실행된다
  case int.min..<0, 101..<Int.max:
  	print("Value < 0 or Value > 100")
  	break
  default:
  	print("10 < Value <= 100")
}

// result
// Value == 1~10
// Value < 0 or Value > 100
```

- 와일드카드 식별자를 사용한 튜플 switch case구성

```swift
typealias NameAge = (name: String, age: Int)

let tupleValue: NameAge = ("kiki", 99)

switch tupleValue {
  case ("kiki", 50):
  	print("정확히 맞췄습니다!")
  case ("kiki", _):
  	print("이름만 맞았다. 나이는 \(tupleValue.age)이다")
  case (_, 99):
  	print("나이만 맞았다. 이름은 \(tupleValue.name)이다")
  default:
  	print("누굴 찾나요?")
}

// 이름만 맞았다. 나이는 99이다
```

=> `_`같은 와일드카드 식별자를 사용하면 무시된 값을 직접 가져와야 하는 불편함이 생긴다. 그래서 미리 지정된 조건 값을 제외한 다른 값은 실행문 안으로 가져올 수 있다. 그때 `let`을 붙인 값 바인딩을 사용한다.

```swift
typealias NameAge = (name: String, age: Int)

let tupleValue: NameAge = ("kiki", 99)

switch tupleValue {
  case ("kiki", 50):
  	print("정확히 맞췄습니다!")
  case ("kiki", let age):
  	print("이름만 맞았다. 나이는 \(age)이다")
  case (let name, 99):
  	print("나이만 맞았다. 이름은 \(name)이다")
  default:
  	print("누굴 찾나요?")
}

// 이름만 맞았다. 나이는 99이다
```

`where`키워드를 사용하여 `case`의 조건을 확장할 수 있다.

```swift
let 직급: String = "사원"
let 연차: Int = 1
let 인턴인가: Bool = false

switch 직급 {
  case "사원" where 인턴인가 == true:
  	print("인턴입니다.")
  case "사원" wherer dusck < 2 && 인턴인가 == false:
  	print("신입사원입니다.")
  case "사원" where 연차 > 5:
  	print("연식 좀 된 사원입니다.")
  case "사원":
  	print("사원입니다.")
  case "대리":
  	print("대리입니다.")
  default:
  	print("사장입니까?")
}

// 신입사원입니다.
```



