def repi_words_in_str(s:str):
    seen={}
    repeated=[]
    not_repeated=[]
    for char in s:
        if char in seen:
            seen[char]+=1
            repeated.append(char)
        else:
            seen[char]=1 
            not_repeated.append(char)
    return repeated,not_repeated
   # You're looping through each key-value pair in the dictionary.
   #char is the key (the character in the string)
   #count is the value (how many times that character appeared)
   #You're doing tuple unpacking — getting the key and value for each dictionary entry. 
    '''ANOTHER METHOD
    for char,count in seen.items():
        if count>1:
            repeated.append(char)
        else:
            not_repeated.append(char)
    return repeated,not_repeated'''

string = "programming"
print(repi_words_in_str(string))
