import sshtunnel
# import mysql.connector
import os
from dotenv import dotenv_values,load_dotenv
import os
import json
import pymysql

load_dotenv('.env')

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

try:
    server=sshtunnel.SSHTunnelForwarder(('217.160.32.229',22),
                              
                              ssh_username=os.environ.get("ssh_username"),
                              ssh_password=os.environ.get("ssh_password"),
                              ssh_proxy_enabled=os.environ.get("ssh_proxy_enabled"),
                              remote_bind_address=('localhost',3306)
                              )
    server.start()
    print('Server started through ssh')

    con= pymysql.connect(
        database=os.environ.get("database"),
        host=os.environ.get("host"),
        user=os.environ.get("user"),
        password=os.environ.get("password"),
        charset='utf8',
        port=server.local_bind_port,
        
        cursorclass=pymysql.cursors.DictCursor
        
        
    )
    if con != None:
        print('To mysql Database Connected')
    else:
        print('Mysql not connected')

    cursor= con.cursor()
    # with con.cursor() as cursor:

    #### INMUEBLES #####
    ####################

    # Todos los inmuebles
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
    
    # Vendedores asociados a un inmueble
    def get_vendedor_id_inmuebles(id):
        query = f"SELECT * FROM avap.vendedores where id IN (SELECT idVendedor FROM avap.asociaciones WHERE idInmueble = {id});"
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
    
    # Compradores asociados a un inmueble
    def get_comprador_id_inmuebles(id):
        query = f"SELECT * FROM avap.compradores where id IN (SELECT idComprador FROM avap.asociaciones WHERE idInmueble = {id});"
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
    
    #Inmuebles por ID
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

    #Nuevo inmueble
    def create_inmueble(inmueble):
        print('ooooooooo')
        tipologia = inmueble['tipologia']
        provincia = inmueble['provincia']
        municipio = inmueble['municipio']
        direccion = inmueble['direccion']
        refCatastral = inmueble['refCatastral'] 
        superficie = inmueble['superficie'] 
        descripNotaSimple = inmueble['descripNotaSimple'] 
        inscripcionRegistro = inmueble['inscripcionRegistro']
        cru = inmueble['cru'] 
        precio = inmueble['precio'] 
        finalizado = inmueble['finalizado']
        llaves = inmueble['llaves']
        fechaAlta= inmueble['fechaAlta']
        comisionVen= inmueble['comisionVen']
        comisionCom= inmueble['comisionCom']
        observaciones= inmueble['observaciones']
        comercial= inmueble['comercial']
        dormitorios= inmueble['dormitorios']
        banos= inmueble['banos']
        exterior= inmueble['exterior']
        operacion= inmueble['operacion']
        cee= inmueble['cee']
        descripcion= inmueble['descripcion']
        ascensor= inmueble['ascensor']
        condiPrestamo= inmueble['condiPrestamo']
        if condiPrestamo:
            condiPrestamo = 1
        else:
            condiPrestamo = 0
        importeArras= inmueble['importeArras']

        query = f"INSERT INTO avap.inmuebles (tipologia, provincia, municipio, direccion, refCatastral, superficie, descripNotaSimple, inscripcionRegistro, cru, precio, finalizado, llaves, fechaAlta, comisionVen,comisionCom,observaciones,comercial,dormitorios,banos,exterior,operacion,cee,descripcion,ascensor,condiPrestamo,importeArras) VALUES ('{tipologia}', '{provincia}', '{municipio}', '{direccion}', '{refCatastral}', '{superficie}', '{descripNotaSimple}', '{inscripcionRegistro}', '{cru}', '{precio}', {finalizado}, {llaves}, '{fechaAlta}', {comisionVen}, {comisionCom}, '{observaciones}', '{comercial}', {dormitorios}, {banos}, '{exterior}', '{operacion}', '{cee}', '{descripcion}', '{ascensor}', {condiPrestamo}, {importeArras});"
        print('query insert', query)
        cursor.execute(query)
        # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)
        con.commit()
        idNewInmueble = cursor.lastrowid
        
        

        msn = f'Se ha creado un inmueble con id {idNewInmueble}'

        response = {
            "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
            },
            "statusCode": 200,
            'body': json.dumps({"status":"suscess","results":msn})
            }
        return response

        

    #Update inmueble
    def up_inmueble_id(id, inmueble):
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
        if db:

            tipologia = inmueble['tipologia']
            provincia = inmueble['provincia']
            municipio = inmueble['municipio']
            direccion = inmueble['direccion']
            refCatastral = inmueble['refCatastral'] 
            superficie = inmueble['superficie'] 
            descripNotaSimple = inmueble['descripNotaSimple'] 
            inscripcionRegistro = inmueble['inscripcionRegistro']
            cru = inmueble['cru'] 
            precio = inmueble['precio'] 
            finalizado = inmueble['finalizado']
            llaves = inmueble['llaves']
            fechaAlta= inmueble['fechaAlta']
            comisionVen= inmueble['comisionVen']
            comisionCom= inmueble['comisionCom']
            observaciones= inmueble['observaciones']
            comercial= inmueble['comercial']
            dormitorios= inmueble['dormitorios']
            banos= inmueble['banos']
            exterior= inmueble['exterior']
            operacion= inmueble['operacion']
            cee= inmueble['cee']
            descripcion= inmueble['descripcion']
            ascensor= inmueble['ascensor']
            condiPrestamo= inmueble['condiPrestamo']
            if condiPrestamo:
                condiPrestamo = 1
            else:
                condiPrestamo = 0
            importeArras= inmueble['importeArras']

            compradores = inmueble['compradores']
            vendedores = inmueble['vendedores']

            if compradores:
                queryDel = f"DELETE FROM avap.asociaciones WHERE idinmueble = {id} and idComprador IS NOT NULL;"
                cursor.execute(queryDel)
                con.commit()
                for comprador in compradores:
                    idComprador = comprador['id']
                    query = f"INSERT INTO avap.asociaciones (idinmueble, idComprador) VALUES ('{id}', '{idComprador}');"
                    cursor.execute(query)
                    con.commit()

            if vendedores:
                queryDel = f"DELETE FROM avap.asociaciones WHERE idinmueble = {id} and idVendedor IS NOT NULL;"
                cursor.execute(queryDel)
                con.commit()
                for vendedor in vendedores:
                    idVendedor = vendedor['id']
                    query = f"INSERT INTO avap.asociaciones (idinmueble, idVendedor) VALUES ('{id}', '{idVendedor}');"
                    cursor.execute(query)
                    con.commit()
            
            query1 = f"UPDATE avap.inmuebles SET tipologia = '{tipologia}', provincia = '{provincia}', municipio = '{municipio}', direccion = '{direccion}', refCatastral = '{refCatastral}', superficie = '{superficie}', descripNotaSimple = '{descripNotaSimple}', inscripcionRegistro = '{inscripcionRegistro}', cru = '{cru}', precio = '{precio}', finalizado = {finalizado}, llaves = {llaves}, fechaAlta = '{fechaAlta}', comisionVen = '{comisionVen}', comisionCom = '{comisionCom}', observaciones = '{observaciones}', comercial = '{comercial}', dormitorios = '{dormitorios}', banos = '{banos}', exterior = '{exterior}', operacion = '{operacion}', cee = '{cee}', descripcion = '{descripcion}', ascensor = '{ascensor}', condiPrestamo = {condiPrestamo}, importeArras = {importeArras} WHERE id = {id};"
            cursor.execute(query1)
            con.commit()

        return
    
    #Finalizar inmueble
    def finalizar_inmueble(id, inmuebleFin):
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
        if db:
            inmuebleFin = dict(inmuebleFin)
            estadoFin = inmuebleFin['finalizado']

            print('EstadoFinnnn',estadoFin )
            
            query = f"UPDATE avap.inmuebles SET finalizado = {estadoFin} WHERE id = {id};"
            print('query insert', query)
            cursor.execute(query)
            con.commit()

            msn = f'Se ha cambiado el estado de finalizado el inmueble con id {id}'

            response = {
                "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Credentials': True
                },
                "statusCode": 200,
                'body': json.dumps({"status":"suscess","results":msn})
                }
            return response

    #### VENDEDORES #####
    ####################

