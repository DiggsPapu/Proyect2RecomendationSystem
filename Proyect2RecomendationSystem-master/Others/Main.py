import requests
import pandas as pd
from neo4j import GraphDatabase
from re import search
from this import d
from py2neo import Graph
from UserCreator import *
print("Bienvenidos a sistema de recomendacion de empresas basado en fundamentales de bolsa\n")
url = 'https://www.estrategiasdeinversion.com/cotizaciones/indices/ibex-35/1/desc/variacion-porcentual?gclid=CjwKCAjwgr6TBhAGEiwA3aVuIRuVssaDkelirEroGhMwXA9bgAYYLR8BFaAF_btZX0HWjj5JjKnb9xoC44wQAvD_BwE'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
# print(df)
df2 = df_list[-8]
# print(df2)
#df.to_csv(r'C:\Users\Administrator\Documents\Proyecto\Proyecto2\Proyect2RecomendationSystem-master\Others\data.csv', index=False)
greeter = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "Manager123"))
with greeter.session() as session:
    query2 = "match(a:User)-[r:Agresividad_Para_Invertir]->() delete r"
    session.run(query2)
    query2 = "match(a:User)-[r:Relacion_Con_Libros_De_Interes]->() delete r"
    session.run(query2)
    query2 = "match(a:User)-[r:Sector_De_Interes]->() delete r"
    session.run(query2)
    query2 = "match(a:User)-[r:Tamanio_De_Interes]->() delete r"
    session.run(query2)
    query2 = "match(a:User)-[r:Riesgo_De_Interes]->() delete r"
    session.run(query2)
    query2 = "match(a:Business)-[r:Rentabilidad_De_Interes]->() delete r"
    session.run(query2)
    query2 = "match(a:Business)-[r:SameSector]->() delete r"
    session.run(query2)
    query2 = "match(a:Business)-[r:SimilarBenefitRatio]->() delete r"
    session.run(query2)
    query2 = "match(a:Business)-[r:SimilarDividendos]->() delete r"
    session.run(query2)
    query2 = "match(a:Business)-[r:SimilarExpectativaDeBeneficio]->() delete r"
    session.run(query2)
    query2 = "match(a:Business)-[r:SimilarPrecioConLibros]->() delete r"
    session.run(query2)
    query2 = "match(a:Business)-[r:SimilarVariacion]->() delete r"
    session.run(query2)
    query2 = "match(a:Business)-[r:SimilarCotizacion]->() delete r"
    session.run(query2)
    query2 = "match(a:Business) delete a"
    session.run(query2)
