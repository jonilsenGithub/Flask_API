# Flask API for dog names with authorization interface
#
# External API used:
# https://dog.ceo/dog-api/documentation/
#
# Author:  Jonas Nilsen
#
# Imports
import requests
from flask import Flask, jsonify, render_template, request, redirect, url_for
from cassandra.cluster import Cluster

cluster = Cluster(contact_points=['172.17.0.2'],port=9042)
session = cluster.connect()

cluster1 = Cluster(contact_points=['172.17.0.3'],port=9042)
session1 = cluster1.connect()

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



# Home page
@app.route('/')
def home():

    return render_template('create.html')




# Redirect from homepage when creating user
@app.route('/newuser', methods=['POST'])
def create():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        row = session1.execute("""select username from login.users where username='{0}'""".format(username))
        result = []
        for r in rows:
            result.append(r.username)

        if result!=[]:
            return 'Username already in use', 404

        else:
            session1.execute("""insert into login.users(username, password) values('{0}', '{1}')""".format(username, password))
            return 'Thank you', 200




# Retrieving all items in database, without the need for authorization
@app.route('/all', methods=['GET'])
def dogs():

    template = session.execute("""select * from dogApi.dogs""")
    all = []

    for dog in template:
        all.append(dog.name)

    return jsonify(all), 200
    


# Retrieving specific items in database, without the need for authorization
@app.route('/<name>/<name2>', methods=['GET'])
def twoNames(name,name2):

    nameOrder1 = session.execute("""select * from dogApi.dogs where name='{0} {1}'""".format(name,name2))
    nameOrder2 = session.execute("""select * from dogApi.dogs where name='{0} {1}'""".format(name2,name))
    result = []
    result2 = []

    for r in nameOrder1:
        result.append(r.name)
    for r2 in nameOrder2:
        result2.append(r2.name)

    if result==[]:
        return 'Not found', 404

    elif result!=[] and result2==[]:
        return jsonify(result), 200

    else:
        return jsonify(result2), 200



# Retrieving all items in database, without the need for authorization
@app.route('/<name>', methods=['GET'])
def oneName(name):

    rows = session.execute("""select * from dogApi.dogs where name='{0}'""".format(name))
    result = []

    for r in rows:
        result.append({'name':r.name})

    if result==[]:
        return 'Not found', 404
        
    else:
        return jsonify(result), 200


# Authorization page for posting new items
@app.route('/post')
def post():

    return render_template('post.html')
    
    

# Checking for valid login and storing new items
@app.route('/post/login', methods=['GET','POST'])
def newpost():

    username = request.form['username']
    password = request.form['password']
    name = request.form['name']

    rows = session1.execute("""select username from login.users where username='{0}' and password='{1}'""".format(username,password))
    check = []
    for r in rows:
        check.append(r.username)

    if check==[]:
        return 'Invalid username and/ or password', 404

    else:

        row = session.execute("""select * from dogApi.dogs where name='{0}'""".format(name))
        result = []

        for r in row:
            result.append(r.name)

        if result==[]:

            dog = name.split(" ")

            if len(dog)==2:

                dog1 = dog[0]
                dog2 = dog[1]

                data = requests.get('https://dog.ceo/api/breeds/list/all').json()
                for breed in data['message']:
                    if breed==dog1 or breed==dog2:
                        for subbreed in data['message'][breed]:
                            if subbreed==dog1 or subbreed==dog2:
                                session.execute("""insert into dogApi.dogs(name) values('{0} {1}')""".format(subbreed,breed))
                                return 'Success! Your input "{0} {1}" has been added.'.format(subbreed,breed), 200
                else:
                    return 'Breed not valid', 404

            elif len(dog)==1:

                dog = dog[0]

                data = requests.get('https://dog.ceo/api/breeds/list/all').json()
                for breed in data['message']:
                    if breed==dog:
                        session.execute("""insert into dogApi.dogs(name) values('{0}')""".format(breed))
                        return 'Success! Your input "{0}" has been added.'.format(breed), 200

                    else:
                        return 'Breed not valid', 404

                else:
                    return 'Breed not valid', 404

            else:
                return 'This breed has already been added', 404



# Authorization page for updating items
@app.route('/put')
def putpage():

    return render_template('put.html')



# Checking for valid login and redirecting to seperate put method as HTML forms do not support PUT methods
@app.route('/put/login', methods=['GET','POST'])
def put():

    username = request.form['username']
    password = request.form['password']
    name = request.form['name']
    name2 = request.form['name2']

    rows = session1.execute("""select username from login.users where username='{0}' and password='{1}'""".format(username,password))

    check = []
    for r in rows:
        check.append(r.username)

    if check!=[]:
        return redirect(url_for('newput', name=name, name2=name2))

    else:
        return 'Invalid username and/ or password', 404



# Updating items in database
@app.route('/put/login/<name>/<name2>', methods=['GET','PUT'])
def newput(name,name2):

    row = session.execute("""select * from dogApi.dogs where name='{0}'""".format(name))
    result=[]

    for r in row:
        result.append(r.name)

    if result==[]:
        return 'Item to change does not exist in database', 404

    else:
        session.execute("""delete from dogApi.dogs where name='{0}'""".format(name))
        session.execute("""insert into dogApi.dogs(name) values('{0}')""".format(name2))
        return 'OK', 200



# Authorization page for updating items
@app.route('/delete')
def deletepage():

    return render_template('delete.html')



# Checking for valid login and redirecting to seperate delete method as HTML forms do not support DELETE methods
@app.route('/delete/login', methods=['GET','POST'])
def delete():

    username = request.form['username']
    password = request.form['password']
    name = request.form['name']

    rows = session1.execute("""select username from login.users where username='{0}' and password='{1}'""".format(username,password))

    check = []
    for r in rows:
        check.append(r.username)

    if check!=[]:
        return redirect(url_for('newdelete', name=name))

    else:
        return 'Invalid username and/ or password'


# Deleting items in database
@app.route('/delete/login/<name>', methods=['GET','DELETE'])
def newdelete(name):

    row = session.execute("""select * from dogApi.dogs where name='{0}'""".format(name))
    result=[]

    for r in row:
        result.append(r.name)

    if result==[]:
        return 'Item to delete is not in database'

    else:
        session.execute("""delete from dogApi.dogs where name='{0}'""".format(name))
        return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)