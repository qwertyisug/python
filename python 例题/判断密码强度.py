import re
 
def checklen(data):
    return len(data) >= 10
 
def checkUpper(data):
    upper = re.compile('[A-Z]+')
    match = upper.findall(data)
    if match:
        return True
    else:
        return False
 
def checkLower(data):
    lower = re.compile('[a-z]+')
    match = lower.findall(data)
    if match:
        return True
    else:
        return False
 
def checkNum(data):
    num = re.compile('[0-9]+')
    match = num.findall(data)
    if match:
        return True
    else:
        return False
 
def checkSymbol(data):
    symbol = re.compile('([^a-zA-Z0-9])+')
    match = symbol.findall(data)
    if match:
        return True
    else:
        return False
 
def checkio(data):
    if checklen(data):
        if checkUpper(data):
            if checkLower(data):
                if checkNum(data):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
    
if __name__ == '__main__':
    def checkio(s):
    fs = ''.join(filter(str.isalnum, s)) 
    return (
            len(fs) >= 1        
        and len(s)  >= 10      
        and not fs.isalpha()    
        and not fs.isdigit()    
        and not fs.islower()   
        and not fs.isupper()    
    )
