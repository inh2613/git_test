n=int(input())

num=[]
for _ in range(n):
    a,b=map(int,input().split())

    num.append([a,b])

num.sort(key=lambda x: (x[1],x[0]))


for i in num:
    print(i[0],i[1])


    