import sys
sys.stdin = open("py/input.txt", "r")
sys.stdout = open("py/output.txt", "w")

n, k = map(int, input().split())

a = list(map(int, input().split()))

count = 0

for i in range(n):
    if a[i] >= a[k] and a[i] > 0:
        count += 1
    else:
        break

print(count)


sys.stdin.close()
sys.stdout.close()