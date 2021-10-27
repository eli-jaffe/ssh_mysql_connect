import pandas as pd
import matplotlib.pyplot as plt
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder

import config


# define the functions we will be using

def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.
    
    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """
    
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
    global tunnel
    tunnel = SSHTunnelForwarder(
        (config.ssh_host, 22),
        ssh_username = config.ssh_username,
        ssh_password = config.ssh_password,
        remote_bind_address = ('127.0.0.1', 3306)
    )
    
    tunnel.start()
    
    
def mysql_connect():
    """Connect to a MySQL server using the SSH tunnel connection
    
    :return connection: Global MySQL database connection
    """
    
    global connection
    
    connection = pymysql.connect(
        host='127.0.0.1',
        user=config.database_username,
        password=config.database_password,
        database=config.database_name,
        port=tunnel.local_bind_port
    )
    

def run_query(sql):
    """Runs a given SQL query via the global database connection.
    
    :param sql: MySQL query
    :return: Pandas dataframe containing results
    """
    
    return pd.read_sql_query(sql, connection)


def mysql_disconnect():
    """Closes the MySQL database connection.
    """
    
    connection.close()
    
    
def close_ssh_tunnel():
    """Closes the SSH tunnel connection.
    """
    
    tunnel.close
