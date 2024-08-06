a=int(input())
res=int(a%100)
if(res<10):
    print(0,end='')
    print(res)
else:
    print(res)