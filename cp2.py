a = input("Enter your String")
b = a.split(" ")
c = []
count = 0
for i in b:
    c.append(len(i))
maxlength = max(c)
for i in c:
    if(i == maxlength):
        count = count + 1
print(maxlength)
print(count)
# shubham jadhao
