import random


def Merge(li,low,mid,high):
    i=low
    j=mid+1
    ltemp=[]
    while i<=mid and j<=high:
        if li[i]<li[j]:
            ltemp.append(li[i])
            i+=1
        else:
            ltemp.append(li[j])
            j+=1
    while i<=mid:
        ltemp.append(i)
        i+=1
    while j<=high:
        ltemp.append(j)
        j+=1
    li[low:high+1]=ltemp

def MergeSort(li,low,high):
    if low<high:
        mid=(low+high)//2
        MergeSort(li,low,mid)
        MergeSort(li,mid+1,high)
        Merge(li,low,mid,high)
li=list(range(1000))
random.shuffle(li)
print(li)
MergeSort(li,0,len(li)-1)
print(li)