print("Fase 1 completada\n")
n=0
names= []
pers = []
pegs = []
pvcs = []
divs = []
vars = []
sectors = []
cots = []
while (n<35):
    nombre=df['Nombre'].values[n]
    
    
    a=df['PER'].values[n]
    if (a!='-'):
        per=int(a)
    else:
        per=-10000 
    b=df['PEG'].values[n]
   
    if (b!="-"):
        peg=int(b)
    else:
        peg=-10000
    c = df['PVC'].values[n]
    if (c!="-"):
        pvc=int(c)
    else:
        pvc=-10000
    
    d=df['Dividendo'].values[n]
    d= d.replace(",",".")
    div=float(float(d[:-1])/100)

    e=df2["Var %"].values[n]
    e=e.replace(",",".")
    var=float(abs(float(e[:-1]))/100)
    cot=int(df2["Último"].values[n])
    sector = ""
    if (nombre=="Banco Sabadell" or nombre=="Banco Santander" or nombre=="Caixabank" or nombre=="Bankinter" or nombre=="BBVA"):
        sector = "Bancos" #Bancos
    elif (nombre=="Acerinox" or nombre=="ArcelorMittal" ):
        sector = "Mineria" #Mineria
    elif (nombre=="IAG (Iberia)" or nombre=="Aena" ):
        sector = "Aerolineas" #Aerolineas
    elif (nombre=="Indra" or nombre=="Ferrovial" ):
        sector = "Transporte" #Transporte
    elif (nombre=="Iberdrola" or nombre=="Repsol" or nombre=="Solaria" or nombre=="Endesa" or nombre=="REE" or nombre=="Enagas" or nombre=="Naturgy" or nombre=="Siemens-Gamesa" or nombre=="Acciona" ):
        sector = "Energia" #Energia
    elif (nombre=="CIE Automotive"):
        sector = "Mecanica" #Mecanica
    elif (nombre=="Melia Hotels" or nombre=="Fluidra" or nombre=="Amadeus"):
        sector="Turismo" #Turismo
    elif (nombre == "PharmaMar" or nombre=="Almirall" or nombre=="Laboratorios Rovi" or nombre=="Grifols"):
        sector = "Quimica" #Quimica
    elif (nombre == "Inditex"):
        sector = "Textiles"
    elif(nombre == "Mapfre"):
        sector = "Salud"
    elif(nombre == "Telefonica" or "Cellnex"):
        sector = "Telecomunicaciones"
    elif (nombre == "Inmobiliaria Colonial" or nombre=="MERLIN Properties"):
        sector = "Inmobiliaria"
    
    names.append(nombre)
    pers.append(per)
    pegs.append(peg)
    pvcs.append(pvc)
    divs.append(div)
    sectors.append(sector)
    cots.append(cot)
    vars.append(var)
    with greeter.session() as session:
        # query = ("create (a:Business{name:NAME,per:per,PVC:PVC,PEG:$PVC,DIV:$DIV,SECTOR:$SECTOR})")
        query = "create(a:Business{name:'"+str(nombre)+"',PER:"+str(per)+",PVC:"+str(pvc)+",PEG:"+str(peg)+",DIV:"+str(div)+",SECTOR:'"+sector+"',VAR:"+str(var)+",COTIZACION:"+str(cot)+"})"
        session.run(query)
        
     
    n=n+1
