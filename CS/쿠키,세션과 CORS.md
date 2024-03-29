# 브라우저 저장 공간

모두 도메인 단위이고, 브라우저 저장 공간이다.

### 쿠키

##### 장점

- 만료일자를 지정할 수 있어 데이터 저장 기간을 설정할 수 있다.

##### 단점

- 쿠키를 설정하면 이후 모든 웹 요청은 쿠키 정보를 포함하여 서버로 전송되기 때문에 트래픽 비용이 크다.
- 쿠키는 개수와 용량의 제한이 있음

### Web Storage

##### 장점

- 저장된 데이터가 클라이언트에 존재할 뿐 서버로 전송은 이루어지지 않는다.
  데이터를 선별해서 전송할 수 있기 때문에 네트워크 트래픽 비용을 줄여준다.
- 갯수의 제한이 없고, 쿠키에 비해 큰 용량을 가진다.

##### 단점

- 저장 기간을 설정할 수 없다.

##### Local

- 직접 삭제하지 않는 한 영구 저장된다.

##### Session

- 세션기간(탭이 열린동안) 내에서만 지속 가능하다.
- 탭마다 session Storage는 따로 배정이 되며, 서로의 영역을 공유하지 않는다.



# 쿠키 / 세션

### 쿠키와 세션을 왜 쓸까?

http는 항상 연결되어있는 것이 아닌 필요할 때마다 요청을 보내고, 응답을 받는 비연결성(Connectionless)이라는 특징을 가진다.

이는 클라이언트가 응답을 받으면 서버는 접속을 끊는다는 것인데, 연결이 끝나면 상태 정보가 유지되지 않는 특성이 있다.

>  로그인을 한 뒤, 다른 도메인으로 이동했다가 기존 사이트로 돌아오면 로그인 정보가 유지되지 않는다는 것.

이렇게 유지되지 않는 로그인 정보를 유지하기 위한 방법이 **쿠키와 세션**이다.

### 쿠키

HTTP의 일종으로 사용자가 어떤 웹 사이트를 방문할 경우, 그 사이트가 사용하고 있는 서버에서 **사용자의 컴퓨터에 저장하는 작은 기록 정보 파일**이다.

HTTP에서 클라이언트의 상태 정보를 클라이언트의 PC에 저장하였다가, **필요 시 정보를 참조하거나 재사용**한다.

##### 특징

- **이름, 값, 만료일(저장 기간 설정), 경로 정보**로 구성
- 클라이언트에 총 300개의 쿠키를 저장할 수 있다.
- 하나의 도메인 당 20개의 쿠키를 저장할 수 있다.
- 하나의 쿠키는 4KB(=4096byte)까지 저장 가능

##### 동작 순서

1. 클라이언트가 페이지를 요청한다.(사용자가 웹사이트에 접근)
2. 웹 서버는 쿠키를 생성한다.
3. 생성한 쿠키에 정보를 담아 HTTP 화면을 돌려줄 때, 같이 클라이언트에게 돌려준다.
4. 넘겨받은 쿠키는 클라이언트가 가지고 있다가(로컬 PC에 저장) 다시 서버에 요청할 때 요청과 함께 쿠키를 전송한다.
5. 동일 사이트 재 방문 시 클라이언트의 PC에 해당 쿠키가 있는 경우, 요청 페이지와 함께 쿠키를 전송한다.

##### 사용 예시

1. 방문 사이트에서 로그인 시, "아이디와 비밀번호를 저장하시겠습니까?"
2. 팝업창을 통해 "오늘 이 창을 다시 보지 않기" 체크

##### 약점

1. 쿠키의 특징으로는 클라이언트(브라우저)단에 저장된다는 것이다.

2. 즉, 보안에 약할 수 있다.

3. 쿠키를 훔쳐서 계정 접근 권한 등을 탈취하여 유저의 정보를 악용할 수 있다.

   > document.cookie를 통해 쿠키 스토리지에 저장된 사용자 권한이 있는 쿠키에 접근



### 세션

HTTP 세션이란 **클라이언트가 웹 서버에 연결된 순간부터 웹 브라우저를 닫아 서버와의 HTTP 통신을 끝낼 때 까지의 기간**이다.

