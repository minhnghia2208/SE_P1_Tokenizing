# Connection String
fStopWord = "stopwords.txt"
fTokenA = "tokenization-input-part-A.txt"
fTokenB = "tokenization-input-part-B.txt"
#

def tokenization():
    # Param: string
    # Return: string
    def contraction(str): 
        return str.replace("'", "")
    
    # Param: string
    # Return: string[]
    def abbrivation(str):       
        arr = str.split('.')
        for ch in arr:
            if len(ch) > 1: return punctuation(str)
        
        return [''.join(arr)]
    
    # Param: string
    # Return: string[]
    def punctuation(str):
        ans = []
        isPun = False
        # string to char array as string isn't mutable
        arr = list(str)
        
        for i in range(0, len(arr)):
            asc = ord(arr[i])
            if not (
                (asc >= 97 and asc <= 122) or # lower case char
                (asc >= 48 and asc <= 57)   # number
                ):                
                isPun = True
                # recursively remove punctuation
                for j in str.split(arr[i]):
                    temp = punctuation(j)
                    
                    # Concat new tokenized word to ans array
                    for k in temp:
                        ans.append(k)
                
                # stop at the first punctuation 
                break
        
        if isPun: return ans
        else: return [str]
    
    # Body
    f = open(fTokenA, "r")
    ans = []
    line = f.readline()
    while line:
        arr = line.split()
                
        for ele in arr:
            ele = contraction(ele.lower())
            for k in abbrivation(ele):
                ans.append(k)
            # ele = punctuation(ele)
        line = f.readline()
    
    print(ans)
        
    f.close()
    
    # UNIT TEST AREA
    # print(abbrivation("u.s.d.a.s.d"))
    # print(contraction("don't"))
    # print(punctuation("100,200*300"))
    
tokenization()