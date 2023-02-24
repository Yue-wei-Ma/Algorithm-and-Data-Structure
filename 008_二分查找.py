"""
有序数列
"""
#熟练度★
li=[2,3,5,7,9,13,17,21,26,29,30]
def binary_search(li,val):
    left=0
    right=len(li)-1
    while left<=right:
        mid=(left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]>val:
            right=mid-1
        else:
            left=mid+1
    else:
        return None
print(binary_search(li,7))
