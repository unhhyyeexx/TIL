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
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))