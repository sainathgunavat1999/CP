n = int(input("Enter your Number"))
b = []
b.append(n)
while(n != 1):
    if(n%2 == 0):
        n = n/2
        b.append(n)
    else:
        n = n*3 + 1
        b.append(n)

print(b)
# shubham jadhao
