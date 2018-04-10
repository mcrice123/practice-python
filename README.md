# Practice Python

This is my repository for storing some simple examples of 
video-taking with Python. 

## To run test_api/server.py

Install sqlite3

After cloning this repository, execute the following commands:
```
cd practice-python
cd test_api
python server.py
```

Press `Ctrl+C` to stop the server. Navigate to http://127.0.0.1:5002 and 
if you add '/employees' to the url, you will see employee data. If you 
add '/employees/' and some existing id of an employee, you will see the 
details for that employee. If you add '/tracks', you will see various 
objects containing music track information. 