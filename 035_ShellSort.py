def insertionSort(li,gap):
    n=len(li)
    for i in range(gap,n):
        temp=li[i]
        j=i-gap
        while j>=0 and temp<li[j]:
            li[j+gap]=li[j]
            j-=gap
        li[j+gap]=temp
    return li
def shellSort(li):
    d=len(li)//2
    while d>=1:
        insertionSort(li,d)
        d//=2
li=list(range(1000))
import random
random.shuffle(li)
shellSort(li)
print(li)
