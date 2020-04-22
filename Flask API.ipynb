{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Flask RESTful Web API"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Setting up server"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Things to note:\n",
    "\n",
    "I created two Cassandra instances, which was not really necessary. The difference was having two Cluster(contact_points) as opposed to one with two tables. This made the code less efficient than it could have been."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Create new directory and enter:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "mkdir miniProject\n",
    "cd miniProject"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Installing software:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "sudo apt update\n",
    "sudo apt install docker.io\n",
    "sudo apt install python3-pip"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Downloading files:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "sudo wget -O Dockerfile https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/Dockerfile\n",
    "sudo wget -O requirements.txt https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/requirements.txt\n",
    "sudo wget -O myapp.py https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/myapp.py\n",
    "sudo wget -O create.html https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/create.html\n",
    "sudo wget -O post.html https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/post.html\n",
    "sudo wget -O put.html https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/put.html\n",
    "sudo wget -O delete.html https://raw.githubusercontent.com/jonilsenGithub/Flask_API/master/delete.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Enabling render_template()\n",
    "\n",
    "Making a templates folder for the render_template() method to work and moving html files that folder:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "mkdir templates\n",
    "\n",
    "mv /path/from/home/miniProject/create.html /path/from/home/miniProject/templates\n",
    "\n",
    "mv /path/from/home/miniProject/post.html /path/from/home/miniProject/templates\n",
    "\n",
    "mv /path/from/home/miniProject/put.html /path/from/home/miniProject/templates\n",
    "\n",
    "mv /path/from/home/miniProject/delete.html /path/from/home/miniProject/templates"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Create Cassandra databases:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "sudo docker pull cassandra:latest\n",
    "sudo docker run --name miniProject -p 9042:9042 -d cassandra:latest\n",
    "\n",
    "sudo docker exec -it miniProject cqlsh\n",
    "\n",
    "CREATE KEYSPACE dogApi WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};\n",
    "CREATE TABLE dogApi.dogs(name text PRIMARY KEY);\n",
    "\n",
    "exit"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "sudo docker run --name login -p 9043:9043 -d cassandra:latest\n",
    "\n",
    "sudo docker exec -it login cqlsh\n",
    "\n",
    "CREATE KEYSPACE login WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1};\n",
    "CREATE TABLE login.users(username VARCHAR, password VARCHAR, primary key(username,password));\n",
    "\n",
    "exit"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Running application from localhost:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "sudo pip3 install -r requirements.txt\n",
    "sudo python3 miniProject.py"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Running application as a Docker image"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "sudo docker build . --tag=cassandrarest:v1\n",
    "sudo docker run -p 80:80 cassandrarest:v1"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## API Documentation"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### GET\n",
    "\n",
    "Terminal command to check database content\n",
    "\n",
    "Returns all dogs currently in cassandra database dogApi.dogs\n",
    "\n",
    "Returns status code 200, example:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "curl -i ec2-35-170-245-138.compute-1.amazonaws.com/all"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### POST\n",
    "\n",
    "Terminal command to add new user\n",
    "\n",
    "Returns 'Thank you' and status code 200 if OK \n",
    "\n",
    "Returns status code 404 if username is already in use\n",
    "\n",
    "Example:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "curl -X POST -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/newuser"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### POST\n",
    "\n",
    "Terminal command to add new dogs to database\n",
    "\n",
    "Returns status code 200 if OK\n",
    "\n",
    "Returns status code 404 if there are problems such as invalid login, not valid breed after checking it in external API or the breed has already been added\n",
    "\n",
    "Example:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "curl -X POST -F 'name=golden retriever' -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/post/login"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "curl -X POST -F 'name=boxer' -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/post/login"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### GET\n",
    "\n",
    "Terminal command to search database dogApi.dogs for specific content\n",
    "\n",
    "Returns all matching results with status code 200\n",
    "\n",
    "Returns status code 404 if not found\n",
    "\n",
    "Example:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "curl -i ec2-35-170-245-138.compute-1.amazonaws.com/golden/retriever"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "curl -i ec2-35-170-245-138.compute-1.amazonaws.com/boxer"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### PUT\n",
    "\n",
    "Terminal command to update added dog\n",
    "\n",
    "Returns 'OK' if successful. Status code was not added.\n",
    "\n",
    "Returns status code 404 if item to change was not found\n",
    "\n",
    "Example:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "curl -X PUT -F 'name=boxer' -F 'name2=irish setter' -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/put/login/boxer/irish%20setter"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### DELETE\n",
    "\n",
    "Terminal command to add delete dog\n",
    "\n",
    "Returns status code 200 if successful\n",
    "\n",
    "Returns 'Item to delete is not in database' if not found, but no status code.\n",
    "\n",
    "Example:"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "curl -X DELETE -F 'name=boxer' -F 'username=jonas' -F 'password=nilsen' http://ec2-35-170-245-138.compute-1.amazonaws.com/delete/login/irish%20setter"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
