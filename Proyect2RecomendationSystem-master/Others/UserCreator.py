from py2neo import Graph

# ------------------------------------ FUNCIONES PARA CONECTARSE A NEO4J ------------------------------------

# ------------------------------------ FUNCION PARA CREAR UN NUEVO USUARIO EN LA BASE DE DATOS ------------------------------------
def create_user(username: str,
                password: str,
                nombre: str,
                apellido: str,
                Sector_Interes1:str,
                Sector_Interes2:str,
                Sector_Interes3:str,
                Riesgo:int, 
                Rentabiidad: int,
                Tamanio: int,
                Libros: int,
                Agresividad: int,                
                graph: Graph):
    try:

        # print("Ingreso1")
        graph.run("""
        CREATE (p:User{name:$username1,
        password:$password1,
        nombre:$nombre1, 
        apellido:$apellido1,
        Sector_Interes1:($Sector1),
        Sector_Interes2:($Sector2),
        Sector_Interes3:($Sector3),
        Riesgo:toInteger($riesgo),
        Rentabilidad:toInteger($rentabilidad),
        Tamanio:toInteger($tamanio),
        Libros:toInteger($libro),
        Agresividad:toInteger($agresividad),
        loged:FALSE})
        """,
        username1=username,
        password1=password,
        nombre1=nombre, 
        apellido1=apellido,
        Sector1=Sector_Interes1,
        Sector2=Sector_Interes2,
        Sector3=Sector_Interes3,
        riesgo=Riesgo,
        rentabilidad=Rentabiidad,
        tamanio=Tamanio,
        libro=Libros,
        agresividad=Agresividad
        )
        # print("Ingreso2")
        # Crear sector de Interes
        graph.run(
            """
            MATCH (a:User), (b:Business)
            WHERE a.name = $username1 AND b.SECTOR = a.Sector_Interes1 OR a.name = $username1 AND b.SECTOR = a.Sector_Interes2 OR a.name = $username1 AND b.SECTOR = a.Sector_Interes3 
            CREATE (a)-[r:Sector_De_Interes{name: a.name+'<->'+b.name}]->(b)
            """,
            username1=username
        )

       # Crear riesgo de interes
        # print("Ingreso3")
        graph.run(
            """
            MATCH (a:User), (b:Business)
            WHERE a.name = $username1 AND (a.Riesgo>5 AND b.VAR=-10000 OR a.Riesgo>=0 AND a.Riesgo<1 AND b.VAR<=0.0010 OR a.Riesgo>=1 AND a.Riesgo<2 AND b.VAR<0.0015 AND b.VAR>=0.0010 OR a.Riesgo>=2 AND a.Riesgo<3 AND b.VAR<0.004 AND b.VAR>=0.0015 OR  a.Riesgo>=3 AND a.Riesgo<4 AND b.VAR<0.006 AND b.VAR>=0.004 OR  a.Riesgo>=4 AND a.Riesgo<5 AND b.VAR<0.007 AND b.VAR>=0.006 OR a.Riesgo>=5 AND b.VAR>0.007 ) 
            CREATE (a)-[r:Riesgo_De_Interes{name:a.name+'<->'+b.name}]->(b)
            """,
            username1=username
        )        
        # print("Ingreso4")
        graph.run(
            """
            MATCH (a:User), (b:Business)
            WHERE a.name = $username1 AND (a.Rentabilidad=0 AND a.Rentabilidad>1 AND b.PER>=0 AND b.PER<300 OR a.Rentabilidad=1 AND b.PER<800 AND b.PER>=300 OR a.Rentabilidad<=2 AND a.Rentabilidad>3 AND b.PER<1400 AND b.PER>=800 OR  a.Rentabilidad<=3 AND a.Rentabilidad>4 AND b.PER<2000 AND b.PER>=1400 OR  a.Rentabilidad<=4 AND a.Rentabilidad>5 AND b.PER>=2000 AND b.PER<5000 OR a.Rentabilidad>=5 AND b.PER>=5000 )
            CREATE (a)-[r:Rentabilidad_De_Interes{name:a.name+'<->'+b.name}]->(b)
            """,
            username1=username
        )
        
        # print("Ingreso5")
        graph.run(
            """
            MATCH (a:User), (b:Business)
            WHERE a.name = $username1 AND (a.Tamanio<=0 AND a.Tamanio>1 AND b.COTIZACION<700 OR a.Tamanio=1  AND b.COTIZACION<4000 AND b.COTIZACION>=700 OR a.Tamanio=2 AND b.COTIZACION<12000 AND b.COTIZACION>=4000 OR  a.Tamanio=3 AND b.COTIZACION<18000 AND b.COTIZACION>=12000 OR  a.Tamanio=4 AND b.COTIZACION>=18000 AND b.COTIZACION<20000 OR a.Tamanio=5 AND b.COTIZACION>=20000 )
            CREATE (a)-[r:Tamanio_De_Interes{name:a.name+'<->'+b.name}]->(b)
            """,
            username1=username
        )


        # print("Ingreso7")
        graph.run(
            """
            MATCH (a:User), (b:Business)
            WHERE a.name = $username1 AND (a.Libros=0 AND b.PVC=-10000 
            OR a.Libros=1  AND b.PVC<100 OR a.Libros=2 AND b.PVC<300 AND b.PVC>=100 
            OR  a.Libros=3 AND b.PVC<700 AND b.PVC>=300 OR  a.Libros=4 AND b.PVC>=700 AND b.PVC<800 OR a.Libros=5 AND b.PVC>=800 )
            CREATE (a)-[r:Relacion_Con_Libros_De_Interes{name:a.name+'<->'+b.name}]->(b)
            """,
            username1=username
        )

        # print("Ingreso8")
        graph.run(
            """
            MATCH (a:User), (b:Business)
            WHERE a.name = $username1 AND (a.Agresividad=0 AND b.PEG<=10 OR a.Agresividad=1  
            AND b.PEG<30 AND b.PEG>10 OR a.Agresividad=2 AND b.PEG<80 AND b.PEG>=30 OR  a.Agresividad=3 AND b.PEG<150 AND b.PEG>=100 
            OR  a.Agresividad=4 AND b.PEG>=100 AND b.PEG<500 OR a.Agresividad=5 AND b.PEG>=500 )
            CREATE (a)-[r:Agresividad_Para_Invertir{name:a.name+'<->'+b.name}]->(b)
            """,
            username1=username
        )
        

        print('\nUsuario creado\n')
        
    except Exception as e:
        print('\nError al crear este usuario\n')
        print(e)



