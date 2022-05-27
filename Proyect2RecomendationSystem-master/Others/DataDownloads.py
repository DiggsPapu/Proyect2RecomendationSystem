import requests
import pandas as pd
from neo4j import GraphDatabase

class WriteInGraph:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def print_greeting(self, message):
        with self.driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    def CreateBusiness(self, NAME, PER, PVC, PEG, DIV, SECTOR):
        with self.driver.session() as session:
            query = ("create (a:Business{name:$NAME,PER:$PER,PVC:$PVC,PEG:$PVC,DIV:$DIV,SECTOR:$SECTOR})")
            session.run(query, NAME, PER, PVC, PEG, DIV, SECTOR)




url = 'https://www.estrategiasdeinversion.com/cotizaciones/indices/ibex-35/1/desc/variacion-porcentual?gclid=CjwKCAjwgr6TBhAGEiwA3aVuIRuVssaDkelirEroGhMwXA9bgAYYLR8BFaAF_btZX0HWjj5JjKnb9xoC44wQAvD_BwE'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-1]
print(df)
df2 = df_list[-8]
print(df2)
#df.to_csv(r'C:\Users\Administrator\Documents\Proyecto\Proyecto2\Proyect2RecomendationSystem-master\Others\data.csv', index=False)
greeter = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "Manager123"))
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
    var=float(float(e[:-1])/100)
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
with greeter.session() as session:
    k=0
    # while (k<35):
            
    #     k=k+1
    query2 = "match(a:Business),(b: Business) where a.SECTOR = b.SECTOR and a.name<>b.name Create(a)-[:SameSector{name:a.name+'<->'+b.name}]->(b)"
    session.run(query2)

    query3 = "match (a:Business),(b: Business) where a.PER<>-10000 and b.PER<>-10000 and a.PER<= 700 and b.PER<=700 and a.name<>b.name or a.PER>700 and b.PER>700 and a.PER<=1400 and b.PER<=1400 and a.name<>b.name or a.PER>1400 and b.PER>1400 and a.PER<=2000 and b.PER<=2000 and a.name<>b.name or a.PER>2000 and b.PER>2000 and a.name<>b.name Create(a)-[:SimilarBenefitRatio{name:a.name+'<->'+b.name}]->(b)"
    session.run(query3)                                                                                                                                                                                                                                                                                                                                                                                              #Create(a)-[:SimilarBenefitRatio{name:a.name+'<->'+b.name}]->(b)
    query4 = "match (a:Business),(b: Business) where a.PVC<>-10000 and b.PVC<>-10000 and a.PVC<=100 and b.PVC<=100 and a.name<>b.name or a.PVC>100 and b.PVC>100 and a.PVC<=300 and b.PVC<=300 and a.name<>b.name or a.PVC>300 and b.PVC>300 and a.PVC<=700 and b.PVC<=700 and a.name<>b.name or a.PVC>700 and b.PVC>700 and a.PVC<=800 and b.PVC<=800 and a.name<>b.name or a.PVC>800 and b.PVC>800 and a.name<>b.name Create(a)-[:SimilarPrecioConLibros{name:a.name+'<->'+b.name}]->(b)"
    session.run(query4)
    query5 = "match (a:Business),(b: Business) where a.PEG<>-10000 and b.PEG<>-10000 and a.PEG<=10 and b.PEG<=10 and a.name<>b.name or a.PEG>10 and b.PEG>10 and a.PEG<=40 and b.PEG<=40 and a.name<>b.name or a.PEG>40 and b.PEG>40 and a.PEG<=1000 and b.PEG<=1000 and a.name<>b.name or a.PEG>1000 and b.PEG>1000 and a.name<>b.name Create(a)-[:SimilarExpectativaDeBeneficio{name:a.name+'<->'+b.name}]->(b)"
    session.run(query5)
    query6 = "match (a:Business),(b: Business) where a.DIV<=0.015 and b.DIV<=0.015 and a.name<>b.name or a.DIV>0.05 and b.DIV>0.05 and a.DIV<=0.04 and b.DIV<=0.04 and a.name<>b.name or a.DIV>0.04 and b.DIV>0.04 and a.DIV<=0.06 and b.DIV<=0.06 and a.name<>b.name or a.DIV>0.06 and b.DIV>0.06 and a.name<>b.name Create(a)-[:SimilarDividends{name:a.name+'<->'+b.name}]->(b)"
    session.run(query6)
    query7 = "match (a:Business),(b: Business) where a.VAR<=0.00 and b.VAR<=0.00 and a.name<>b.name or a.VAR>0.00 and b.VAR>0.00 and a.VAR<=0.0015 and b.VAR<=0.0015 and a.name<>b.name or a.VAR>0.0015 and b.VAR>0.0015 and a.VAR<=0.004 and b.VAR<=0.004 and a.name<>b.name or a.VAR>0.004 and b.VAR>0.004 and a.VAR<=0.007 and b.VAR<=0.007 and a.name<>b.name or a.VAR>0.007 and b.VAR>0.007 and a.name<>b.name Create(a)-[:SimilarVariacion{name:a.name+'<->'+b.name}]->(b)"
    session.run(query7)
    query8 = "match (a:Business),(b: Business) where a.COTIZACION<=700 and b.COTIZACION<=700 and a.name<>b.name or a.COTIZACION>700 and b.COTIZACION>700 and a.COTIZACION<=4000 and b.COTIZACION<=4000 and a.name<>b.name or a.COTIZACION>4000 and b.COTIZACION>4000 and a.COTIZACION<=12000 and b.COTIZACION<=12000 and a.name<>b.name or a.COTIZACION>12000 and b.COTIZACION>12000 and a.COTIZACION<=18000 and b.COTIZACION<=18000 and a.name<>b.name or a.COTIZACION>18000 and b.COTIZACION>18000 and a.name<>b.name Create(a)-[:SimilarDividendos{name:a.name+'<->'+b.name}]->(b)"
    session.run(query8)


greeter.close()