# ssh_mysql_connect
Code for connecting python to a MySQL server behind an SSH tunnel

Sometimes, the database you want to connect to in Python is located behind an SSH tunnel.
Using the files here, you can set establish the SSH connection and connect to the database all from within Python.

I have this set up such that both the config file and the connector methods are separate from the Python script you are working in.
However, you can also copy the mypython_dbconnector.py file into a Jupyter Notebook and not worry about importing it. I like the
separation to keep the ipynb file clean.

Note: this code is adapted from https://practicaldatascience.co.uk/data-science/how-to-connect-to-mysql-via-an-ssh-tunnel-in-python