print("Fase 2 completada\n")  
with greeter.session() as session:
    k=0
    # while (k<35):
    # PER:Razon Precio Beneficio - Rentabilidad
    # VAR: Valor en Riesgo - Risk
    # PVC: Libros - Books
    # Cotizacion: Valor de la accion - Size
    # Dividendos: El reparto de beneficios - Rentability
    # PEG: Inversores agresivos   - Fierce
        
    query5 = "match (a:Business),(b: Business) where a.PEG<>-10000 and b.PEG<>-10000 and a.PEG<=10 and b.PEG<=10 and a.name<>b.name or a.PEG>10 and b.PEG>10 and a.PEG<=40 and b.PEG<=40 and a.name<>b.name or a.PEG>40 and b.PEG>40 and a.PEG<=1000 and b.PEG<=1000 and a.name<>b.name or a.PEG>1000 and b.PEG>1000 and a.name<>b.name Create(a)-[:SimilarExpectativaDeBeneficio{name:a.name+'<->'+b.name}]->(b)"
    session.run(query5)
    query2 = "match(a:Business),(b: Business) where a.SECTOR = b.SECTOR and a.name<>b.name Create(a)-[:SameSector{name:a.name+'<->'+b.name}]->(b)"
    session.run(query2)

    query3 = "match (a:Business),(b: Business) where a.PER<>-10000 and b.PER<>-10000 and a.PER<= 700 and b.PER<=700 and a.name<>b.name or a.PER>700 and b.PER>700 and a.PER<=1400 and b.PER<=1400 and a.name<>b.name or a.PER>1400 and b.PER>1400 and a.PER<=2000 and b.PER<=2000 and a.name<>b.name or a.PER>2000 and b.PER>2000 and a.name<>b.name Create(a)-[:SimilarBenefitRatio{name:a.name+'<->'+b.name}]->(b)"
    session.run(query3)                                                                                                                                                                                                                                                                                                                                                                                              #Create(a)-[:SimilarBenefitRatio{name:a.name+'<->'+b.name}]->(b)
    query4 = "match (a:Business),(b: Business) where a.PVC<>-10000 and b.PVC<>-10000 and a.PVC<=100 and b.PVC<=100 and a.name<>b.name or a.PVC>100 and b.PVC>100 and a.PVC<=300 and b.PVC<=300 and a.name<>b.name or a.PVC>300 and b.PVC>300 and a.PVC<=700 and b.PVC<=700 and a.name<>b.name or a.PVC>700 and b.PVC>700 and a.PVC<=800 and b.PVC<=800 and a.name<>b.name or a.PVC>800 and b.PVC>800 and a.name<>b.name Create(a)-[:SimilarPrecioConLibros{name:a.name+'<->'+b.name}]->(b)"
    session.run(query4)
    
    query6 = "match (a:Business),(b: Business) where a.DIV<=0.015 and b.DIV<=0.015 and a.name<>b.name or a.DIV>0.05 and b.DIV>0.05 and a.DIV<=0.04 and b.DIV<=0.04 and a.name<>b.name or a.DIV>0.04 and b.DIV>0.04 and a.DIV<=0.06 and b.DIV<=0.06 and a.name<>b.name or a.DIV>0.06 and b.DIV>0.06 and a.name<>b.name Create(a)-[:SimilarDividendos{name:a.name+'<->'+b.name}]->(b)"
    session.run(query6)
    query7 = "match (a:Business),(b: Business) where (a.VAR<=0.00 and b.VAR<=0.00 and a.name<>b.name or a.VAR>0.00 and b.VAR>0.00 and a.VAR<=0.0015 and b.VAR<=0.0015 and a.name<>b.name or a.VAR>0.0015 and b.VAR>0.0015 and a.VAR<=0.004 and b.VAR<=0.004 and a.name<>b.name or a.VAR>0.004 and b.VAR>0.004 and a.VAR<=0.007 and b.VAR<=0.007 and a.name<>b.name or a.VAR>0.007 and b.VAR>0.007 and a.name<>b.name) Create(a)-[:SimilarVariacion{name:a.name+'<->'+b.name}]->(b)"
    session.run(query7)
    query8 = "match (a:Business),(b: Business) where a.COTIZACION<=700 and b.COTIZACION<=700 and a.name<>b.name or a.COTIZACION>700 and b.COTIZACION>700 and a.COTIZACION<=4000 and b.COTIZACION<=4000 and a.name<>b.name or a.COTIZACION>4000 and b.COTIZACION>4000 and a.COTIZACION<=12000 and b.COTIZACION<=12000 and a.name<>b.name or a.COTIZACION>12000 and b.COTIZACION>12000 and a.COTIZACION<=18000 and b.COTIZACION<=18000 and a.name<>b.name or a.COTIZACION>18000 and b.COTIZACION>18000 and a.name<>b.name Create(a)-[:SimilarCotizacion{name:a.name+'<->'+b.name}]->(b)"
    session.run(query8)
    query9 = "MATCH (a:User), (b:Business) WHERE a.Riesgo>5 AND b.VAR=-10000 OR a.Riesgo>=0 AND a.Riesgo<1 AND b.VAR<=0.0010 OR a.Riesgo>=1 AND a.Riesgo<2 AND b.VAR<0.0015 AND b.VAR>=0.0010 OR a.Riesgo>=2 AND a.Riesgo<3 AND b.VAR<0.004 AND b.VAR>=0.0015 OR  a.Riesgo>=3 AND a.Riesgo<4 AND b.VAR<0.006 AND b.VAR>=0.004 OR  a.Riesgo>=4 AND a.Riesgo<5 AND b.VAR<0.007 AND b.VAR>=0.006 OR a.Riesgo>=5 AND b.VAR>0.007 CREATE(a)-[r:Riesgo_De_Interes{name:a.name+'<->'+b.name}]->(b)"
    session.run(query9)
    query10 = " MATCH (a:User), (b:Business) WHERE b.SECTOR = a.Sector_Interes1 OR b.SECTOR = a.Sector_Interes2 OR b.SECTOR = a.Sector_Interes3 CREATE (a)-[r:Sector_De_Interes{name: a.name+'<->'+b.name}]->(b)"
    session.run(query10)
    query11 = "MATCH (a:User), (b:Business) WHERE a.Rentabilidad<0 AND b.PER=-10000 OR a.Rentabilidad<=0 AND a.Rentabilidad>1 AND b.PER>=0 AND b.PER<300 OR a.Rentabilidad<=1 AND a.Rentabilidad>2 AND b.PER<800 AND b.PER>=300 OR a.Rentabilidad<=2 AND a.Rentabilidad>3 AND b.PER<1400 AND b.PER>=800 OR  a.Rentabilidad<=3 AND a.Rentabilidad>4 AND b.PER<2000 AND b.PER>=1400 OR  a.Rentabilidad<=4 AND a.Rentabilidad>5 AND b.PER>=2000 AND b.PER<5000 OR a.Rentabilidad>=5 AND b.PER>=5000 CREATE (a)-[r:Rentabilidad_De_Interes{name:a.name+'<->'+b.name}]->(b)"
    session.run(query11)
    query12 = " MATCH (a:User), (b:Business) WHERE (a.Tamanio<=0 AND a.Tamanio>1 AND b.COTIZACION<700 OR a.Tamanio=1  AND b.COTIZACION<4000 AND b.COTIZACION>=700 OR a.Tamanio=2 AND b.COTIZACION<12000 AND b.COTIZACION>=4000 OR  a.Tamanio=3 AND b.COTIZACION<18000 AND b.COTIZACION>=12000 OR  a.Tamanio=4 AND b.COTIZACION>=18000 AND b.COTIZACION<20000 OR a.Tamanio=5 AND b.COTIZACION>=20000 ) CREATE (a)-[r:Tamanio_De_Interes{name:a.name+'<->'+b.name}]->(b)"
    session.run(query12)
    query13 = " MATCH (a:User), (b:Business) WHERE (a.Libros=0 AND b.PVC=-10000 OR a.Libros=1  AND b.PVC<100 OR a.Libros=2 AND b.PVC<300 AND b.PVC>=100 OR  a.Libros=3 AND b.PVC<700 AND b.PVC>=300 OR  a.Libros=4 AND b.PVC>=700 AND b.PVC<800 OR a.Libros=5 AND b.PVC>=800 ) CREATE (a)-[r:Relacion_Con_Libros_De_Interes{name:a.name+'<->'+b.name}]->(b)"
    session.run(query13)
    query14 = "MATCH (a:User), (b:Business) WHERE (a.Agresividad=0 AND b.PEG<=10 OR a.Agresividad=1  AND b.PEG<30 AND b.PEG>10 OR a.Agresividad=2 AND b.PEG<80 AND b.PEG>=30 OR  a.Agresividad=3 AND b.PEG<150 AND b.PEG>=100 OR  a.Agresividad=4 AND b.PEG>=100 AND b.PEG<500 OR a.Agresividad=5 AND b.PEG>=500 ) CREATE (a)-[r:Agresividad_Para_Invertir{name:a.name+'<->'+b.name}]->(b)"
    session.run(query14)
