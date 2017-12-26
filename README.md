# **"projectX"** 
This project will  aggregate articles for analysis. Next step is to put the data into mongodb.
## Getting Started
You need version Python 3.6.2
### Installing
You need to install requirements for your Python. 
```
pip install -r requeriments.txt
```
Please create python file ``theguardian_site_parse/settings.py`` for connection in mongodb. For example:
```python

# settings for connection to mongodb
HOST = "hostname"
PORT = "port"
USER = "username"
PASS = "password"
DB_NAME = "db_name"
``` 
Attention, if you use OS windows, you need to change path to save dir in the file "article_parse" in func "save_in_file"
Project is developing fast, we will keep you informed.
