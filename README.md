# Project1

### How to run Flask (ik its heading 3 deal with it)

To compile this code first clone the repository:
```
git clone https://github.com/cvyndy/Project1
```
Create a virtual environment to download flask
```
python -m venv venv
```
Activate the virtual environment
```
source venv\Scripts\activate
```
Download requirements.txt
```
pip install -r requirements.txt
```
After everything is setup, install flask
```
pip install flask
```
To run the app do
```
flask run
```
### How to connect to the database
To create a PostgreSQL Database:
```
sudo -u postgres psql
```
```
postgres=# CREATE DATABASE flask_db;
```
Enter Username and Password and then grant privileges
```
postgres=# GRANT ALL PRIVILEGES ON DATABASE flask_db TO username;
```
Also, make an .env file to hide your credentials
```
DATABASE_URL = postgresql://username:password@localhost/name_of_db
```

After you setup your database, run the app to test the database
```
flask run
```
At [http://localhost:5000/test-db](http://localhost:5000/test-db), the database will show you if the connection is successful or not.
