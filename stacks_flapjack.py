cakes = list(map(int,input().split()))
count = 0
ques = tuple(cakes)

def flip(no,lst,sn=0,ln=0):
    global cakes
    c =0
    if(no == 0):
        return int(0),cakes
    if(no == len(lst)-1):
        lst.reverse()
        # print(lst)
        return int(1),lst
    # for i in range(len(cakes) - 1):
    #     if (cakes[i] > cakes[i + 1]):
    #         c = cakes[i] - cakes[i+1]
    #         break
    #

    return None,cakes

re = -1
ans = []
while re!=0 and re!=None:
    count = 0
    if(re==0):
        ans.append(int(0))
        break
    # print("re = ",re)
    # print("Cakes = ",cakes)
    for i in range(len(cakes) - 1):
        if (cakes[i] > cakes[i + 1]):
            count = count + 1
    # print("Counttt = ",count)
    re,cakes = flip(count, cakes)
    ans.append(re)

print(ques)
print(ans)
# print("count = ",count)
# print("cakes = ",cakes)
