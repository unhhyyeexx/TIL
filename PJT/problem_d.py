import json


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
    # 여기에 코드를 작성합니다.  
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))