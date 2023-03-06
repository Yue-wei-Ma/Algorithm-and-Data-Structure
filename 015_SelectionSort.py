"""
首先确定第一个元素，第一个位置的数最小，然后确定第二个，第三个...
"""
li=[3,4,2,1,5,6,7,8]
n=len(li)
for i in range(n):
    for j in range(i+1,n):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
        print(li)






