# 1. 옷가게 할인 받기
def solution(price):
    if price < 100000:
        return price
    elif price >= 100000 and price < 300000:
        return int(price*0.95)
    elif price >= 300000 and price < 500000:
        return int(price*0.9)
    else:
        return int(price*0.8)
        
# 2. 아이스 아메리카노
def solution(money):
    return [money//5500, money%5500]
    
# 3. 나이 출력
def solution(age):
    return 2022-age+1
    
# 4. 배열 뒤집기
def solution(num_list):
    return num_list[::-1]
