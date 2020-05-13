def solution(gems):
    answer = []
    cnt = 0
    uniq = list(set(gems))
    if len(uniq) == 1:
        return [1,1]
    for i in gems:
        if i in uniq:
            uniq.remove(i)
        elif i not in uniq:
            cnt += 1
                 
    return answer,cnt

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])