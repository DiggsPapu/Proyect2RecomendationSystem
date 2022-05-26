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

#df.to_csv(r'C:\Users\Administrator\Documents\Proyecto\Proyecto2\Proyect2RecomendationSystem-master\Others\data.csv', index=False)
n=0
greeter = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "Manager123"))

while (n<35):
    
    nombre=df['Nombre'].values[n]
    per=df['PER'].values[n]
    pvc=df['PVC'].values[n]
    peg=df['PEG'].values[n]
    div=df['Dividendo'].values[n]
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
    elif (nombre=="Melia Hotels" or "Fluidra" or "Amadeus"):
        sector="Turismo" #Turismo
    elif (nombre == "PharmaMar" or "Almirall" or "Laboratorios Rovi" or "Grifols"):
        sector = "Quimica" #Quimica
    elif (nombre == "Inditex"):
        sector = "Textiles"
    elif(nombre == "Mapfre"):
        sector = "Salud"
    elif(nombre == "Telefonica" or "Cellnex"):
        sector = "Telecomunicaciones"
    elif (nombre == "Inmobiliaria Colonial" or "MERLIN Properties"):
        sector = "Inmobiliaria"
    
    print(str(nombre)+str(pvc)+str(peg)+str(div)+str(sector))
    with greeter.session() as session:
        # query = ("create (a:Business{name:NAME,per:per,PVC:PVC,PEG:$PVC,DIV:$DIV,SECTOR:$SECTOR})")
        query = "create(a:Bussiness{name:'"+str(nombre)+"',PER:'"+str(per)+"',PVC:"+str(pvc)+",PEG:'"+str(peg)+"',DIV:'"+str(div)+"',SECTOR:'"+sector+"'})"
        session.run(query)
    n=n+1

greeter.close()