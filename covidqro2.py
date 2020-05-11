
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
import datetime

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
	if e[12].strip() != '9999-99-99':
		D.append('Defunción')
	else:
		FD = e[11].split('-')
		FC = datetime.date(int(FD[0]),int(FD[1]),int(FD[2]))
		HY = datetime.date.today()
		df = HY - FC
		print(FC,HY,df)
		if df.days > 30:
			D.append('Inactivo') # Sintomas
		else:	      
			D.append('  Activo') # Sintomas
		
	
	D.append( "SI" if e[13] == "1" else "NO" ) # INTUBADO
	D.append( "SI" if e[14] == "1" else "NO" ) # Neumonia
	D.append( int(e[15]) ) # Edad
	return D


FormatArea = map(formato,Area)

Ordena = sorted(FormatArea, key=lambda x: x[1])

Encabezado = ("ID","Municipio","Contagio","Intubado","Neumonia","Edad")

with open("Resumen.csv", 'w') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(Encabezado)
	for e  in Ordena:
		wr.writerow(e)
