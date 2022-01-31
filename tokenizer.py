# Global variables
fStopWord = "stopwords.txt"
fTokenA = "tokenization-input-part-A.txt"
fTokenB = "tokenization-input-part-B.txt"
#

def tokenization():
    # Input: string
    # Return: string
    def abbrivation(str):
        # Convert string to char array as string isn't mutable
        arr = list(str)

        i = 0
        while i < len(arr):
            if i < len(arr) and arr[i] == '.': 
                del arr[i]
            else: i += 1
                
        return ''.join(arr)
    
    # Input: string
    # Return: string
    def contraction(str): 
        return str.replace("'", "")
        
    # Input: string
    # Return: string[]
    def punctuation(str):
        # Convert string to char array as string isn't mutable
        arr = list(str)
        res = []

        i = 0
        while i < len(arr):
            # check if an alphabectical character
            if i < len(arr):
                asc = ord(arr[i])
                
                if not (
                    (asc >= 97 and asc <= 122) or # lower case char
                    (asc >= 65 and asc <= 90) or # upper case char
                    (asc >= 48 and asc <= 57)   # number char
                    ): res.append(str.split(arr[i])[0])
                    
            i += 1
            
        return res
    
    # Input: string
    # Return: string
    def lowerCase(str):
        print('test')
    
    # f = open(fTokenA, "r")
    # line = f.readline()
    # while line:
    #     arr = line.split()
        
    #     for ele in arr:
    #         res = abbrivation(ele)
    #     line = f.readline()
        
    # f.close()
    
    # UNIT TEST AREA
    # print(abbrivation("U.S.A.."))
    # print(contraction("don't"))
    print(punctuation("200,000,000,"))
    
tokenization()