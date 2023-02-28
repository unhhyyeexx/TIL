# DOCTYPE

### DOCTYPE이란?

```javascript
<!--HTML5-->
<!DOCTYPE html>
```

HTML이 어떤 버전으로 작성되었는지 미리 선언해, 웹 브라우저가 내용을 올바로 표시할 수 있도록 해주는 것이다.

쉽게 말하면, **문서 형식을 정의해 주는 것**

### meta태그란?

HTML문서가 어떤 내용을 담고 있고, 키워드는 무엇이며, 누가 만들었는지에 대한 정보를 담고 있는 태그

### meta태그의 요소

##### charset

```html
<mata charset="utf-8" />
```

`charset`요소는 문서에 허용하는 문자 집합에 대해 간단히 표시한다.

`uft-8`은 전세계적인 character집합으로 많은 언어의 문자들을 포함한다.

웹페이지에서 어떤 문자라도 취급할 수 있다는 것을 의미한다.

##### name

`name`요소는 메타 요소가 어떤 정보의 형태를 갖고 있는지 알려준다.

`content`요소는 실제 메타 데이터의 컨텐츠. 머릿말을 요약하는데 유용

```html
<meta name="author" content="Chris Mills" />
    
<meta name="description" content="The MDN Web Docs site provides information about Open Web technologies including HTML, CSS, and APIs for both Web sites and progressive web apps."
```

해당 태그는 실제 MDN 웹 페이지에 등록된 meta 태그의 name 어트리뷰트와 content 어트리뷰트이다

구글에 'MDN'을 검색했을 때, 검색 엔진이 메타 태그의 `content 어트리뷰트`안에 있는 내용을 검색 결과와 함께 추가적으로 보여주고 있다.

### 검색 엔진 최적화를 위해 메타 태그를 어떻게 활용할 수 있을까?

##### 1. 검색엔진을 위한 키워드를 정의한다.

```html
<meta name="keyword" content="HTML, meta, tag, element, reference" />
```

##### 2. 웹 페이지에 대한 설명(description)을 정의한다.

```html
<meta name="description" content="HTML meta tag page" />
```

##### 3. 문서의 저자(author)를 정의한다.

```html
<meta name="author" content="kikiPage" />
```

##### 4. 5초 뒤에 다른 페이지로 리다이렉트(redirect)시킨다.

```html
<meta http-equiv="refresh" content="5;url=http://www.kiki.com" />
```

##### 5. 모든 장치에서 웹 사이트가 잘 보이도록 뷰포트 (viewport)를 설정한다.

```html
<meta name="viewport" content="width=device-width", initial-scale=1.0" />
```

##### 전체코드

```html
<head>
    <meta name="keyword" content="HTML, meta, tag, element, reference" />
    <meta name="description" content="HTML meta tag page" />
    <meta name="author" content="kikiPage" />
    <meta http-equiv="refresh" content="5;url=http://www.kiki.com" />
    <meta name="viewport" content="width=device-width", initial-scale=1.0" />
	<title>HTML meta tag</title>
</head>       
```

