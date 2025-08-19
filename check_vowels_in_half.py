def check_vowels_in_half(s):
    def count_vowels(string):
        vowels='aeiouAEIOU'
        count=0
        for i in string:
            if i in vowels:
                count+=1
        return count
    
    
    mid=n//2
    first_half=s[:mid]
    second_half=s[mid:]
    first=count_vowels(first_half)
    second=count_vowels(second_half)
    return first==second

str=input("enter even string=")
n=len(str)
if n%2 != 0:
    print("enter even string")
else:
    print(check_vowels_in_half(str))