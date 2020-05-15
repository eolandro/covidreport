
Estado = 22
Municipios = {
	"001":"Amealco Bonfil",
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
	#D.append(e[1]) #ID
	D.append(Municipios[ e[8] ]) #Municipio
	if e[12].strip() != '9999-99-99':
		D.append('Fallecidos')
	else:
		FD = e[11].split('-')
		FC = datetime.date(int(FD[0]),int(FD[1]),int(FD[2]))
		HY = datetime.date.today()
		df = HY - FC
		#print(FC,HY,df)
		if df.days > 30:
			D.append('Inactivos') # Sintomas
		else:	      
			D.append('Activos') # Sintomas
		
	
	D.append( 1 if e[13] == "1" else 0 ) # INTUBADO
	D.append( 1 if e[14] == "1" else 0 ) # Neumonia
	#D.append( int(e[15]) ) # Edad
	return D


FormatArea = map(formato,Area)

#No need it on massive 
#Ordena = sorted(FormatArea, key=lambda x: x[1])

Resultado = {}
for e in FormatArea:
	if e[0] not in Resultado:
		Resultado[ e[0] ] = {"Fallecidos":0,"Activos":0,"Inactivos":0, "Intubados":0, "Neumonias":0 }
	Resultado[ e[0] ] [ e[1] ] += 1
	Resultado[ e[0] ] [ 'Intubados' ] += e[2]
	Resultado[ e[0] ] [ 'Neumonias' ] += e[3]
	
print(Resultado)


Encabezado = ("Municipio","Fallecidos","Activos","Inactivos","Intubados","Neumonias")
#print(args.csv.name)

with open("Resumen-"+args.csv.name, 'w') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(Encabezado)
	Ordena = Resultado.keys()
	for e  in Ordena:
		L = [e]
		L.append( Resultado [e]['Fallecidos'])
		L.append( Resultado [e]['Activos'])
		L.append( Resultado [e]['Inactivos'])
		L.append( Resultado [e]['Intubados'])
		L.append( Resultado [e]['Neumonias'])
		wr.writerow(L)

