from flask import Flask, request

app = Flask(__name__)


@app.route('/search/<string>', methods=['GET'])
def search(string):
    return str(searchstring(string))

#/get/index?length=10
@app.route('/get/<index>', methods=['GET'])
def get(index):
    length = request.args.get('length', default=10, type=int)
    return getstring(index,length)


def getstring(index,length):
    return "bom dia " + length

def searchstring(index):
    return 1

def install():
    pass

if __name__ == '__main__':
    install()
    app.run()
