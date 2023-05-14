import sys
import re
from webbot import Browser

def callFun():
    filename = sys.argv[1]
    contents = Words(filename)
    email = verifiyGmail(contents)
    passW = findPassword(contents)
    tryEmailAndPass(email, passW)

def Words(filename):
        
    with open(filename) as f:
        contents = "".join(f.read().splitlines())
        contents = re.sub("[\(\[].*?[\)\]]", "", contents)
        return contents
def verifiyGmail(contents):
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', contents)
    match = str(match)
    match = match[1:-2]
    i = 0
    while i < len(match):
        if match[i:i+5] == "l.com":
            match = match[1:i+5]
        i += 1
    print(match)
    return match
def findPassword(contents):
    i = 0
    possibePass = ""
    while i < len(contents):
        if contents[i:i+5] == "l.com":
            possibePass = contents[i+5:i+17]
            print(possibePass)
            return(possibePass)
        i += 1 
def tryEmailAndPass(email, passW):
    webList = ['google.com', 'amazon.com', 'youtube.com']
    web = Browser()
    for i in webList:
        web.go_to(i)
        #web.type('hello its me')  # or web.press(web.Key.SHIFT + 'hello its me')
        #web.press(web.Key.ENTER)
        #web.go_back()
        web.click('Sign in')
        web.type(email , into='Email')
        web.click('NEXT' , tag='span')
        web.type(passW , into='Password', id='passwordFieldId') # specific selection
        web.click('NEXT' , tag='span')
    
    


print(callFun())
