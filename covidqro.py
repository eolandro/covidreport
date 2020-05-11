
Estado = 22
Municipios = {
	"001":"Amealco   Bonfil",
	"004":"Cadereyta Montes",
	"007":"Ezequiel Montes ",
	"012":"Pedro Escobedo  ", 
	"016":"San Juan del Rio", 
	"017":"Tequisquiapan   " 
}

import argparse
import sys
import csv

parser = argparse.ArgumentParser(description='Extrae datos sobre covid')
parser.add_argument("csv", type=argparse.FileType('r', encoding='iso-8859-1'),  help="CSV Dirección General de Epidemiología ")
args = parser.parse_args()
if not 'csv' in args:
	print(args)
	sys.exit(1)

covidreader = csv.reader(args.csv)


Positivos = filter( lambda e :  e[30] == "1",covidreader)

Entidad = filter( lambda e :  e[7] == "22",Positivos)



NumMun = list(Municipios.keys())

Area = filter( lambda e :  e[8] in NumMun,Entidad)



def formato(e):
	D = []
	D.append(e[1]) #ID
	D.append(Municipios[ e[8] ]) #Municipio
	
		
	D.append( e[10] ) # Ingreso
	D.append( e[11] ) # Sintomas
	D.append( e[12] ) # Defuncion
	D.append( "SI" if e[13] == "1" else "NO" ) # INTUBADO
	D.append( "SI" if e[14] == "1" else "NO" ) # Neumonia
	D.append( int(e[15]) ) # Edad
	return D


FormatArea = map(formato,Area)

Ordena = sorted(FormatArea, key=lambda x: x[1])

Encabezado = ("ID","Municipio","Ingreso","Sintomas","Defunción","Intubado","Neumonia","Edad")

with open("Resumen.csv", 'w') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(Encabezado)
	for e  in Ordena:
		wr.writerow(e)
