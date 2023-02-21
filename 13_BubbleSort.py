"""
首先确定第一个元素，第一个位置的数最小，然后确定第二个，第三个...
arr=[64,34,25,12,22,11,90]
import random
li=[i+1 for i in range(10)]
"""
li=[90,64,34,25,12,22,11]
def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]

bubble_sort(li)
print(li)

