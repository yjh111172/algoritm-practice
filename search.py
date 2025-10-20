def search_all(a,x):
    result= []
    for i in range(0,len(a)):
            if a[i]== x:
                result.append(i)
    return result

v=[17,92,18,33,58,7,33,42]
print(search_all(v,18))
print(search_all(v,33))
print(search_all(v,900))