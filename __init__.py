# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import os
import sys
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'sftp_' + os.sep + 'libs' + os.sep
# print(cur_path)
sys.path.append(cur_path)

import pysftp
"""
    Obtengo el modulo que fue invocado
"""
global sftp
global server_
global user_
global pass_
global cnopts
global dir_
module = GetParams("module")

if module == "conn_sftp":

    server_ = GetParams("server_")
    user_ = GetParams("user_")
    pass_ = GetParams("pass_")
    port_ = GetParams("port_")
    port_ = int(port_)
    var_ = GetParams("var_")

    if not port_:
        port_ = 22

    print(port_)

    try:

        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection(host=server_, username=user_, password=pass_, port=port_, cnopts=cnopts) as sftp:
            print("Connection succesfully stablished ... ")
            res = True

            # # Switch to a remote directory
            # sftp.cwd('/')
            #
            # localFilePath = r'C:\Users\Marce\Desktop\Capacitaciones\test.xlsx'
            #
            # # Define the remote path where the file will be uploaded
            # remoteFilePath = '/test.xlsx'
            #
            # sftp.put(localFilePath, remoteFilePath)

    except:
        PrintException()
        res = False

    SetVar(var_, res)

if module == "go_dir":

    try:
        dir_ = GetParams("dir_")
        var_ = GetParams("var_")

        with pysftp.Connection(host=server_, username=user_, password=pass_, cnopts=cnopts) as sftp:
            go_ = sftp.cwd(dir_)
            pwd_ = sftp.pwd

        SetVar(var_,pwd_)

    except:
        PrintException()

if module == "upload_":

    file_ = GetParams("file_")
    var_ = GetParams("var_")

    try:

        with pysftp.Connection(host=server_, username=user_, password=pass_, cnopts=cnopts) as sftp:
            filename = os.path.basename(file_)
            print(file_)
            sftp.put(file_, os.path.join(dir_,filename))
            res = True

    except:
        PrintException()
        res = False

    SetVar(var_, res)
#
if module == "download_":

    file_ = GetParams("file_")
    path_ = GetParams("path_")
    var_ = GetParams("var_")

    try:

        with pysftp.Connection(host=server_, username=user_, password=pass_, cnopts=cnopts) as sftp:
            # Define the file that you want to download from the remote directory
            remoteFilePath = os.path.join(dir_,file_)
            print(remoteFilePath)
            filename = os.path.basename(remoteFilePath)

            # Define the local path where the file will be saved
            # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
            localFilePath = path_

            sftp.get(remoteFilePath, os.path.join(localFilePath,filename))

            res = True

    except:
        PrintException()
        res = False

    SetVar(var_, res)

if module == "delete_file":
    file_ = GetParams("file_")
    var_ = GetParams("var_")

    try:
        del_ = ftp.delete(file_)
        res = True

    except:
        PrintException()
        res = False

    SetVar(var_, res)
