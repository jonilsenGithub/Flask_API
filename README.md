# Flask_API

## Setting up server

### Things to note

I created two Cassandra instances, which was not really necessary. The difference was having two Cluster(contact_points) as opposed to one with two tables. This made the code less efficient than it could have been.

#### Create new directory and enter:

```
mkdir miniProject
cd miniProject
```

#### Installing software:

````
sudo apt update
sudo apt install docker.io
sudo apt install python3-pip
````

#### Downloading files:

````
sudo wget -O Dockerfile https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/Dockerfile
sudo wget -O requirements.txt https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/requirements.txt
sudo wget -O myapp.py https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/myapp.py
sudo wget -O create.html https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/create.html
sudo wget -O post.html https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/post.html
sudo wget -O put.html https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/put.html
sudo wget -O delete.html https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/delete.html
````

#### Enabling render_template()

Making a templates folder for the render_template() method to work and moving html files that folder:

```
mkdir templates

mv /path/from/home/miniProject/create.html /path/from/home/miniProject/templates

mv /path/from/home/miniProject/post.html /path/from/home/miniProject/templates

mv /path/from/home/miniProject/put.html /path/from/home/miniProject/templates

mv /path/from/home/miniProject/delete.html /path/from/home/miniProject/templates
```

#### Create Cassandra databases:

```
sudo docker pull cassandra:latest
sudo docker run --name miniProject -p 9042:9042 -d cassandra:latest

sudo docker exec -it miniProject cqlsh

CREATE KEYSPACE dogApi WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};
CREATE TABLE dogApi.dogs(name text PRIMARY KEY);

exit
```

```
sudo docker run --name login -p 9043:9043 -d cassandra:latest

sudo docker exec -it login cqlsh

CREATE KEYSPACE login WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};
CREATE TABLE login.users(username VARCHAR, password VARCHAR, primary key(username,password));

exit
```

#### Running application from localhost:

```
sudo pip3 install -r requirements.txt
sudo python3 miniProject.py
```

#### Running application as a Docker image:

```
sudo docker build . --tag=miniproject:v1
sudo docker run -p 80:80 miniproject:v1
```

## API Documentation

#### GET

Terminal command to check database content

Returns all dogs currently in cassandra database dogApi.dogs

Returns status code 200, example:

```
curl -i ec2-35-170-245-138.compute-1.amazonaws.com/all
```

#### POST

Terminal command to add new user

Returns 'Thank you' and status code 200 if OK 

Returns status code 404 if username is already in use

Example:

```
curl -X POST -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/newuser
```

#### POST

Terminal command to add new dogs to database

Returns status code 200 if OK

Returns status code 404 if there are problems such as invalid login, not valid breed after checking it in external API or the breed has already been added

Example:

```
curl -X POST -F 'name=golden retriever' -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/post/login
```
```
curl -X POST -F 'name=boxer' -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/post/login
```

#### GET

Terminal command to search database dogApi.dogs for specific content

Returns all matching results with status code 200

Returns status code 404 if not found

Example:

```
curl -i ec2-35-170-245-138.compute-1.amazonaws.com/golden/retriever
```

```
curl -i ec2-35-170-245-138.compute-1.amazonaws.com/boxer
```

#### PUT

Terminal command to update added dog

Returns 'OK' if successful. Status code was not added.

Returns status code 404 if item to change was not found

Example:

```
curl -X PUT -F 'name=boxer' -F 'name2=irish setter' -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/put/login/boxer/irish%20setter
```

#### DELETE

Terminal command to add delete dog

Returns status code 200 if successful

Returns 'Item to delete is not in database' if not found, but no status code.

Example:

```
curl -X DELETE -F 'name=boxer' -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/delete/login/irish%20setter
```
