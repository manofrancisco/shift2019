from flask import Flask,request as r,Response
import requests
from pathlib import Path
from random import SystemRandom
import json
from netifaces import *




from stringutils import BMSearch

app = Flask(__name__)

digits = ''
def main():
    global myaddress
    global contaclist
    contaclist={}
    myaddress='0'



@app.route('/search/<string>', methods=['GET'])
def search(string):
    return searchstring(string)

@app.route('/register/<ip>',methods=['GET','POST'])
def register(ip):
    if(r.method =='POST' ):
        newid = len(contactlist.keys())
        contactlist[str(newid)] = ip
        return Response(status=200)
    if(r.method == 'GET'):
        #add to contactlist and return
        contactlist
        newid = len(contactlist.keys())
        contactlist[str(newid)] = ip
        return json.dumps(contactlist, ensure_ascii=False)

#/get/index?length=10
@app.route('/get/<index>', methods=['GET'])
def get(index):
    length = r.args.get('length', default=10, type=int)
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

def propagate(myaddress):
    for k,v in contactlist:
        address = 'http://' + v + '/register/' + myaddress
        requests.post(address)

def register():
    print('getting info')
    ifaceName = interfaces()[6]
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr': 'No IP addr'}])]
    myaddress = addresses[0]
    address = 'http://'+contactlist.keys[0]+'/register/'+myaddress
    r = requests.get(address)
    contactlist= r.json()
    propagate(myaddress)
    return '0'

def setupclient():
    info = register()
    clientfile = open('clientid.txt', 'w')
    clientfile.write(info)
    clientfile.close()

def is_installed():
    file = Path('digits.pi')
    if not file.is_file():
        return False
    return True



def setup():
    with open('contacts.json', 'r') as infile:
        list= json.load(infile)
    contactlist = list
    idH = ''


if __name__ == '__main__':
    main()
    install()
    setup()
    app.run()
