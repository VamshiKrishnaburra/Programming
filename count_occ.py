#Given a list of numbers, count the occurrences of each number and return a dictionary.
def count_occ(nums):
    count_dict={}
    for i in nums:
        if i in count_dict:
            count_dict[i]+=1
        else:
            count_dict[i]=1
    return count_dict
num=[1,2,3,1,2,3,4,5,1]
print(count_occ(num))