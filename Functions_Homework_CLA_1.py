#Write a Python function that checks whether a passed string is palindrome or not. 
#A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
string_with_space=input('Enter name')
string=''
def delete_spece(string_with_space,string):
    for i in range(len(string_with_space)):
        if string_with_space[i]!=' ':
            string=string+string_with_space[i]
        else:
            pass
    return string
delete_spece(string_with_space,'')
print(string)
def palindrome_check(string):
    mid_length=int(len(string)/2)
    rev_string=string [::-1]
    if string[:mid_length]==rev_string[:mid_length]:
        print('This word is indeed a palindrome')
    else:
        print('This word is not a palindrome')
palindrome_check(string)

