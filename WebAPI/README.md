# Info

## primero se debe crear el ambiente virtual (gestor de modulos)
```sh
python -m venv venv
```
## para activar virtualenv
```sh
venv\Scripts\Activate.ps1
```
## y para desactivar
```sh
deactivate
```

## para instalar modulos
```sh
pip install -r requirements.txt
```
## para generar requirement.txt solo con los packages instalados por pip
```sh
pip install pipreqs
```
## y luego ejecutar
```sh
pipreqs --force
```

## para generar requirements.txt con todos los packages
```sh
python -m pip freeze > requirements.txt
```

## para ejecutar flask server
```sh
flask --app main run
```

## para ejecutar archivo especifico
```sh
python main.py
```

## _*el servidor donde este alojado el servicio requiere de odbc para usar como provedor_
https://learn.microsoft.com/es-es/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16#download-for-windows


## metodos de la api
```
http://127.0.0.1:5000/cvMaker/cvDesdeArchivo?template=simpleB
```

