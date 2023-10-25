def solution(genres, plays):
    answer = []
    songs = [] # 장르, 재생수, 인덱스
    dic = {} # 내림차순용

    for i in range(len(genres)):
      songs.append({"genre": genres[i], "play": plays[i], "index": i})

    # 장르, 재생수로 나열
    sorted_by_play = sorted(songs, key=lambda x: (x['genre'], x['play']), reverse=True)

    # 각 장르당 재생수 합을 딕셔너리에 저장
    for i in sorted_by_play:
      if i['genre'] in dic.keys():
        dic[i['genre']] += i['play']
      else:
        dic[i['genre']] = i['play']

    # 재생수 순서대로 내림차순 + 다시 딕셔너리
    sorted_dict = dict(sorted(dic.items(), key= lambda item:item[1], reverse=True))

    # 장르별로 2개씩
    for g in sorted_dict:
      lst = []
      for i in sorted_by_play:
        if i['genre'] == g:
          if len(lst) == 2:
            break
          else:
            lst.append(i['index'])
            answer.append(i['index'])
    return answer