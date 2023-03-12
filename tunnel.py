from sshtunnel import SSHTunnelForwarder

try:
    server=SSHTunnelForwarder(('217.160.32.229',22),
                              ssh_username='root',
                              ssh_password='!ov1I%fN62',
                              ssh_proxy_enabled=True,
                              remote_bind_address=('localhost',3306))
    server.start()
    print('Server started')
except BaseException as e:
    print('El problema con --> ', e)

finally:
    if server:
        server.close