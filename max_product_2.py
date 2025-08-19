import array as arr
def max_product_of_2(num):
    num1=sorted(num)
    print(num1)
    print(num1[-1]*num1[-2])
    return None
arr1=arr.array('i',[3,4,8,5,7])
print(max_product_of_2(arr1))