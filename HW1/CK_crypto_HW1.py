#Chris Kopacz
#Crypto 100 HW1 -> filename = CK_crypto_HW1.py
#created: 25 May 2017
#NOTE: run this script in ipython using "run CK_crypto_HW1.py"
#      or from a windows command line using "python.exe CK_crypto_HW1.py" (provided that the
#      location of python.exe is added to the PATH variable)
"""
Make simple rotation, substitution, and permutation ciphers.
"""

import random

#define user input function
def userInput():
    selection = input('Select desired cipher:\n'+
                      '1) Rotation\n'+
                      '2) Substitution (Vigenere)\n'+
                      '3) Permutation\n'+
                      '\n4) Exit'+
                      '\n\n   >>> ')
    try:
        if int(selection) > 4 or int(selection) < 1:
            return 0
        else:
            return int(selection)
    except ValueError:
        return 0

#define rotation cipher
def rotationCipher():
    
    message = input('Input message to be encrypted:\n   >>> ')
    kValue = input('Input rotation value:\n   >>> ')
    
    #try this code, if it fails for invalid kValue, print error
    try:
        intK = int(kValue)
        encM = []
        message = message.upper()
        listM = list(message)
        output = ''
        
        #convert message to numbers, omit punctuation, spaces, and digits
        for iter in range(0,len(listM)):
            if listM[iter].isalpha():
                encM.append(ord(listM[iter]))

        #encryption
        for iter in range(0,len(encM)):
            temp = (((encM[iter]-65)+intK)%26)+65
            encM[iter] = temp

        #convert encrypted numbers to characters and append to string
        while len(encM) > 0:
            output = output + chr(encM.pop(0))

        #output encrypted message
        print('Encrypted message:')
        print('   '+output)
        
    #error handling for invalid kValue
    except ValueError:
        print("Invalid rotation value")
#=====    
    
#define substitution cipher
def subvigCipher():
    
    message = input('Input message to be encrypted:\n   >>> ')
    subKey = input('Input key for encryption:\n   >>> ')

    message = message.upper()
    subKey = subKey.upper()
    listM = list(message)
    listK = list(subKey)
    newListK = []
    newListM = []
    encM = []
    output = ''

    #convert key to numbers, omit punctuation, spaces, and digits
    for iter in range(0,len(listK)):
        if listK[iter].isalpha():
            temp = ord(listK[iter])-65
            newListK.append(temp)
    
    #convert message to numbers, omit punctuation, spaces, and digits
    for iter in range(0,len(listM)):
        if listM[iter].isalpha():
            temp = ord(listM[iter])-65
            newListM.append(temp)
            
    #encryption
    for iter in range(0,len(newListM)):
        k = newListK[(iter%len(newListK))]
        m = newListM[iter]
        L = ((k+m)%26)+65
        encM.append(L)
        
    #converted encrypted numbers back to characters and append to string
    while len(encM) > 0:
        output = output + chr(encM.pop(0))

    #print output
    print('Encrypted message:')
    print('   '+output)
#=====

#define permutation cipher
def permutationCipher():
    message = input('Input message to be encrypted:\n   >>>')
    key = input('Input transposition key:\n'+
                '(one word, less than 10 characters for simplicity)\n   >>>')

    message = message.upper()
    key = key.upper()
    listM = list(message)
    listK = list(key)
    newListM = []
    grid = []
    tempGrid = []
    order = []

    #remove spaces and non-alpha characters
    for iter in range(0,len(listM)):
        if listM[iter].isalpha():
            newListM.append(listM[iter])
    
    #remove non-unique characters from key
    i = 0
    listK.reverse()
    while i < len(listK):
        temp = listK[i]
        if listK.count(temp)>1:
            while listK.count(temp)>1:
                listK.remove(temp)
            i=0
        else:
            i = i+1
    listK.reverse()

    #put message into grid with rows of length len(key)
    for iter in range(1,len(newListM)+1):
        tempGrid.append(newListM[iter-1])
        if iter%len(listK) == 0:
            grid.append(tempGrid)
            tempGrid = []
        if iter == len(newListM) and len(tempGrid)>0:
            grid.append(tempGrid)

    #if grid has empty spaces in last row, fill with random letters
    if len(grid[len(grid)-1]) < len(listK):
        while len(grid[len(grid)-1]) < len(listK):
            grid[len(grid)-1].append(chr(random.randint(65,90)))
    
    #determine order of columns for transposition
    temp = listK.copy()
    temp.sort()
    
    for iter in range(0,len(listK)):
        order.append(listK.index(temp[iter]))

    #transpose the columns based on order[]
    encM = ''

    for col in range(0,len(order)):
        for row in range(0,len(grid)):
            encM = encM + grid[row][col]

    #print(grid)
    #print(order)
    print('Encrypted message:')
    print('   '+encM)
#=====


#=========================================================================

#define main function
def main():
    userSelection = userInput()

    if (userSelection >= 1) and (userSelection <= 3):
        print('\n***\n'+
              'NOTE: For simplicity, all messages are handled as uppercase and\n'+
              '      punctuation, spaces, and #\'s are removed\n'+
              '***\n')

    if (userSelection == 1): #call rotation cipher
        print('ROTATION CIPHER:')
        rotationCipher()
    elif userSelection == 2: #call substitution cipher
        print('SUBSTITUTION (VIGENERE) CIPHER:')
        subvigCipher()
    elif userSelection == 3: #call permutation cipher
        print('PERMUTATION CIPHER:')
        permutationCipher()
    elif userSelection == 4:
        print('EXIT')
    else:
        print("\n===== Invalid Selection - EXIT =====")

#call main function =================
main()

