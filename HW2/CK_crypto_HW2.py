#Chris Kopacz
#Crypto 100 HW2 -> filename = CK_crypto_HW2.py
#created: 8 June 2017
#NOTE: run this cript in ipyton using "run CK_crypto_HW2.py"
#      or from a windows command line using "python.exe CK_crypto_HW2.py" (provided that the
#      location of python.exe is added to the PATH variable)
#NOTE: make sure that when this script is run that the appropriate files 'tags.txt' and
#      'master.key' are in the same directory/folder as 'CK_crypto_HW2.py'
#      no error catching has been used for file placement or formatting of said files

"""
read through 'tags.txt' which contains plaintext and MAC values then determine which MAC
values are valid and which are not by using 'master.key' and relevant hmac functions
"""

import hmac

#define function to open tags file and retrive plaintext msg's and MAC values/tags
#the MAC values/tags will later be tested for validity for the given plaintext msg
#returns an array containing pairs of plaintext msg's and MAC values in each row
def openTagsAndCleanUp():
    #open the file
    fileIn = open('tags.txt',mode='rt')

    #read file to a new variable
    tags = fileIn.readlines()

    #close the file
    fileIn.close()

    #remove newline characters (\n) from tags 
    for iter in range(0,len(tags)):
        tags[iter] = tags[iter].replace('\n','')

    #partition each line of tags[] by the ':' character
    for iter in range(0,len(tags)):
        tags[iter] = tags[iter].rpartition(':')

    #right now each line of tags[] is a tuple
    #convert each line to a list 
    #then remove the ':' character which will be in list index 1 (one)
    for iter in range(0,len(tags)):
        tags[iter] = list(tags[iter])
        tags[iter].pop(1)

    #return array of plaintext and MAC values
    return tags
#=====

#define function to open key file and retrieve key value for MAC tag generation
#returns the key value as a string
def getKeyFromFile():
    #open the file
    fileIn = open('master.key',mode='rt')

    #read the file to a new variable
    key = fileIn.read()

    #close the file
    fileIn.close()

    #return key value
    return key
#=====

#define function for generating MAC value/tag
#input 1 is a string called 'msg' -> plaintext to be encrypted
#input 2 is a string called 'key' -> value used as the key for encryption
#returns the MAC value/tag generated for the given plaintext msg
def genTag(msg, key):
    hm = hmac.new(key.encode())
    hm.update(msg.encode())

    return hm.hexdigest()
#=====

#define main function
def main():
    #get plaintext and tags
    tags = openTagsAndCleanUp()
    
    #get key
    key = getKeyFromFile()

    #generate tags using 'key' and plaintext from tags[]
    newTags = []
    for iter in range(0,len(tags)):
        newTags.append(genTag(tags[iter][0],key))

    #check validity of the generated MAC values vs the given MAC values
    validity = []
    for iter in range(0,len(newTags)):
        validity.append(newTags[iter] == tags[iter][1])

    #print results
    for iter in range(0,len(tags)):
        temp = tags[iter][0]
        temp2 = temp[0:15]+'...'

        print(str(iter+1) + ')  ' + temp2 + '  ->  ' + 
              tags[iter][1] + '  ->  ' + str(validity[iter]))
#=====

#call main function
main()
#=====
