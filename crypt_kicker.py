alphabets={'a':'x','b':'k','c':'q','d':'s','e':'u','f':'p','g':'m','h':'j',
           'i':'f','j':'g','k':'d','l':'b','m':'e','n':'h','o':'c','p':'a',
           'q':'y','r':'r','s':'v','t':'o','u':'i','v':'n','w':'z','x':'t',
           'y':'l','z':'w'}

n=int(input())
print("")
str=''
for i in range(n):
    string=input()
    for j in string:
        #print(j)
        if j is ' ':
            str=str+' '
        else:
            str=str+alphabets[j]
    print(str)
    print("")
    

