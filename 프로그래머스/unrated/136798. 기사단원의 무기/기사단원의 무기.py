def divisor_num(number):
    sum=0
    for i in range(1, int(number**0.5)+1 ):
        if number%i==0:
            sum+=2
        if number/i==i:
            sum-=1
    return sum

def solution(number, limit, power):
    answer = 0
    divisor_list = [] 
    for n in range(1, number+1):
        divisor_list.append(divisor_num(n))
    for n in divisor_list:
        if n>limit:
            answer+=power
        else:
            answer+=n
    return answer