import re
# Connection String
connectionString = {
    "fStopWord": "stopwords.txt",
    "fTokenA": "tokenization-input-part-A.txt",
    "fTokenB": "tokenization-input-part-B.txt"
}

def tokenization(file):
    # Param: string
    # Return: string
    def contraction(str): 
        return str.replace("'", "")
    
    # Param: string
    # Return: string[]
    def abbreviation(str):
        arr = str.split('.')
        if re.search("[a-z][.]([a-z][.])+", str):
            return punctuation(''.join(arr))
        
        else: return punctuation(str)
    
    # Param: string
    # Return: string[]
    def punctuation(str):
        ans = []
        isPun = False
        # string to char array as string isn't mutable
        str = contraction(str)
        arr = list(str)
        
        for i in range(0, len(arr)):
            asc = ord(arr[i])
            if not re.search("[a-z]|[0-9]", arr[i]):                
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
    
    f = open(file, "r")
    ans = []
    line = f.readline()
    while line:
        arr = line.split()
                
        for ele in arr:
            for k in abbreviation(ele.lower()):
                if (k != ''):
                    ans.append(k)
        line = f.readline()
    
    f.close()
    
    # Unit Test: All empty element will be removed later
    assert abbreviation("u.s.a.") == ["usa"], "Is abbreviation 1"
    assert abbreviation("u.s.a.,") == ["usa",""], "Is abbreviation 2"
    assert abbreviation("u.s.,a.") == ["us","a"], "Not abbreviation 1"
    assert abbreviation("u*.*s.,a'.") == ['u', '', '', 's', '', 'a', ''], "Not abbreviation 2"
    assert abbreviation("don't") == ["dont"], "Is contraction"
    assert abbreviation("ph.d") == ["ph", "d"], "Removimg punctuation"
    assert abbreviation("p'h.d") == ["ph", "d"], "Contraction within puntuation"
    return ans
    
def stemming(file):
    arr = tokenization(file)
    ans = []
    hash = {}
    
    f = open(connectionString['fStopWord'], "r")
    line = f.readline()
    # Init hashmap of stopwords
    while line:
        sw = line.split()[0]
        hash[line.split()[0]] = True
        line = f.readline()
    for i in range(0, len(arr)):
        if not hash.get(arr[i]): ans.append(arr[i])
    
    return ans

def porterStemmer(file):
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
            str = popHelper(2, str)
        
        # Delete 's' 
        if re.search("[aeiou][^aeiou]+s$", str) and not re.search("(us|ss)$", str):
            str = popHelper(1, str)
        
        # Replace 'ied' or 'ies' by 'i' or 'ie'
        if re.search("..+(ied|ies)", str):
            str = popHelper(2, str)
        elif re.search(".(ied|ies)", str):
            str = popHelper(1, str)
        return str
        
    def step1b(str):
        # Replace 'eed', 'eedly'
        if re.search("[aeiou][^aeiou]+eedly$", str):
            str = popHelper(2, str)
        elif re.search("[aeiou][^aeiou]+eed$", str):
            str = popHelper(1, str)
            
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
        
        if isDel:
            # Then end with 'at', 'bl', 'iz' or if word is short add 'e'
            if re.search("((at)|(bl)|(iz))$", str) or (len(str) <= 3 and len(str) > 0):
                temp = list(str)
                temp.append('e')
                str = "".join(temp)
            # End with double letter that is not 'll', 'ss', 'zz'
            else:
                temp = list(str)
                if temp[-1] == temp[-2] and not re.search("((ll)|(ss)|(zz))$", str):
                    str = popHelper(1, str)
        return str
    
    ans = []
    arr = stemming(file)
    for i in arr:
        ans.append(step1b(step1a(i)))
    
    return ans

def first300(arr):
    f = open('terms.txt', "w")
    dict = {}
    index = 0

    for i in arr:
        if dict.get(i): dict[i] += 1
        else: dict[i] = 1
        
    dict = sorted(dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    for i in dict:
        index += 1
        if index <= 300: f.write(i[0] + ' ' + str(i[1]) + '\n')
        else: break
    f.close()
        
def gatherData(arr):
    px = open('x.txt', 'w')
    py = open('y.txt', 'w')
    # vocab, collection = [], []
    vocabCount, collectionCount = 0, 0
    dict = {}
    
    for i in arr:
        collectionCount += 1
        # collection.append(collectionCount)
        
        if not dict.get(i): 
            vocabCount += 1
            dict[i] = True
        # vocab.append(vocabCount)
        
        px.write(str(collectionCount) + '\n')
        py.write(str(vocabCount) + '\n')
        
    px.close()
    py.close()
    
# Tokenized A
arr = porterStemmer(connectionString['fTokenA'])
f = open('tokenized.txt', "w")
for i in arr:
    f.write(i)
    f.write('\n')
f.close()

# Tokenized Moby Dick
arr = porterStemmer(connectionString['fTokenB'])
first300(arr)
gatherData(arr)
