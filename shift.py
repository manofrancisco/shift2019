import flask
import requests
from pathlib import Path
from random import SystemRandom
app = flask.Flask(__name__)

digits = ''
id = 0
server_address = 'http://127.0.0.1:8000'


@app.route('/search/<string>', methods=['GET'])
def search(string):
    return searchstring(string)


#/get/index?length=10
@app.route('/get/<index>', methods=['GET'])
def get(index):
    length = flask.request.args.get('length', default=10, type=int)
    return getstring(index,length)


def getstring(index,length):
    return "bom dia " + length

def searchstring(s):
    return str(BMSearch(s))

def install():
    if(not is_installed()):
        print('Installinggggg')
        setupclient()
        get_digits()


def get_digits():
    string = ''
    rand = SystemRandom()
    for i in range(10000):
        string+=str(rand.randint(0, 9))
    clientfile = open('digits.pi', 'w')
    clientfile.write(string)
    clientfile.close()


def get_info():
    print('getting info')
    #r = requests.get(server_address+'/Registration')
    #return r.text
    return '0'

def setupclient():
    info = get_info()
    clientfile = open('clientid.txt', 'w')
    clientfile.write(info)
    clientfile.close()

def is_installed():
    file = Path('clientid.txt')
    if not file.is_file():
        return False
    return True


# Generate the Bad Character Skip List
def generateBadCharShift(term):
    skipList = {}
    for i in range(0, len(term) - 1):
        skipList[term[i]] = len(term) - i - 1
    return skipList


# Generate the Good Suffix Skip List
def findSuffixPosition(badchar, suffix, full_term):
    for offset in range(1, len(full_term) + 1)[::-1]:
        flag = True
        for suffix_index in range(0, len(suffix)):
            term_index = offset - len(suffix) - 1 + suffix_index
            if term_index < 0 or suffix[suffix_index] == full_term[term_index]:
                pass
            else:
                flag = False
        term_index = offset - len(suffix) - 1
        if flag and (term_index <= 0 or full_term[term_index - 1] != badchar):
            return len(full_term) - offset + 1


def generateSuffixShift(key):
    skipList = {}
    buffer = ""
    for i in range(0, len(key)):
        skipList[len(buffer)] = findSuffixPosition(key[len(key) - 1 - i], buffer, key)
        buffer = key[len(key) - 1 - i] + buffer
    return skipList


# Actual Search Algorithm
def BMSearch(needle):
    haystack = ''
    with open('digits.pi', 'r') as myfile:
        haystack = myfile.read()
    print(haystack)
    goodSuffix = generateSuffixShift(needle)
    badChar = generateBadCharShift(needle)
    i = 0
    while i < len(haystack) - len(needle) + 1:
        j = len(needle)
        while j > 0 and needle[j - 1] == haystack[i + j - 1]:
            j -= 1
        if j > 0:
            badCharShift = badChar.get(haystack[i + j - 1], len(needle))
            goodSuffixShift = goodSuffix[len(needle) - j]
            if badCharShift > goodSuffixShift:
                i += badCharShift
            else:
                i += goodSuffixShift
        else:
            return i
    return -1



def setup():
    idH = ''
    with open('clientid.txt','r') as myfile:
        idH = myfile.read()
    id = idH
    print('\n')
    print(id)
    print('\n')

if __name__ == '__main__':
    install()
    setup()
    app.run()
