from flask import Flask,escape,jsonify,request

app=Flask(__name__)

items ={
    'carrot': 5,
    'cauliflower': 3,
    'spinach' : 7
 }

@app.route('/groceries',methods=['GET', 'POST'])
def allItems():
    if request.method=='GET':
        return items

@app.route('/groceries/<string:name>',methods=['GET', 'POST','DELETE'])
def veggie(name):
    if request.method=='POST':
        items[name]=8
        return  jsonify(items)

    if request.method=='DELETE':
        del items[name]
        return  jsonify(items)

    




