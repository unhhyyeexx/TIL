# annotation

[TOC]

### annotation?

에너테이션

자바 소스 코드에 추가하는 표식으로, 보통 @ 기호를 앞에 붙여서 사용한다.

다양한 목적으로 사용하지만, 메타 데이터(데이터에 대한 설명을 담고 있는 데이터)의 비중이 가장 크다.





### @Controller와 @RestController 차이

공통점 : Spring에서 컨트롤러를 지정해주기 위한 어노테이션

`@Controller` : 전통적인 Spring MVC의 컨트롤러

`@RestController`: Restful 웹 서비스의 컨트롤러

 주요한 차이점 : HTTP Response Body가 생성되는 방식





### @RequestMapping

- 이 annotation은 클래스와 메서드 수준에서 모두 사용할 수 있다.
- 대부분의 경우 메서드 레벨에서 애플리케이션은 HTTP 메서드 특정 변형 `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, 또는 `PatchMapping` 중 하나를 사용하는 것을 선호한다.





### @GetMapping

HTTP GET 요청을 특정 핸들러 메소드에 맵핑하기 위한 annotation

주소에 파라미터가 노출된다.

`@RequestMapping(method = RequestMethod.GET, path="/test"`) == 

`@GetMapping("/test")`

- `/test`: 메서드와 매핑할 때 스프링부트에서 설정한 경로





### @SpringBootApplication

스프링 부트 사용에 필요한 기본 설정을 해준다.

```java
// SpringBootApplication.java

@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@SpringBootConfiguration // 스프링 부트 관련 설정
@EnableAutoConfiguration // 자동으로 등록된 빈을 읽고 등록
@ComponentScan(excludeFilters = { 
    @Filter(type = FilterType.CUSTOM, 
            // 사용자가 등록한 빈을 읽고 등록
            classes = TypeExcludeFilter.class), 
    @Filter(type = FilterType.CUSTOM, 
            classes = AutoConfigurationExcludeFilter.class) 
})
public @interface SpringBootApplication {
...생략...
}
```

#### @SpringBootConfiguration

- 스프링 부트 관련 설정을 나타내는 애너테이션

- @Configuration을 상속해서 만든 애너테이션

#### @ComponentScan

- 사용자가 등록한 빈을 읽고 등록하는 애너테이션
- @Component라는 애너테이션을 가진 클래스들을 찾아 빈으로 등록하는 역할
- 모든 빈에 @Component를 사용하는 게 아니라 @Component를 감싸는 애너테이션이 있는데 실제 개발을 하면 용도에 따라 다른 애너테이션을 사용한다. 아래는 그런 애너테이션
  - `@Configuration`: 설정 파일 등록
  - `@Repository`: ORM 매핑
  - `@Controller`, `@RestControoler`: 라우터
  - `@Service`: 비즈니스 로직

#### @EnableAutoConfiguration

- 스프링부트에서 자동 구성을 활성화하는 애너테이션
- 스프링 부트 서버가 실행될 때 스프링 부트의 메타 파일을 읽고 정의된 설정들을 자동으로 구성하는 역할 수행



```java
@SpringBootApplication
public class SpringBootDeveloperApplication {
    public static void main(String[] args){
        SpringApplication.run(SpringBootDeveloperApplication.class, args);
    }
}
```

`SpringApplication.run()` 

- 애플리케이션을 실행하는 메서드
- 첫 번째 인수: 스프링 부트 애플리케이션의 메인 클래스로 사용할 클래스를 전달
- 두 번째 인수: 커맨드 라인의 인수들을 전달