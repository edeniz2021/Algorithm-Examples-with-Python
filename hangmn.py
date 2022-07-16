import random
lis = ["banana","apple","chair","table","glass"]
a = random.choice(lis)
c = []
for i in a:
    c= "_"
    print(end=c)
p=0
print("\n")
n=0
while n != len(a):
    b = input("harf tahmin et\n")
    n+=1
    for i in range(len(a)):
        d = a[i]
        if d == b:
            c[i]= d
        #    print(end=b)
       # else:
        #    print(end="_")
        print(end=c)
