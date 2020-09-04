from flask import Flask, jsonify, request, render_template

app = Flask(__name__)  #creating object of Flask

stores = [
    {
        'name': 'My Wonderful Store',
        'items':[
        {
        'name': 'My item',
        'price': 15.99
        }
      ]
    }
]

# POST - used to recieve data, as we are on the server side
# GET - used to send data only, as we are on the server side
@app.route('/')
def home():
    return render_template('index.html')

# POST /store data: {name}
@app.route('/store',methods=['POST']) # by default it is GET
def create_store():
    request_data = request.get_json() # browser will send data and we need to access it
    new_store = {                       # dictionary
    'name': request_data['name'],      # when we do get_json, it converts json into python dictionary
    'items': []
    }
    stores.append(new_store)
    return jsonify(new_store) # return a string not a dictionary

# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store) # remember store is a dictionary, so we cant return store directly
    return jsonify({"message":"store not found"})
    # Iterate over the get_stores
    # If the store name matches, return it
    # If none match, return with error msg

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores}) # the 1st name could be used for reference and the 2nd one is the list we created above

# POST /store/<string:name>/item {name:, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
            'name' : request_data['name'],
            'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({"message":"store not found"})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})

    return jsonify({"message":"item not found"})
 # decorator for path

app.run(port=5000)
