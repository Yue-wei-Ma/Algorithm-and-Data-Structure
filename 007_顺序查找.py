#熟练度★
li=[2,3,5,7,9]
def search(li,val):
    for i in range(len(li)):
        if li[i]==val:
            return i
    return
print(search(li,10))
