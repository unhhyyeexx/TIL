import json
from pprint import pprint


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
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))