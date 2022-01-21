import json
from pprint import pprint


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
    # 여기에 코드를 작성합니다.  
      

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))