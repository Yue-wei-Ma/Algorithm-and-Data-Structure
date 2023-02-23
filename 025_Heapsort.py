"""
堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
即子结点的键值或索引总是小于（或者大于）它的父节点。
堆排序可以说是一种利用堆的概念来排序的选择排序。
"""
def sift(li,low,high):
    i=low
    j=2*i+1
    temp=li[low]
    while j<=high:
        if j+1<=high and li[j+1]>li[i]:
            j=j+1
        if li[j]>temp:
            li[i]=li[j]
            i=j
            j=2*i+1
        else:
            li[i]=li[temp]
            break
    else:
        li[i]=temp
def heap_sort(li):
    n=len(li)
    for i in range((n-2)//2,-1,-1):
        sift(li,i,n-1)
    for i in range(n-1,-1,-1):
        li[0],li[i]=li[i],li[0]
        sift(li,0,i-1)

