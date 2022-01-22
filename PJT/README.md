## PJT 01

> Python을 활용한 데이터 수집
>
> 커뮤니티 서비스 개발을 위한 데이터 수집 단계로, 전체 데이터 중 필요한 데이터를 추출



### 1. 목표

- Python 기본 문법 실습
- 파일 입출력에 대한 이해
- 데이터 구조에 대한 분석과 이해
- 데이터를 가공하고 JSON 형태로 저장



### 2. 문제

#### A. 제공되는 영화 데이터 주요내용 수집

- **요구사항**
  -  dictionary 형태의 제공된 데이터에서 필요로 하는 정보만 불러오기
  - moive.json파일에 담겨있는 데이터 활용
- **코드**

```python
import json
from pprint import pprint


def movie_info(movie):

    # movie.json 파일에서 원하는 데이터 불러와서 같은 이름의 변수에 저장
    id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')

    # 불러온 데이터를 dictionary result에 담는다
    result = {
        'id' : id ,
        'title' : title ,
        'poster_path' : poster_path,
        'votd_average' : vote_average,
        'overview' : overview,
        'genre_ids' : genre_ids    
    }
    return result
```

- **문제 포인트 및 어려웠던 점**
  - dictionary에서 데이터를 추출 할 수 있는가를 묻는 문제



#### B. 제공되는 영화 데이터의 주요내용 수정

- **요구사항**
  - 제공된 데이터에서 필요로 하는 정보 추출
  - genres.json 파일을 이용하여 genre_ids를 genre_names로 변환하여 dictionary에 추가

- **코드**

```python
def movie_info(movie, genres):
    
    #problem_a 와 같은 방식
    id = movie.get('id')
    title = movie.get('title')
    poster_path = movie.get('poster_path')
    vote_average = movie.get('vote_average')
    overview = movie.get('overview')
    genre_ids = movie.get('genre_ids')

    #genre_ids를 이용하여 genre name 추출
    genre_name = []
    for i in genres:
        if i["id"] == genre_ids[0] or i["id"] == genre_ids[1]:
            genre_name.append(i["name"])

    result = {
        'id' : id ,
        'title' : title ,
        'poster_path' : poster_path,
        'votd_average' : vote_average,
        'overview' : overview,
        'genre_name' : genre_name
    }
    return result
```

- **문제 포인트 및 어려웠던 점**
  - movie 에서 추출한 id로 genre에서 genre_name을 찾아내기
  - 초반에 문제 이해 과정에서 어려움이 있었다.



#### C. 다중 데이터 분석 및 수정

- **요구사항**
  - 이전 문제의 함구 구조 재사용
  - 평점이 높은 20개의 영화데이터의 필요한 정보 출력

- **코드**

```python
def movie_info(movies, genres):

    result = []

    for i in movies:
        result_in = {}

        #movies 파일에서 필요한 정보 추출
        for j in i:
            if j == 'id' or j == 'title' or j == 'poster_path' or j == 'vote_avarage' or j == 'overview':
                result_in[j] = i[j]
        
        #genre 파일에서 필요한 정보 추출
        genre_name = []
        for k in genres:
            for genre in i['genre_ids']:
                if k['id'] == genre:
                    genre_name.append(k['name'])
        result_in['genre_name'] = genre_name
        

        result.append(result_in)

    return result
```

- **문제 포인트 및 어려웠던 점**
  - 문제A와 B를 활용하는 문제
  - 문제A에서 반복문을 활용하지 않아 이 문제에서 다시 반복문으로 바꾸는데서 시간이 걸렸다.
  - for문 안에 for문을 넣고 그 안에 또 for문을 작성하다 보니 변수설정에 있어서 많이 헷갈렸다.



#### D. 알고리즘을 통한 데이터 출력

- **요구사항**
  - movies.json과 movies폴더 내부의 파일들 사용
  - movies 폴더 내부 파일들은 각 영화의 상세정보 포함
  - 반복문을 통해 상세정보 파일 오픈
  - 가장 높은 수익을 낸 영화 출력
- **코드**

```python
def max_revenue(movies):

    #movie들의 id 추출
    ids = []
    for dic in movies:
        id = dic['id']
        ids.append(id)
    
    #추출한 id를 이용하여 각 영화의 수익을 revenue의 원소로 저장
    revenue = []
    for i in ids:
        openfile = open(f'data/movies/{i}.json', encoding='UTF8')
        detail = json.load(openfile)

        revenue.append([detail['revenue'], detail['original_title']])
    
    #가장 큰 revenue비교
    # 해당 revenue의 index를 이용하여 name출력
    max_rev = 0
    max_name = ''
    for i in revenue:
        if i[0] > max_rev:
            max_rev = i[0]
            max_name = i[1]

    return max_name
```

- **문제 포인트 및 어려웠던 점**
  - movies.json파일에서 필요한 데이터를 추출하고, 추출한 데이터를 이용하여 movies폴더 내부 파일 사용
  - 문제를 처음 봤을 때 문제 이해 자체가 어려웠다.
  - openfile을 사용할 때 문자열 중간에 변수를 넣는 문제는 처음 풀어보는 줄 알고 당황했는데, print()함수와 동일하게 formating하여 풀었다.
  - 문제를 잘못 읽고 처음에 revenue의 최댓값만 뽑아냈는데, 이후에 name과 함께 뽑아내는 게 어려웠다. 



#### E. 알고리즘을 통한 데이터 출력

- **요구사항**
  - movies.json과 movies폴더 내부의 파일들 사용
  - movies 폴더 내부 파일들은 각 영화의 상세정보 포함
  - 반복문을 통해 상세정보 파일 오픈
  - 개봉일 정보(release_date)를 이용하여 모든 영화 중 12우러에 개봉한 영화들의 제목 리스트 출력
- **코드**

```python
def dec_movies(movies):

    #각 영화의 id 추출
    ids = []
    for dic in movies:
        id = dic['id']
        ids.append(id)
    
    dec_movie = []
    for i in ids:
        openfile = open(f'data/movies/{i}.json', encoding='UTF8')
        detail = json.load(openfile)

        #12월에 개봉한 영화 골라내기
        if detail['release_date'][5:7] == '12':
            dec_movie.append(detail['original_title'])
    return dec_movie
```

- **문제 포인트 및 어려웠던 점**

  - 특정 조건의 데이터만 골라낼 수 있는가

  - 영화 개봉일이 월만 써져있는게 아니라 연도부터 일까지 써져있어 처음에 당황했다

  - 수업에서 배운 슬라이딩을 이용하여 문자열의 중간값만 뽑아낼 수 있었다.

