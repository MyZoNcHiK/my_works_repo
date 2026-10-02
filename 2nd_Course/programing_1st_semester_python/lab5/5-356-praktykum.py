n = int(input())
sum = 0
expr = ""
for i in range(1,n):
    sum += i*(i+1)
    expr += str(i) + "*" + str(i + 1)
    if i < n-1:
        expr += "+"
print(expr + "=" + str(sum))
