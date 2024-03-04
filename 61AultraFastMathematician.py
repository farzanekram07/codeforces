n = input()
m = input()

re = ""
for i in range(len(n)):
    if n[i] != m[i]:
        re =  re + "1"
    else:
         re = re + "0"

print(re)