# Todos los vendedores
    def get_all_vendedores():
        query = "SELECT * FROM avap.vendedores"
    
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
    
# Vendedor por Id
    def get_vendedores_id(id):
        query = f"SELECT * FROM avap.vendedores where id = {id} "
    
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

# Actualizar un vendedor
    def up_vendedor_id(id, vendedor):
        query = f"SELECT * FROM avap.vendedores WHERE id={id}"
    
    # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)
        cursor.execute(query)
        db = cursor.fetchone()
        if db:

            nombre = vendedor['nombre']
            dni = vendedor['dni']
            direccion = vendedor['direccion']
            email = vendedor['email']
            telefono = vendedor['telefono'] 
            fechaNacimiento = vendedor['fechaNacimiento'] 
            estadoCivil = vendedor['estadoCivil'] 
            fechaAlta = vendedor['fechaAlta']
            finalizado = vendedor['finalizado'] 
            municipio = vendedor['municipio'] 
            provincia = vendedor['provincia']
            
            query1 = f"UPDATE avap.vendedores SET nombre = '{nombre}', dni = '{dni}', direccion = '{direccion}', email = '{email}', telefono = '{telefono}', fechaNacimiento = '{fechaNacimiento}', estadoCivil = '{estadoCivil}', fechaAlta = '{fechaAlta}', municipio = '{municipio}', finalizado = {finalizado}, provincia = '{provincia}' WHERE id = {id};"
            cursor.execute(query1)
            con.commit()

        return   
    
    def createAsociaVendedor(id,vendedor):


        query = f"SELECT * FROM avap.asociaciones where idInmueble = {id} and idVendedor = {vendedor['id']}"
        # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)
        cursor.execute(query)
        found = cursor.fetchone()
        if not found:
            print('no existe asocio')
            query = f"INSERT INTO avap.asociaciones (idInmueble, idVendedor) VALUES ({id}, {vendedor['id']});"
            print('query insert', query)
            cursor.execute(query)
            con.commit()
            msn = 'No esta asociado, creo la asociación'
        else:
            print('Ya existe la asociacion')
            print(found)
            msn = 'Ya existe la asociacion'


        return msn
    
    

    #### COMPRADORES #####
    ####################

