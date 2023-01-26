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

cur_path_x64 = os.path.join(cur_path, 'Windows' + os.sep +  'x64' + os.sep)
cur_path_x86 = os.path.join(cur_path, 'Windows' + os.sep +  'x86' + os.sep)

if sys.maxsize > 2**32:
    sys.path.append(cur_path_x64)
else:
    sys.path.append(cur_path_x86)
        
import traceback

try:
    import pysftp
except Exception as e:
    traceback.print_exc()
    print("Error: No se pudo importar pysftp")
    raise e

"""
    Obtengo el modulo que fue invocado
"""
global pwd_
global pconn

separator = "/"
global serverOs

module = GetParams("module")

try:
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
        except (pysftp.ConnectionException, pysftp.CredentialException, Exception) as e:
            PrintException()
            traceback.print_exc()
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
                finalPathServer = os.path.join(dir_, filename)
                if serverOs == "Windows":
                    finalPathServer = finalPathServer.replace("/", "\\")
                else:
                    finalPathServer = finalPathServer.replace("\\", "/")
                pconn.put(file_, finalPathServer)
            res = True

        except Exception:
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
                remoteFilePath = remoteFilePath.replace("/", "\\")
            else:
                remoteFilePath = remoteFilePath.replace("\\", "/")
            filename = os.path.basename(remoteFilePath)

            # Define the local path where the file will be saved
            # or absolute "C:\Users\sdkca\Desktop\TUTORIAL.txt"
            localFilePath = path_


            localFilePath = os.path.join(localFilePath, filename)
            if os.path == "/":
                localFilePath = localFilePath.replace("/", "\\")
            else:
                localFilePath = localFilePath.replace("\\", "/")

            pconn.get(remoteFilePath, localFilePath)
            res = True
        except (pysftp.ConnectionException, pysftp.CredentialException, pysftp.SSHException) as e:
            PrintException()
            try:
                os.remove(localFilePath)
            except:
                pass
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

        except Exception as e:
            PrintException()
            res = False

        SetVar(var_, res)

    if module == "list_files":

        try:
            dir_ = GetParams("dir_")
            var_ = GetParams("var_")

            listedFiles = pconn.listdir(dir_)

            SetVar(var_, listedFiles)

        except Exception as e:
            PrintException()
            raise e
        
    if module == "rename_file":

        try:
            file_ = GetParams("file_")
            new_name = GetParams("new_name")
            var_ = GetParams("var_")

            oldPath = os.path.join(pwd_, file_)
            
            if serverOs == "Windows":
                oldPath = oldPath.replace("/", "\\")
            else:
                oldPath = oldPath.replace("\\", "/")
            newPath = os.path.join(pwd_, new_name)
            if serverOs == "Windows":
                newPath = newPath.replace("/", "\\")
            else:
                newPath = newPath.replace("\\", "/")
            pconn.rename(oldPath, newPath)
            res = True

        except Exception as e:
            PrintException()
            res = False

        SetVar(var_, res)
        
    if module == "close_":
        var_ = GetParams("var_")
        
        try:
            if pconn:
                pconn.close()
                pconn = None
                SetVar(var_, True)
            else:
                res = False
                raise Exception("Connection not stablished")
        except Exception as e:
            PrintException()
            SetVar(var_, False)
            raise e
            
        
except Exception as e:
    PrintException()
    raise e

