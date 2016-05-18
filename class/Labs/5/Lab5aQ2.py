# def merge(L1, L2):
#     result = [[]]
#     L3 = L1 + L2
#     for x in range(len(L3)):
#         temp = min(L3)
#         L3.remove(temp)
#         result.append(temp)
#     return(result)
def insert(L, X):

    result = [ ]
    i = 0

    while i < len(L) and L[i] <= X:
        result.append(L[i])
        i += 1

    result.append(X)

    return result + L[i:]



## inefficient way using insert function
def merge(L1, L2):
    result = L1.copy()
    for x in L2:
       result = insert(result,x)
    return result

# efficient without using insert
def merge2(L1, L2):
    L3 = []
    i = j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            L3.append(L1[i])
            i+=1
        else:
            L3.append(L2[j])
            j+=1
    if i < len(L1):
        L3+=L1[i:]
    else:
        L3+=L2[j:]
    return L3


   




L1 = [10, 20, 30, 40, 50]
L2 = [5, 15, 45, 55, 85, 95]
L3 = merge(L1, L2)
print(L3)

L3 = merge2(L1, L2)

print(L3)