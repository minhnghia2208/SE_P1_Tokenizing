import re
# Connection String
# from sympy import true
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
            if len(ch) > 1: 
                return punctuation(str)
        
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
                if (k != ''):
                    ans.append(k)
        # ans.append('\n')
        line = f.readline()
    
    f.close()
    return " ".join(ans)
    
def stemming():
    f = open(fStopWord, "r")
    arr = tokenization().split()
    ans = []
    hash = {}
    line = f.readline()
    # Init hashmap of stopwords
    while line:
        sw = line.split()[0]
        hash[line.split()[0]] = True
        line = f.readline()
    for i in range(0, len(arr)):
        if not hash.get(arr[i]): ans.append(arr[i])
    
    return "".join(ans)

def porterStemmer():
    def popHelper(n, str):
        temp = list(str)
        for i in range(0, n):
            temp.pop()
        return "".join(temp)
    
    # Param string
    # Return string
    def step1a(str):
        # Replace 'sses' by 'ss'
        if re.search("sses$", str):
            temp = list(str)
            temp.pop()
            temp.pop()
            str = "".join(temp)
        
        # Delete 's' 
        if re.search("[aeiou][^aeiou]+s$", str) and not re.search("(us|ss)$", str):
            temp = list(str)
            temp.pop()
            str = "".join(temp)
        
        # Replace 'ied' or 'ies' by 'i' or 'ie'
        if re.search("..+(ied|ies)", str):
            temp = list(str)
            temp.pop()
            temp.pop()
            str = "".join(temp)
        elif re.search(".(ied|ies)", str):
            temp = list(str)
            temp.pop()
            str = "".join(temp)
            
        print(str)
        return str
        
    def step1b(str):
        # Replace 'eed', 'eedly'
        if re.search("[aeiou][^aeiou]+eedly$", str):
            temp = list(str)
            temp.pop()
            temp.pop()
            str = "".join(temp)
        elif re.search("[aeiou][^aeiou]+eed$", str):
            temp = list(str)
            temp.pop()
            str = "".join(temp)
            
        # Delete 'ed', 'edly', 'ing', 'ingly'
        isDel = False
        if re.search("[aeiou].*ed$", str):
            str = popHelper(2, str)
            isDel = True
        elif re.search("[aeiou].*edly$", str):
            str = popHelper(4, str)
            isDel = True
        elif re.search("[aeiou].*ing$", str):
            str = popHelper(3, str)
            isDel = True
        elif re.search("[aeiou].*ingly$", str):
            str = popHelper(5, str)
            isDel = True
        
        # Then end with 'at', 'bl', 'iz' add 'e'
        if isDel:
            if re.search("(at)|(bl)|(iz)", str):
                temp = list(str)
                temp.append('e')
                str = "".join(temp)
            # elif re.search("")
            
        print(str)
        return str
    # arr = stemming().split()
    step1b('pirbring')

# stemming()
porterStemmer()