word1 = input('Please write the first word: ')
word2 = input('Please write the first word: ')

def checkForAnagram(word1,word2):
    str1 =  word1.lower()
    str2 =  word2.lower()

    list1 = list(word1)
    list2 = list(word2)
    str1 = sorted(str1)
    str2 = sorted(str2)
    # print(type(str1))
    # print()
    # print(str2)

    for value1,value2 in zip(str1,list1):
        if value1 ==' ' or value1==',':
            str1.remove(value1)
        elif value2 ==' ' or value2==',':    
            list1.remove(value2)
            
    for value1,value2 in zip(str2,list2):
        if value1 ==' ' or value1 ==',':
            str2.remove(value1)
        elif value2 ==' ' or value2==',':       
            list2.remove(value2)

    if str1 == str2:
        print('True')
        list1 = ''.join(list1)
        list2 = ''.join(list2)
        print(list1)          
        print(list2)
    else:    
        print('false') 
   

checkForAnagram(word1,word2) 