하지만 보통 세션이라고 말할 때에는 **서버에 세션에 대한 정보(세션 상태, 클라이언트 상태, 세션 데이터 등)를 저장해놓고 세션 쿠키(고유한 세션 ID값)를 클라이언트에게 주어 서버가 클라이언트를 식별할 수 있도록 하는 방식자체를 의미**하는 경우가 많다.

-> 일정 시간(웹 브라우저를 통해 웹 서버에 접속한 시점~웹 브라우저를 종료하여 연결을 끝내는 시점)동안 같은 사용자(브라우저)로부터 들어오는 일련의 요구를 하나의 상태로 보고, 그 상태를 유지시키는 기술

-> 즉, 방문자가 웹 서버에 접속해 있는 상태를 하나의 단위로 보고 그것을 세션이라고 한다.

##### 특징

- 웹 서버에 **웹 컨테이너의 상태를 유지하기 위한 정보를 저장**한다.

- **저장 데이터에 제한이 없다**(서버 용량이 허용하는 한에서)
- 서버에 세션 객체를 생성하며, **각 클라이언트마다 고유한 세션 ID값**을 부여한다. 세션 ID로 클라이언트를 구분하여 각 요구에 맞는 서비스를 제공한다.
- 쿠키를 사용하여 세션 ID값을 클라이언트에 보낸다
- 웹 브라우저가 종료되거나, 서버에서 세션을 삭제 했을 때만 삭제가 되므로, **쿠키보다 비교적 보안이 좋다**.

##### 동작 순서

1. 클라이언트가 페이지에 요청한다. (사용자가 웹사이트에 접근)
2. 서버는 접근한 클라이언트의 Request-Header 필드인 Cookie를 확인하여, 클라이언트가 해당 session-id를 보냈는지 확인한다.
3. session-id가 존재하지 않는다면, 서버는 session-id를 생성해 클라이언트에게 돌려준다.
4. 서버에서 클라이언트로 돌려준 session-id를 쿠키를 사용하여 서버에 저장한다.
5. 클라이언트는 재 접속 시, 이 쿠키를 이용해 session-id값을 서버에 전달한다.
6. 서버는 받은 session-id로 클라이언트 정보를 가져와 활용한다.

##### 사용 예시

- 화면을 이동해도 로그인이 풀리지 않고 로그아웃하기 전까지 유지



### 쿠키와 세션의 차이?

쿠키와 세션은 비슷한 역할을 하며, 동작 원리도 비슷하다. 그 이유는 **세션도 결국 쿠키를 사용**하기 때문.

- 큰 차이점은 **사용자의 정보가 저장되는 위치**이다. 
  **쿠키는 서버의 자원을 전혀 사용하지 않으며**, **세션은 서버의 자원을 사용**한다.

- **보안면에서는 세션이 더 우수**
  **쿠키는 클라이언트 로컬에 저장되기 때문에 변질되거나 request에서 스니핑 당할 우려가 있어 보안에 취약**하지만,
  세션은 **쿠키를 이용해서 session-id만 저장**하고 그것으로 구분하여 **서버에서 처리하기 때문에 비교적 보안성이 높다**.

- **라이프 사이클**은 **쿠키도 만료기간이 있지만, 파일로 저장되기 때문에 브라우저를 종료해도 정보가 유지**될 수 있다. 또한 **만료기간을 따로 지정해 쿠키를 삭제할 때까지 유지**할 수도 있다.
  반면 **세션**도 만료기간을 정할 수 있지만, **브라우저가 종료되면 만료기간에 상관없이 삭제**된다.

- **속도면에서 쿠키가 더 우수**
  쿠키는 쿠키에 정보가 있기 때문에 서버에 요청 시 속도가 빠르고
  세션은 정보가 서버에 있기 때문에 처리가 요구되어 비교적 느린 속도를 낸다.

보통 쿠키와 세션의 차이에 대해서 저장 위치와 보안에 대해서는 잘 알고 있지만, 사실 가장 중요한 것은 라이프 사이클.

### 세션을 사용하면 좋은데 왜 쿠키 사용?

세션이 쿠키에 비해 보안이 높은 편이나, 
세션은 서버에 저장되고, 서버의 자원을 사용하기에 서버 자원에 한계가 있고, 속도가 느려질 수 있기 때문에 
자원관리 차원에서 쿠키와 세션을 적절한 요소 및 기능에 병행 사용하여 **서버 자원의 낭비를 방지하며 웹 사이트의 속도를 높일 수 있다.**



