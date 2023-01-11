## 콘솔 로그

> 로그 : 애플리케이션의 상태 또는 애플리케이션 내부 로직의 흐름을 관찰할 수 있도록 출력한 정보
>
> Console Log : 디버깅 중 디버깅 콘솔에 보여줄 로그
>
> 스위프트에서는 `print()` 또는 `dump()` 함수를 사용하여 콘솔로그 출력

### Print()

```swift
 public func print(items: Any..., separator: String = default, terminator: String=default)
```

줄바꿈 문자 : \n

- Print()와 dump() 의 차이
  - Print()함수 : 
    - 디버깅 콘솔에 간략한 정보를 출력
    - 출력하려는 인스턴스의 description 프로퍼티에 해당하는 내용을 출력
  - Dump() 함수:
    - 조금 더 자세한 정보 출력
    - 출력하려는 인스턴스의 자세한 내부 콘텐츠까지 출력



### 문자열 보간법

>  String Interpolation

변수 또는 상수 등의 값을 문자열 내에 나타내고 싶을 때 사용

문자열 내에 \\(변수나 상수) 의 형태로 표기하면 이를 문자열로 치환해서 넣는다.

```swift
let name: String = "kiki"
print("My name is \(name)")
```

