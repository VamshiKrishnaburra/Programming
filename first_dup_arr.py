import array as arr
def first_dup_arr(arr):
    seen=set()
    for item in arr:
        if item in seen:
            return item
        seen.add(item)
    return None
arr1=[2,1,3,2,5]
print(first_dup_arr(arr1))