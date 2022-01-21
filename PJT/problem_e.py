import json


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
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))