# Todos los compradores
    def get_all_compradores():
        query = "SELECT * FROM avap.compradores"
    
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

# Asociar compradores a inmuebles
    def createAsociaComprador(id,comprador):


        query = f"SELECT * FROM avap.asociaciones where idInmueble = {id} and idComprador = {comprador['id']}"
        # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)
        cursor.execute(query)
        found = cursor.fetchone()
        if not found:
            print('no existe asocio')
            query = f"INSERT INTO avap.asociaciones (idInmueble, idComprador) VALUES ({id}, {comprador['id']});"
            print('query insert', query)
            cursor.execute(query)
            con.commit()
            msn = 'No esta asociado, creo la asociación'
        else:
            print('Ya existe la asociacion')
            print(found)
            msn = 'Ya existe la asociacion'


        return msn

    #### COMERCIALES #####
    ####################
# Todos los comerciales
    def get_all_comerciales():
        query = "SELECT * FROM avap.comerciales"
    
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
    


    #### USUARIOS #####
    ####################

# Encontrar usuario para Login
    def find_usuario(user):
        print('user', user)
        email = user['email']
        password = user['password']

        query = f"SELECT * FROM avap.usuarios where email = '{email}' and password = '{password}'"
        print('query insert', query)
        cursor = con.cursor()
        
        # global connection timeout arguments
        global_connect_timeout = 'SET GLOBAL connect_timeout=180'
        global_wait_timeout = 'SET GLOBAL connect_timeout=180'
        global_interactive_timeout = 'SET GLOBAL connect_timeout=180'

        cursor.execute(global_connect_timeout)
        cursor.execute(global_wait_timeout)
        cursor.execute(global_interactive_timeout)
        cursor.execute(query)
        db = cursor.fetchone()

        if db:
            print('encontrado')
            return True
        else:
            return False

  

except BaseException as e:
    print('El problema con --> ', e)

finally:
    if server:
        print('Finished')
        server.close