import numpy as np

def fun(x):
    return np.sum(x) > 4

def combinationsvar(array,max,condition):
    length = np.size(array)
    indexs = list()
    results = list()
    for m in range(1,max+1):
        if m > length:
            break

        indices = np.arange(m)
        if condition(array[indices]):
            results.append(array[indices])
            indexs.append(indices.copy())

        while True:
            for i in reversed(range(m)):
                if indices[i] != i + length - m:
                    break
            else:
                break
            indices[i] += 1
            for j in range(i+1,m):
                indices[j] = indices[j-1] + 1
            if condition(array[indices]):
                indexs.append(indices.copy())   
                results.append(array[indices])

    return indexs,results
                
if __name__=='__main__':
    array = np.random.randint(6,size=10)
    #array = np.arange(3)
    print array
    (indexs,result) = combinationsvar(array,2,fun)
    print indexs
    print result