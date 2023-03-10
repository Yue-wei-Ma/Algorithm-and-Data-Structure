import random


def bucket_sort(li,n=100,max_num=10000):
    buckets=[[] for _ in range(n)]
    for var in li:
        i=min(var//(max_num//n),n-1)
        buckets[i].append(var)
        for j in range(len(buckets[i])-1,0,-1):
            if buckets[i][j]<buckets[i][j-1]:
                buckets[i][j],buckets[i][j-1]=buckets[i][j-1],buckets[i][j]
            else:
                break
    sortedLi=[]
    for buc in buckets:
        sortedLi.extend(buc)
    return sortedLi
li=[random.randint(0,100) for i in range(1000)]
print(bucket_sort(li))
