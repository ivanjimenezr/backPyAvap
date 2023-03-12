from sshtunnel import SSHTunnelForwarder
import mysql.connector
import os
from dotenv import dotenv_values,load_dotenv
import os

load_dotenv('.env')

try:
    server=SSHTunnelForwarder(('217.160.32.229',22),
                              
                              ssh_username=os.environ.get("ssh_username"),
                              ssh_password=os.environ.get("ssh_password"),
                              ssh_proxy_enabled=os.environ.get("ssh_proxy_enabled"),
                              remote_bind_address=('localhost',3306)
                              )
    server.start()
    print('Server started through ssh')

    con= mysql.connector.connect(
        database=os.environ.get("database"),
        host=os.environ.get("host"),
        user=os.environ.get("user"),
        password=os.environ.get("password"),
        auth_plugin=os.environ.get("auth_plugin"),
        charset='utf8',
        port=server.local_bind_port,
        connection_timeout=180
    )
    if con != None:
        print('To mysql Database Connected')
    else:
        print('Mysql not connected')

    cursor=con.cursor()
    # with con.cursor() as cursor:
    def get_all_inmuebles():
        query = "SELECT * FROM avap.inmuebles"
    
    # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)
        cursor.execute(query)
        db = cursor.fetchall()
        return db
    
    def get_inmueble_id(id):
        query = f"SELECT * FROM avap.inmuebles WHERE id={id}"
    
    # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)
        cursor.execute(query)
        db = cursor.fetchone()
        return db

    # jj = get_all_inmuebles()
    # print(jj)

    inmueble = get_inmueble_id(1)
    print(inmueble)

    
    ################################
    ## IMPORTANT ##
    ################################
    # Call upon the class like this:

    # import db
    # inmuebles = db.get_all_inmuebles()
   

except BaseException as e:
    print('El problema con --> ', e)

finally:
    if server:
        print('Finished')
        server.close