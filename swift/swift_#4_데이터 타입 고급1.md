### 데이터 타입 안심

스위프트는 데이터 타입을 안심하고 사용할 수 있는(Type-safe)언어.

타입을 안심하고 사용할 수 있다? 그만큼 실수를 줄일 수 있다.
스위프트는 컴파일 오류로 알려주므로 서로 다른 타입의 값을 할당하는 실수를 줄일 수 있다. 

**타입확인**: 컴파일 시 타입을 확인하는 것



### 타입 추론

스위프트에서는 변수나 상수를 선언할 때 특정 타입을 명시하지 않아도 컴파일러가 할당된 값을 기준으로 변수나 상수의 타입을 결정한다.

```swift
// 타입을 지정하지 않았으나 타입 추론을 통하여 name은 String 타입으로 선언된다.
var name = "Kiki"

//앞서 타입 추론에 의해 name은 String 타입의 변수로 지정되었기에, 정수를 할당하려고 시도하면 오류
name = 100 // 컴파일 에러
```



### 타입 별칭

스위프트에서 기본으로 제공하는 데이터 타입이든, 사용자가 임의로 만든 데이터 타입이든, 이미 존재하는 데이터 타입에 임의로 다른 이름(별칭)을 부여할 수 있다.
그 다음 기본 타입 이름과 이후에 추가한 별칭을 모두 사용 가능

```swift
typealias MyInt = Int
typealias YourInt = Int
typealias MyDouble = Double

let age: MyInt = 100			//MyInt는 Int의 또 다른 이름
var year: YourInt = 2000	//YourInt도 Int의 또 다른 이름

// MyInt도, YourInt도 Int이기 때문에 같은 타입으로 취급.
year = age
let month: Int = 7		// 물론 기존의 Int도 사용 가능
let percentage: MyDouble = 99.9	
```



### 튜플

**튜플(Tuple)**은 타입의 이름이 따로 지정되어 있지 않은, 프로그래머 마음대로 만드는 타입

**'지정된 데이터의 묶음'**이라고 표현할 수 있다.

파이썬의 튜플과 유사. 이름이 따로 없으므로 일정 타입의 나열만으로 튜플 타입을 생성해줄 수 있다.

튜플에 포함될 데이터의 개수는 자유롭게 정할 수 있다.

```swift
//String, Int, Double 타입을 갖는 튜플
var person: (String, Int, Double) = ("Kiki", 100, 170.2)

// 인덱스를 통해서 값을 빼 올 수 있다.
print("이름: \(person.0), 나이: \(person.1), 신장: \(person.2)")

person.1 = 99		// 인덱스를 통해 값을 할당할 수 있다.
```

이름없이 인덱스만으로 각 요소의 데이터가 무엇을 나타내는지 파악하기 어렵다.

아래는 튜플의 요소마다 이름을 붙여본 예시이다.

```swift
//String, Int, Double 타입을 갖는 튜플
var person: (name: String, age: Int, heigth: Double) = ("Kiki", 100, 170.2)

// 요소의 이름과 인덱스를 통해서 값을 빼 올 수 있다.
print("이름: \(person.name), 나이: \(person.1), 신장: \(person.height)")

person.1 = 99		// 인덱스를 통해 값을 할당할 수 있다.
person.height = 160.3		// 요소 이름을 통해서도 값을 할당할 수 있다.
```

타입 이름에 해당하는 키워드가 따로 없어 사용에 불편함을 겪기도 한다.

아래는 타입별칭을 사용하여 튜플의 별칭을 지정해본 예시이다.

```swift
typealias PersonTuple = (name: String, age: Int, height: Double)

let kiki: PersonTuple = ("kiki", 100, 160.4)
let zizi: PersonTuple = ("zizi", 200, 180.7)
```





## 컬렉션형

>  많은 수의 데이터를 묶어서 저장하고 관리할 수 있는 컬렉션 타입
>
> 배열(Array), 딕셔너리(Dictionary), 세트(Set) 등이 있다.



### 배열

배열은 같은 타입의 데이터를 일렬로 나열한 수 순서대로 저장하는 형태의 컬렉션 타입

각기 다른 위치에 같은 값이 들어갈 수 있다.

Let, var 모두 사용 가능.
실제 배열을 사용할 때는 Array라는 키워드와 타입 이름의 조합으로 사용한다.

대괄호로 값을 묶어 표현하기도 한다.

빈 배열은 이니셜라이저 또는 리터럴 문법을 통해 생성해줄 수 있는데, `isEmpty` 프로퍼티로 비어있는 배열인지 확인해볼 수 있다.

배열에 몇 개의 요소가 존재하는지 알고 싶으면 `count`프로퍼티를 확인하면 된다.

```swift
// 대괄호를 사용하여 배열임을 표현
var names: Array<String> = ["kiki", "zizi", "isu", "kiki"]

// 위 선언과 정확히 동일한 표현. [String]은 Array<String>의 축약 표현
var names: [String] = ["kiki", "zizi", "isu", "kiki"]

var emptyArray: [Any] = [Any]()				// Any 데이터를 요소로 갖는 빈 배열을 생성
var emptyArray: [Any] = Array<Any>()	// 위 선언과 정확히 같은 동작을 하는 코드

// 배열의 타입을 정확히 명시해줬다면 []만으로도 빈 배열을 생성할 수 있다.
var emptyArray: [Any] = []
print(emptyArray.isEmpty) 	// true
print(names.count)					// 4
```

