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
                            #   remote_bind_address=os.environ.get("remote_bind_address")
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
    if con!=None:
        print('To mysql Database Connected')
    else:
        print('Mysql not connected')

    cursor=con.cursor()
    # with con.cursor() as cursor:
            
    query = "SELECT * FROM inmuebles"
    # global connection timeout arguments
    global_connect_timeout = 'SET GLOBAL connect_timeout=180'
    global_wait_timeout = 'SET GLOBAL connect_timeout=180'
    global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

    cursor.execute(global_connect_timeout)
    cursor.execute(global_wait_timeout)
    cursor.execute(global_interactive_timeout)
    cursor.execute(query)
    db = cursor.fetchall()
    # print("Resultados de db: ", db)
    for row in db:
        print(row[1])
    # cursor.execute('SELECT * FROM inmuebles')
    # rows=cursor.fetchall()
    # print(rows)
# for row in rows:
#     print(row)

except BaseException as e:
    print('El problema con --> ', e)

finally:
    if server:
        print('Finished')
        server.close