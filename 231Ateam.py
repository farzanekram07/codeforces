import sys
sys.stdin = open("py/input.txt", "r")
sys.stdout = open("py/output.txt", "w")

n = int(input())

count = 0

for i in range(n):
    a,b,c = map(int, input().split())
    if a + b + c >= 2:
        count += 1

print(count)