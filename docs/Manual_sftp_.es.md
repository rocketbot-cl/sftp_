# SFTP
  
Conecta y gestiona un SFTP  

*Read this in other languages: [English](Manual_sftp_.md), [Português](Manual_sftp_.pr.md), [Español](Manual_sftp_.es.md)*

![banner](imgs/Banner_sftp_.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Descripción de los comandos

### Conectar con SFTP
  
Conectar con SFTP
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Servidor|Dirección del servidor|test.sftp.com|
|Puerto|Puerto del servidor|22|
|Usuario|Usuario de sftp|user@test.com|
|Contraseña|Contraseña de sftp|******|
|Ruta al Archivo .pem|Ruta al archivo .pem para conexión con SFTP|C:/Users/Usuario/archivo.pem|
|Sistema operativo del servidor|Sistema operativo del servidor SFTP||
|Asignar resultado a variable|Variable donde se almacenará el resultado de la conexión|Variable|

### Ir a directorio
  
Se mueve al directorio indicado por el nombre o ruta absoluta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de directorio|Nombre de directorio o ruta absoluta|test|
|Guardar directorio actual en variable|Nombre de variable donde se guardará el directorio actual|Variable|

### Subir archivo
  
Sube el archivo al directorio actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo a subir|Seleccione el archivo a subir|C:/Users/Usuario/Desktop/test.png|
|Nombre de directorio|Nombre del directorio donde se subirá el archivo|/home/ftp/uploads|
|Asignar resultado en variable|Asigna el resultado de la operación a una variable|Variable|

### Subir carpeta
  
Sube la carpeta al directorio actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Carpeta a subir|Seleccione la carpeta a subir|C:/Users/Usuario/Desktop/test|
|Nombre de directorio|Nombre del directorio donde se subirá la carpeta|/home/ftp/uploads|
|Asignar resultado en variable|Asigna el resultado de la operación a una variable|Variable|

### Renombrar archivo
  
Renombra un archivo que se encuentra en el directorio actual
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Archivo a renombrar|Nombre del archivo que será renombrado. Debe estar en el directorio actual|test.txt|
|Nuevo nombre|Nuevo nombre del archivo|test2.txt|
|Asignar resultado en variable|Variable donde se almacenará el resultado|Variable|

### Descargar archivo
  
Descarga archivo del directorio actual o desde la ruta absoluta indicada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de archivo a descargar|Nombre del archivo a descargar|test.png|
|Ruta donde descargar|Ruta donde se descargará el archivo|C:/Users/Usuario/Desktop|
|Asignar resultado en variable|Asigna el resultado de la ejecución del script a la variable indicada|Variable|

### Eliminar archivo
  
Elimina un archivo del directorio actual o desde la ruta absoluta indicada
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre de archivo a eliminar|Nombre del archivo a eliminar|test.png|
|Asignar resultado en variable|Asigna el resultado de la ejecución del script a la variable indicada|Variable|

### Listar archivos en directorio
  
Lista los archivos contenidos en una carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Nombre del directorio|Nombre del directorio del cual se listarán los archivos|/home/test|
|Guardar archivos listados en variable|Nombre de la variable donde se guardarán los archivos listados|Variable|

### Cerrar conexión
  
Cierra la conexión con el servidor
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Guardar resultado de desconexión|Variable donde se guardará el resultado de la desconexión|Variable|