# ------------------------------------ FUNCION PARA VERIFICAR SI EL USUARIO YA EXISTE EN LA DB ------------------------------------
def username_exists(username: str, graph: Graph):
    cursor = graph.run("MATCH (p:User {name: $username1}) RETURN p.username",username1=username)
    try:
        cursor.data()[0].get('p.username')
        return True
    except Exception:
        return False



# ------------------------------------ FUNCION PARA HACER UN INICIO DE SESION ------------------------------------
def login_user(username: str, password: str, graph: Graph):
    if username_exists(username, graph):
        cursor = graph.run("MATCH (p:User {name: $username1}) RETURN p.password", username1=username)
        verify = cursor.data()[0].get('p.password')
        if verify == password:
            cursor = graph.run("""
            MATCH (n:User {name: $username1})
            SET n.loged = true
            RETURN n
            """, username1=username)
            logedin = cursor.data()[0]
            return True, logedin
    return False, {}


# ------------------------------------ PARA HACER LOGOUT ------------------------------------
def logoutuser(user: dict, graph: Graph):
    username = user.get('username')
    try:
        graph.run("""
            MATCH (n:User {name: $username1})
            SET n.loged = false
            RETURN n
            """, username1=username)
            
            
    except Exception as e:
        print(e)
        print('Error')


