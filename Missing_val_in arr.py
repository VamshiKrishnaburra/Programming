import array as arr
def missing_num(num):
    n=len(num)+1
    s_val=min(num)
    l_val=max(num)
    exp_val=(n*(s_val+l_val))//2
    act_val=sum(num)
    op=exp_val-act_val
    return op
#for 1 it will not work ? why
arr1=arr.array('i',[2,4,3,5,7])
print(missing_num(arr1))