# CORS

Cross-Origin-Resource-Sharing, 교차 출처 공유

원래 보안상의 이유로 기본적으로 브라우저는 도메인이 다른 서버의 리소스를 받는 것을 제안한다.(SOP)

하지만 요즘에는 클라이언트에서 도메인이 다른 서버에서 제공하는 API를 사용하는 일이 많아졌다.

그렇기에 요청 도메인이 서버에 등록된 도메인이라면, 다른 도메인의 서버에서도 응답을 받을 수 있도록 해주는 정책인 CORS가 등장했다.

Origin은 1. scheme, 2. host, 3. port로 이루어진 도메인을 의미한다(IE의 경우 port를 비교하지 않음)

```
https://www.naver.com

1. scheme : https
2. host : www.naver.com
3. port : null (공개되지 않음)
```



현재 `자신이 속한 출처(Origin)`를 기준으로 `다른 출처(Origin)`에 API를 요청하게 되면 브라우저에서 이 요청으로 넘어오는 경과가 안전한지 판단하게 되는데,

응답을 보내는 출처가 `자신이 속한 출처` 가 아닌 `다른 출처`여도 서로 예상되는 출처라면 요청에 대해 허용해주는 응답 헤더를 보내, 브라우저가 응답 결과를 보여준다.

이를 CORS라고 한다.

##### 왜 브라우저가 CORS요청을 처리할까?

모든 서버들이 다 CORS를 인지하지는 않기 때문.

결과적으로 브라우저는 거부했다고 하더라도, 서버는 처리해버리는 결과가 생길 수 있기 때문에,
서버가 안전하게 요청을 주고 받을 수 있도록 브라우저에서 해당 요청(CORS)를 처리한다.

브라우저에서 출처를 비교한다.

- Simple Request (단순 요청)
  - 조건이 매우 까다로움
- Preflighted Request (사전 요청)
  - 실제 서버 요청 전에 가능한지 options요청으로 먼저 확인하는 것
  - 단순 요청의 조건이 까다롭기 때문에 대부분 사전 요청으로 실행된다.

1. 도메인이 다른 서버에 요청할 경우 헤더의 Origin속성의 나의 도메인도 같이 보내야한다. (브라우저가 자동으로 해준다)
2. 서버에서도 해당 도메인이 허용된 것이라면, **응답값에 Access-Control-Allow-Origin에 해당 도메인을 같이 보내준다**.
3. 응답을 받은 브라우저는 Access-Control-Allow-Origin 헤더가 탭의 출처와 일치하는지 확인한다. Access-Control-Allow-Origin 값이 정확히 출처와 일치하거나, '*' 와일드 카드 연산자를 포함하는 경우 검사가 통과된다.

##### 실제 요청에서 어떻게 처리할까?

CORS는 다른 Origin에 대한 요청을 허용하는 정책이다.

같은 Origin에서 http통신을 하는 경우 알아서 cookie가 request header에 들어가지만, 교차 출처로 요청하는 상황에서는 그렇지 않다.

Origin이 다른 http통신에서는 request header에 쿠키가 자동으로 들어가지 않기 때문에 서버에게 또는 클라이언트에게 내가 어떤 요청을 보내는 지 알려줄 필요가 있다.

```
프론트 > WithCredentials: true
서버 > Access-Control-Allow-Credentials: true
```



> **CORS를 겪고 직접 해결해 본 경험?**
>
> 1. 서버 개발자와 빠르게 소통한다
>
> 만약 프론트에서 CORS관련 설정이 다 끝난 이후에 HTTP요청을 보냈을 때 CORS 오류가 뜰 경우 해당 오류를 캡쳐해서 같이 확인해 보는 방법
>
> 먼저 프론트에서 응답 헤더에 제대로 된 정보를 넣었는 지 확신을 가지는 것이 중요(credentials 관련 설정을 했는지?)
>
> 2. 개발 환경에 프록시 설정을 해둔다.
>
> 만약 개발 환경에 있어서 세팅을 잘 해놓은 상태이고 서버의 세팅이 완벽함에도 문제가 생긴다면, 개발 환경에서의 프록시 설정도 대안이 될 수 있다.
>
> 해당 프록시 설정은 환경에 따라 (CRA면 CRA) 방법이 다르므로 확인해보고 넣으면 된다.

