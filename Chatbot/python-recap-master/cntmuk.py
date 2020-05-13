def solution(food_times, k):
    answer = 0
    a = 0
    while k > 0:
        for idx,i in enumerate(food_times):
            if i > 0:
                food_times[idx] = i-1
                
            
            else:
                pass
            k -= 1
            print(food_times,i,k,idx)
    answer = a    
    return answer

solution([3, 1, 2],5)