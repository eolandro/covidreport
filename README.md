# ¿Qué hace?

Extrae datos por zonas de covid19 en mexico.
# ¿Qué necesitas ?

* Python 3
* [Base de datos](https://www.gob.mx/salud/documentos/datos-abiertos-152127)
* [Catálogos opcional](https://www.gob.mx/salud/documentos/datos-abiertos-152127)

# ¿Cómo se ejecuta?

``python3 covidqro.py <basedatos.csv>``
``python3 covidqro2.py <basedatos.csv>``

# ¿Qué obtengo?
una archivo llamado resumen.csv

# ¿Cómo lo personalizo?

Modifica  la variable de Estado por el estado que corresponda (mira el catálogo) de gobierno,
del mismo modo los municipios.

``Estado = 22``

``Municipios = {``

``    "001":"Amealco   Bonfil",``
``    "004":"Cadereyta Montes",``
``    "007":"Ezequiel Montes ",``
``    "012":"Pedro Escobedo  ",``
``    "016":"San Juan del Rio",``
``    "017":"Tequisquiapan   "``
    
``}``