#and return (exists( (a)-[:SimilarExpectativaDeBeneficio]->(b) ))=false 
#and (exists( (a)-[:SimilarDividendos]->(b) ))=false 
#and (exists( (a)-[:SimilarVariacion]->(b) ))=false 
#and (exists( (a)-[:SimilarCotizacion]->(b) ))=false 
greeter.close()
print("Fase 3 completada\n")  
grafo = Graph("neo4j://localhost:7687", auth=("neo4j", "Manager123"))
while (True):
    option = input("Elija una opcion:\n1.)Regitrarse\n2.)Ingresar al sistema\n3.)Salir\n")
    if (option=="1"):
        print("\nRegistrarse")
        username = input("\nIngrese su username: ")
        password = input("\nIngrese su contrasenia: ")
        name = input("\nIngrese uno de sus nombres: ")
        surname = input("\nIngrese uno de sus apellidos: ")
        array = ["Bancos", "Mineria", "Quimica", "Aerolineas", "Energia", "Transporte", "Mecanica", "Turismo", "Textiles", "Salud", "Telecomunicaciones", "Inmobiliaria"]
        sector1 = input("\nIngrese un sector que le interese interese (Bancos, Mineria, Quimica, Aerolineas, Energia, Transporte, Mecanica, Turismo, Textiles, Salud, Telecomunicaciones, Inmobiliaria): ")
       
        while sector1 not in array:
            sector1 = input("\nIngrese un sector valido interese (Bancos, Mineria, Quimica, Aerolineas, Energia, Transporte, Mecanica, Turismo, Textiles, Salud, Telecomunicaciones, Inmobiliaria): ")
        
        sector2 = input("\nIngrese un sector que le interese (Bancos, Mineria, Quimica, Aerolineas, Energia, Transporte, Mecanica, Turismo, Textiles, Salud, Telecomunicaciones, Inmobiliaria): ")
        while sector2 not in array:
            sector2 = input("\nIngrese un sector valido interese (Bancos, Mineria, Quimica, Aerolineas, Energia, Transporte, Mecanica, Turismo, Textiles, Salud, Telecomunicaciones, Inmobiliaria): ")
        
        sector3 = input("\nIngrese un sector que le interese (Bancos, Mineria, Quimica, Aerolineas, Energia, Transporte, Mecanica, Turismo, Textiles, Salud, Telecomunicaciones, Inmobiliaria): ")
        while sector3 not in array:
            sector3 = input("\nIngrese un sector valido interese (Bancos, Mineria, Quimica, Aerolineas, Energia, Transporte, Mecanica, Turismo, Textiles, Salud, Telecomunicaciones, Inmobiliaria): ")

        riesgo = 4839201
        while riesgo not in range (0,6):
            riesgo = input("\nIngrese un valor entero que represente el riesgo que esta dispuesto a correr en su inversion [0-5]: ")
            try:
                riesgo = int(riesgo)
                break
            except:
                print("\nNo ingreso un valor valido intentelo de nuevo")
            
        
        rentabilidad = 383
        while rentabilidad not in range (0,6):
            
            rentabilidad = input("\nIngrese un valor entero que represente la rentabilidad que esta dispuesto a correr en su inversion [0-5]: ")
            try:
                rentabilidad = int(rentabilidad)
                
            except:
                print("\nNo ingreso un valor valido intentelo de nuevo")
        
        tamanio = 289
        while tamanio not in range (0,6):
            tamanio = input("\nIngrese un valor entero que represente el tamanio esperado de la empresa en la que quiere invertir [0-5]: ")
            try:
                tamanio = int(tamanio)

            except:
                print("\nNo ingreso un valor valido intentelo de nuevo")
            

        libro = 78329
        while libro not in range (0,6):
            libro = input("\nIngrese un valor entero que represente la relacion esperada entre lo que declara la empresa y la cotizacion en bolsa [0-5]: ")
            try:
                libro = int(libro)

            except:
                print("\nNo ingreso un valor valido intentelo de nuevo")
           

        agresividad = 372819
        while agresividad not in range (0,6):
            agresividad = input("\nIngrese un valor entero que represente que tan agresivo es usted al momento de invertir [0-5]: ")
            try:
                agresividad = int(agresividad)

            except:
                print("\nNo ingreso un valor valido intentelo de nuevo")
            
        create_user(username,
        password, 
        name,
        surname,
        sector1,
        sector2,
        sector3,
        riesgo,
        rentabilidad,
        tamanio,
        libro,
        agresividad,
        graph = grafo
        )     
    elif(option=="2"):
        username = input("\nIngrese su nombre de usuario: ")
        password = input("\nIngrese su password: ")
        is_loged, loged_user = login_user(username, password, grafo)
        print(f'\nIngreso exitoso, Bienvenido, {username}.') 
        while is_loged:
            print("\n1.)Ver Empresas Recomendadas\n2.)Ver Usuarios Recomendados\n3.)Cerrar Sesion")    
            option = input("Ingrese una opcion: ")
            if (option == "1"):
                search_Business(username, grafo)
            elif(option == "2"):
                search_Partner(username, grafo)
            elif(option== "3"):
                print("\nHa cerrado sesion")
                logoutuser(loged_user, grafo)
                is_loged=False

    elif(option=="3"):
        break
    else:
        print("\nNo ingreso una opcion valida")