배열은 각 요소에 인덱스를 통해 접근할 수 있다. 인덱스는 0부터 시작.

잘못된 인덱스로 접근하려고 하면 익셉션오류(Exception Error)발생.

맨 처음과 맨 마지막 요소는 first, last 프로퍼티를 통해 가져올 수 있다.

`first index(of:)` 메서드를 사용하면 해당 요소의 인덱스를 알아낼 수 있다. 중복된 요소가 있다면 제일 먼저 발견된 요소의 인덱스 반환

`append(_:) `메서드를 이용하면 맨 뒤에 요소 추가

`insert(_:at:) `메서드를 이용하면 중간에 요소 삽입 가능

`remove(_:) `메서드를 이용하면 요소 삭제 가능, 해당 요소가 삭제된 후 반환

```swift
let firstItem: String = names.removeFirst()
let lastItem: String = names.removeLast()
let indexZeroItem: String = names.remove(at:0)

// 인덱스 2에 삽입
names.insert("happy", at:2)
// 인덱스 5의 위치에 kiki와 zizi가 삽입된다.
names.insert(contentsOf: ["kiki", "zizi"], at:5)
```



### 딕셔너리

딕셔너리는 요소들이 순서 없이 키(key)와 값(value)의 쌍으로 구성되는 컬렉션 타입

하나의 딕셔너리 안의 키는 같은 이름을 중복해서 사용할 수 없음. 유일한 식별자

`Dictionary`라는 키워드와 키의 타입과 값의 타입 이름의 조합으로 사용

대괄호로 키와 값의 타입 이름의 쌍을 묶어 딕셔너리 타입임을 표현

```swift
// typealias를 통해 조금 더 단순하게 표현해볼 수도 있음
typealias StringDictionary = [String: Int]

// 키는 String, 값은 Int타입인 빈 딕셔너리 생성
var numberForName: Dictionary<String, Int> = Dictionary<String, Int>()

// 위 선언과 같은 표현
var numberForName: [String: Int] = [String: Int]()

// 위 코드와 같은 동작
var numberForName: StringintDictionary = StringIntDictionary()

// 딕셔너리의 키와 값 타입을 정확히 명시해줬다면 [:]만으로도 빈 딕셔너리 생성 가능
var numberForName: [String: Int] = [:]
```

딕셔너리는 각 값에 키로 접근. 키는 유일해야하며, 값은 유일하지 않아도 된다.

딕셔너리는 배열과 다르게 딕셔너리 내부에 없는 키로 접근해도 오류가 발생하지 않는다. 다만 nil반환

특정 키에 해당하는 값을 제거하려면 `removeValue(forKey:)`	메서드 사용 , 키에 해당하는 값이 제거된 후 반환된다.



### 세트

세트는 같은 타입의 데이터를 순서 없이 하나의 묶음으로 젖아하는 형태의 컬렉션 타입.

세트 내의 값은 모두 유일한 값, 중복된 값이 존재하지 않는다. 그래서 세트는, 보통 **순서가 중요하지 않거나, 각 요소가 유일한 값이어야 하는 경우**에 사용.

세트의 요소로는 해시 가능한(Hashable, 스위프트의 기본 자료형은 모두 해시가능) 값이 들어와야 한다.

축약형 없음.

```swift
var naems: Set<String> = Set<String>()		// 빈 세트 생성
var naems: Set<String> = []		// 빈 세트 생성

// Array와 마찬가지로 대괄호 사용
var names: Set<String> = ["kiki", "zizi", "kiki"]
// 그렇기 때문에 타입 추론을 사용하게 되면 컴파일러는 Set이 아닌 Array로 타입을 지정한다.
var numbers = [100,200,300]
print(type(of: numbers)) // Array<Int>

print(names.count) // 2 : 중복된 값은 허용되지 않아 kiki가 하나만 남음
```

`insert(_:)` : 요소 추가, ` remove(_:) ` : 요소 삭제

- 집합연산

```swift
let english: Set<String> = ["kiki", "zizi", "mimi"]
let Korean: Set<String> = ["kiki", "vivi", "titi", "riri", "zizi"]

// 교집합 {"kiki", "zizi"}
let intersectSet: Set<String> = english.intersection(Korean)

// 여집합의 합(배타적 논리합) {"mimi", "vivi", "titi", "riri"}
let symmetricDifferSet: Set<String> = english.symmetricDifference(Korean)

// 합집합 {"kiki", "zizi", "mimi", "vivi", "titi", "riri"}
let unionSet: Set<String> = english.union(Korean)

// 차집합 {"mimi"}
let subtracSet: Set<String> = english.subtracting(korean)
```

- 포함관계 연산

```swift
let bird: Set<String> = ["비둘기", "닭", "기러기"]
let mam: Set<String> = ["사자", "호랑이", "곰"]
let animal: Set<String> = bird.union(mam)

print(bird.isDisjoint(with: mam))			// 서로 배타적인지 -> true
print(bird.isSubset(of: animal))			// 새가 동물의 부분집합인가요 => ture
print(animal.isSuperset(or: mam))			// 동물은 포유류의 전체집합인가요 => true
print(animal.isSuperset(or: bird))		// 동물은 새의 전체집합인가요 => true
```

