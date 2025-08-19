def longest_string(sentence:str):
    words=sentence.split()
    if not words:
        return '',0
    largest_word=max(words,key=len)
    return largest_word,len(largest_word)
    
sentence="python is easy Programming language"
print(longest_string(sentence))