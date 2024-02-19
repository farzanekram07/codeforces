num = int(input())
k = int(input())
'''Here the code and logic is completely right, but 
to run on codeforce we need to keep in mind the input format
codeforces uses comma separated input.
so, new code for input -

num, k = map(int, input().split())
'''
for i in range(k):
    if num % 10 == 0:
        num = num // 10
    else:
        num = num - 1

print(num)