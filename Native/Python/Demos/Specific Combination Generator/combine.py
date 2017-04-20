import numpy as np

def fun(x):
    return np.sum(x) > 5

def combinations(array,m,condition):
    length = np.size(array)
    indexs = None
    result = None
    if m > length:
        return indexs,result

    indices = np.arange(m)
    if condition(array[indices]):
        result = array[indices]
        indexs = indices

    while True:
        for i in reversed(range(m)):
            if indices[i] != i + length - m:
                break
        else:
            return indexs,result
        indices[i] += 1
        for j in range(i+1,m):
            indices[j] = indices[j-1] + 1
        if condition(array[indices]):
            if result is None:
                indexs = indices.copy()     # This is a tutorial bug
                result = array[indices]
            else:
                indexs = np.row_stack((indexs,indices))  
                result = np.row_stack((result,array[indices]))
            
if __name__=='__main__':
    array = np.random.randint(5,size=10)
    print array
    (indexs,result) = combinations(array,2,fun)
    print indexs
    print result