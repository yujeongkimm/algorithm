from itertools import combinations
def is_prime(num):
    flag=False
    if num==1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            flag=True
            break
    return flag

def solution(nums):
    answer = 0
    prime_arr = list(combinations(nums,3))
    for arr in prime_arr:
        if not is_prime(sum(arr)):
            answer+=1
    return answer