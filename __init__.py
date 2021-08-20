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
global pwd_
global pconn

separator = "/"
global serverOs

module = GetParams("module")

if module == "conn_sftp":

    server_ = GetParams("server_")
    user_ = GetParams("user_")
    pass_ = GetParams("pass_")
    port_ = GetParams("port_")
    serverOs = GetParams("serverOs")

    if serverOs == "Windows":
        separator = "\\"
    
    if not port_:
        port_ = 22
    else:
        port_ = int(port_)
    pem = GetParams("pem")
    var_ = GetParams("var_")

    try:
        if pem:
            pconn = pysftp.Connection(
                host=server_,
                username=user_,
                private_key=pem,
            )
            print("Connection succesfully stablished ... ")
        else:
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            pconn = pysftp.Connection(host=server_, username=user_, password=pass_, port=port_, cnopts=cnopts)
            print("Connection succesfully stablished ... ")
        res = True
    except:
        PrintException()
        res = False

    SetVar(var_, res)

if module == "go_dir":

    try:
        dir_ = GetParams("dir_")
        var_ = GetParams("var_")

        go_ = pconn.cwd(dir_)
        pwd_ = pconn.pwd

        SetVar(var_,pwd_)

    except Exception as e:
        PrintException()
        raise e

if module == "upload_":

    

    file_ = GetParams("file_")
    var_ = GetParams("var_")

    dir_ = GetParams("dir_")

    try:
        current = pconn.chdir('.')
        current = pconn.getcwd()
        filename = os.path.basename(file_)
        if not dir_:
#            pconn.put(file_, os.path.join(current, filename))
            finalPathServer = os.path.join(current, filename)
            if serverOs == "Windows":
                finalPathServer = finalPathServer.replace("/", "\\")
            else:
                finalPathServer = finalPathServer.replace("\\", "/")
            pconn.put(file_, finalPathServer)
        else:
            pconn.put(file_, os.path.join(pwd_,filename))
        res = True

    except:
        PrintException()
        res = False

    SetVar(var_, res)

if module == "download_":

    file_ = GetParams("file_")
    path_ = GetParams("path_")
    var_ = GetParams("var_")

    try:
        current = pconn.chdir('.')
        current = pconn.getcwd()
        pwd_ = ""
        if pwd_ == "":
            pwd_ = current
        
        # Define the file that you want to download from the remote directory
        remoteFilePath = os.path.join(pwd_,file_)
        if serverOs == "Windows":
            remoteFilePath = remoteFilePath.replace("/". "\\"))
        else:
            remoteFilePath = remoteFilePath.replace("\\", "/")
        filename = os.path.basename(remoteFilePath)

        # Define the local path where the file will be saved
        # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
        localFilePath = path_
        pconn.get(remoteFilePath, os.path.join(localFilePath,filename))
        res = True
    except:
        PrintException()
        res = False

    SetVar(var_, res)

if module == "delete_file":
    file_ = GetParams("file_")
    var_ = GetParams("var_")

    try:
        delFilePath = os.path.join(pwd_, file_)
        if serverOs == "Windows":
            delFilePath = delFilePath.replace("/", "\\")
        else:
            delFilePath = delFilePath.replace("\\", "/")
        del_ = pconn.remove(delFilePath)
        res = True

    except:
        PrintException()
        res = False

    SetVar(var_, res)