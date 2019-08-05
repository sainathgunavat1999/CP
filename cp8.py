a = int(input("Enter number of CYCLE"))
height = 1
for i in range(1,a+1):
    if(i%2 == 0):
        height = height + 1
    else:
        height = 2*height

print(height)
# shubham jadhao
