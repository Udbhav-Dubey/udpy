def binary(list,K):
    left=0
    right=len(list)-1
    while left <=right:
        mid=left+(right-left)//2
        if K>=list[mid][0] and K<=list[mid][1]:
            return mid
        elif K<list[mid][0] :
            right=mid-1
        else : left= mid+1
    
    return -1


list = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
K = 37
print(binary(list,K))
