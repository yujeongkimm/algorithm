def solution(ingredient):
    answer = 0
    ingredient_stack = []
    for i in ingredient:
        ingredient_stack.append(i)
        if ingredient_stack[-4:]==[1,2,3,1]:
            del ingredient_stack[-4:]
            answer+=1
            
    return answer