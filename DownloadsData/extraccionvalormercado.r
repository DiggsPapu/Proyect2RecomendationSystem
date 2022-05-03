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
ticker <- 'BBVA'
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

