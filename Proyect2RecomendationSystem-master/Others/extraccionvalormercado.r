# entrada:
# - tabla (accion, inicio, fin)
# salida
# - tabla (accion, indice)

# ************************************************************************************
# Instalacion y carga de paquetes
# ************************************************************************************
if(!require('tseries')) install.packages('tseries')
library(tseries)

if(!require('zoo')) install.packages('zoo')
library(zoo)

if(!require('tsbox')) install.packages('tsbox')
library(tsbox)

# Lectura de Datos
ticker <- '^IXIC'
fecha_inicio <- '2022-04-05'
fecha_fin <- '2022-04-19'

indice <- get.hist.quote(instrument = as.character(ticker), 
                         start=as.Date(as.character(fecha_inicio)), 
                         end=as.Date(as.character(fecha_fin)), 
                         quote = "AdjClose")

?ts_ts
ts_indice <- ts_ts(indice)
indice <- ts_zoo(ts_indice)
indice <- na.approx(indice)

indice



library(xml2)
library(rvest)
library(XML)
url <- "https://www.estrategiasdeinversion.com/cotizaciones/indices/ibex-35#pane-8_tbl_quotation--index" 
page <- read_html(url) #Creates an html document from URL
table <- html_table(page, fill = TRUE) #Parses tables into data frames
table[1]
table[2]
table[3]
table[4]
table[5]
table[6]
table[7]
table[8]
table[9]
table[10]
table[11]
table[12]
table[13]
table[14]
table[15]
table[16]
table[17]
table[18]
table[19]#Prints the table in the 19th tab

table1<-table[19]#Assigns the table1 to the 19th tab
write.csv(table1,"C:\\Users\\salon\\OneDrive\\Documentos\\Diego\\Proyectos\\Proyecto2\\Others\\data.csv", row.names = FALSE)

