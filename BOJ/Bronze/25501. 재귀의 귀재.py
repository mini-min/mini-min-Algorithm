count = 0

# 힌트로 주어진 코드
def recursion(s, l, r):
    global count
    count += 1
    if l >= r: return 1, l+1
    elif s[l] != s[r]: return 0, l+1
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

num = int(input())
for i in range(num):
  s = input()
  count = 0
  answer = isPalindrome(s)
  print(answer[0], answer[1])
