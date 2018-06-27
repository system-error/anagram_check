word1 = input('Please write the first word: ')
word2 = input('Please write the first word: ')

def checkForAnagram(word1,word2):
    str1 =  word1.lower()
    str2 =  word2.lower()

    str1 = sorted(str1)
    str2 = sorted(str2)

    if str1 == str2:
        print('True')
    else:    
        print('false') 

    # for letter1,letter2 in zip(str1,str2):
    #     if letter1 == letter2:
    #         print('True')
    #     else:    
    #         print('false')    
        

checkForAnagram(word1,word2)
