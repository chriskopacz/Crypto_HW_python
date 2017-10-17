#Chris Kopacz
#Crypto 100 HW1 (decryption) -> filename = CK_decrypt_HW1.py
#created: 30 May 2017
#NOTE: run this script in ipython using "run CK_decrypt_HW1.py"
#      or from a windows command line using "python.exe CK_decrypt_HW1.py" (provided that
#      the location of python.exe is added to the PATH variable)
"""
Decrypt simple rotation, substitution, and permutation ciphers.
(user provides ciphertext and key for decryption)
"""


#define user input function
def userInput():
    selection = input('Selection desired decryption:\n'+
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

#define rotation decryption
def rotationDecrypt():

    message = input('Input message to be decrypted:\n   >>> ')
    kValue = input('Input rotation value:\n   >>> ')

    #try this code, if it fails for invalid vKalue, print error
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

        #decryption
        for iter in range(0,len(encM)):
            temp = (((encM[iter]-65)-intK)%26)+65
            encM[iter] = temp

        #convert decrypted numbers back to characters and append to string
        while len(encM) > 0:
            output = output + chr(encM.pop(0))

        #output decrypted message
        print('Decrypted message:')
        print('   '+output)

    #error handling for invalid kValue
    except ValueError:
        print('Invalid rotation value')
#=====

#define substitution decryption
def subvigDecrypt():
    
    message = input('Input message to be decrypted:\n   >>> ')
    subKey = input('Input key for decryption:\n   >>> ')

    message = message.upper()
    subKey = subKey.upper()
    listM = list(message)
    listK = list(subKey)
    newListM = []
    newListK = []
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

    #decryption
    for iter in range(0,len(newListM)):
        k = newListK[(iter%len(newListK))]
        m = newListM[iter]
        L = ((m-k)%26)+65
        encM.append(L)

    #convert numbers back to characters and append to string
    while len(encM) > 0:
        output = output + chr(encM.pop(0))

    #print output
    print('Decrypted message:')
    print('   '+output)
#=====

#define permutation decryption
def permutationDecrypt():
    
    message = input('Input message to be decrypted:\n   >>> ')
    key = input('Input transposition key:\n   >>> ')

    message = message.upper()
    key = key.upper()
    listM = list(message)
    listK = list(key)
    newListM = []
    grid = []
    tempGrid = []
    order = []
    output = ''

    #remove spaces and non-alpha characters from message
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
            i = 0
        else:
            i = i+1
    listK.reverse()

    #determine order of columns for transposition
    temp = listK.copy()
    temp.sort()

    for iter in range(0,len(listK)):
        order.append(listK.index(temp[iter]))

    #insert rows according to order[]
    for iter in range(0,len(listK)):
        grid.append('')

    for iter in range(0,len(listK)):
        tempGrid = []
        for jter in range(0,len(listK)):
            tempGrid.append(listM.pop(0))
        grid[order[iter]] = tempGrid

    #put decrypted grid back into string form, read down columns according to order
    for iter in range(0,len(grid[0])):
        temp = ''
        for jter in range(0,len(grid)):
            temp = temp + grid[order[jter]][iter]
        output = output+temp

    #print results
    print('Decrypted message:')
    print('(might contain a few random characters at the end)')
    print('   '+output)
#=====

#define main function
def main():
    userSelection = userInput()

    if (userSelection >= 1) and (userSelection <= 3):
        print('\n***\n'+
              'NOTE: For simplicity, all messages are handled as uppercase and\n'+
              '      punctuation, spaces, and #\'s are removed\n'+
              '      Plaintext decryption returned as a single string\n'+
              '***\n')

    if (userSelection == 1): #call rotation decryption
        print('ROTATION DECRYPTION:')
        rotationDecrypt()
    elif (userSelection == 2): #call substitution decryption
        print('SUBSTITUTION (VIGENERE) DECRYPTION:')
        subvigDecrypt()
    elif userSelection == 3: #call permutation decryption
        print('PERMUTATION DECRYPTION:')
        permutationDecrypt()
    elif userSelection == 4:
        print('EXIT')
    else:
        print('\n===== Invalid Selection - EXIT =====')


#call main cuntion =====================
main()
















