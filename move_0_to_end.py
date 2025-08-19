def move_zeros(arr):
    j=0
    #for i in len(num): → len() gives a number, not an iterable.Should be: for i in range(len(arr))
    for i in range(len(arr)):
        if(arr[i]!=0):
            arr[j]=arr[i]
            j+=1
    while j<len(arr):
        arr[j]=0
        j+=1
   
    return arr

arr1=[3,4,0,9,0,8,5,7]
print(move_zeros(arr1))