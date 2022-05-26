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
View(table)
View(table[[19]])

