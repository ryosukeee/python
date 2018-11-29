import sys

r = -1
s = list(map(int, input().split()))
num1 = s[0]
num2 = s[1]

if num1 < num2:
  tmp = num1
  num1 = num2
  num2 = tmp

while(num1 % num2):
  r = num1 % num2
  num1 = num2
  num2 = r

print(num2)
