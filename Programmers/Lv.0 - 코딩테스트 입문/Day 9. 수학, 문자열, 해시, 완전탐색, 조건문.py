# 1. 개미 군단
def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)
    
# 2. 모스부호 (1)
def solution(letter):
    morse = {
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
    return ''.join([morse[i] for i in letter.split(' ')])
    
# 3. 가위 바위 보
def solution(rsp):
    win = {'0': '5', '2': '0', '5': '2'}
    return ''.join([win.get(i) for i in rsp])
    
# 4. 구슬을 나누는 경우의 수
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def solution(balls, share):
    return factorial(balls)/(factorial(balls-share)*factorial(share))
