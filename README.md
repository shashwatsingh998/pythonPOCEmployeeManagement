This project uses the concepts from  official flask documentation. https://flask.palletsprojects.com/en/3.0.x/. I've tried to add most of the concepts which we can see, such as user authentication using sessions, blueprint management for auth.
Encryption for password using generate_password for the documentation. This project was inspired by the original Flask Blog tutorial which incorporated these features. The PEP8 concepts are also utilized such as 4 space indentation, 
string linearity,naming conventions etc.
#TODO,
* we need to add a logger function which can automatically detect whether user is loggen in or not
* Give manager id attribute to the employee schema
* Build an heirarchial model for the display of organization(this will be done using $graphLookup)

Usage
```
Run Unit Tests using:
python -m unittest tests/auth_test.py
Run the project using:
python run.py

```
