import sys

#initiate
r = -1
s = list(map(int, input().split()))
num1 = s[0]
num2 = s[1]

# to be num1 >= num2
if num1 < num2:
  tmp = num1
  num1 = num2
  num2 = tmp

#get G.C.M
a = num1
b = num2
while(a % b):
  r = a % b
  a = b
  b = r

#get L.C.M
lcm = num1 * (num2/b)
print(lcm)
