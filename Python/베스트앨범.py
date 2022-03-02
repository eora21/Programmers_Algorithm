def solution(genres, plays):
    albums = {}
    for i in range(len(genres)):
        try:
            albums[genres[i]].append([i, plays[i]])
        except:
            albums[genres[i]] = [[i, plays[i]]]

    sorted_albums = sorted(albums.items(), key = lambda item: sum(cnt[1] for cnt in item[1]), reverse=True)

    answer = []
    for play in sorted_albums:
        play[1].sort(key = lambda p: p[1], reverse=True)
        for top_two in play[1][:2]:
            answer.append(top_two[0])

    return answer