# ------------------------------------ FUNCION CON EL ALGORITMO PARA HACER LA RECOMENDACION DE EMPRESAS------------------------------------
def search_Business(user: dict, graph: Graph):
    Relacion = graph.run("""Match (a:User), (b:Business)  
    Where a.name = $username 
    AND (  (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true AND (exists( (a)-[:Sector_De_Interes]->(b) ))=true 
    OR  (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true OR (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true AND (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true AND (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true 
    OR (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true AND (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true 
    OR (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true AND (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true 
    OR (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true AND (exists( (a)-[:Rentabilidad_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Sector_De_Interes]->(b) ))=true AND (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true AND (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true AND (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true AND (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true AND (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true 
    OR (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true AND (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true AND (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true 
    OR (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true AND (exists( (a)-[:Rentabilidad_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Rentabilidad_De_Interes]->(b) ))=true AND (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true AND (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true 
    OR (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true AND (exists( (a)-[:Riesgo_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true AND (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true AND (exists( (a)-[:Relacion_Con_Libros_De_Interes]->(b) ))=true 
    OR (exists( (a)-[:Rentabilidad_De_Interes]->(b) ))=true AND (exists( (a)-[:Agresividad_Para_Invertir]->(b) ))=true AND (exists( (a)-[:Tamanio_De_Interes]->(b) ))=true )
    return b
    """, username = user)
    va = Relacion.data()
    # print(va)
    # print("hola")
    for k in range (0, len(va)):
        lista = list(va[k].values())    
        # print(lista)
        # print(lista[0].items())
        lista1 = list(lista[0].items())
        # print(lista1)
        for d in range(0, len(lista1)):
            # print(lista1[d])
            if (lista1[d][0]=="name"):
                print(str(k)+"-"+lista1[d][1])
    # print(Relacion.data()[0].items())
    
    # for d in Relacion.data()[0].items:
    #     print(d)
# Sector_De_Interes
# Riesgo_De_Interes
# Rentabilidad_De_Interes
# Tamanio_De_Interes
# Relacion_Con_Libros_De_Interes
# Agresividad_Para_Invertir

# OR (exists( (a)-[:]->(b) ))=true AND (exists( (a)-[:]->(b) ))=true AND (exists( (a)-[:]->(b) ))=true
# OR (exists( (a)-[:]->(b) ))=true AND (exists( (a)-[:]->(b) ))=true AND (exists( (a)-[:]->(b) ))=true
# OR (exists( (a)-[:]->(b) ))=true AND (exists( (a)-[:]->(b) ))=true AND (exists( (a)-[:]->(b) ))=true
# OR (exists( (a)-[:]->(b) ))=true AND (exists( (a)-[:]->(b) ))=true AND (exists( (a)-[:]->(b) ))=true



# ------------------------------------ FUNCION PARA RECOMENDAR PERSONAS ------------------------------------
def search_Partner(user: dict, graph: Graph):
    Relacion = graph.run("""Match (a:User), (b:User)  
    Where a.name = $username AND b.name<>a.name AND ( a.Riesgo=b.Riesgo AND a.Sector_Interes1=b.Sector_Interes1 AND  a.Rentabilidad = b.Rentabilidad 
    OR a.Riesgo=b.Riesgo AND a.Sector_Interes2=b.Sector_Interes2 AND  a.Rentabilidad = b.Rentabilidad 
    OR a.Riesgo=b.Riesgo AND a.Sector_Interes3=b.Sector_Interes3 AND  a.Rentabilidad = b.Rentabilidad 
    OR a.Riesgo=b.Riesgo AND a.Rentabilidad=b.Rentabilidad AND a.Libros=b.Libros OR a.Riesgo=b.Riesgo AND a.Agresividad=b.Agresividad AND a.Libros=b.Libros 
    OR a.Riesgo=b.Riesgo AND a.Agresividad=b.Agresividad AND a.Libros=b.Libros )
    return b
    """, username = user)
    va = Relacion.data()
    # print(va)
    # print("hola")
    for k in range (0, len(va)):
        lista = list(va[k].values())    
        # print(lista)
        # print(lista[0].items())
        lista1 = list(lista[0].items())
        # print(lista1)
        for d in range(0, len(lista1)):
            # print(lista1[d])
            if (lista1[d][0]=="name"):
                print(str(k)+"-"+lista1[d][1])
# Sector_Interes1
# Sector_Interes2
# Sector_Interes3
# Riesgo
# Rentabiidad
# Tamanio
# Libros
# Agresividad

# 


   