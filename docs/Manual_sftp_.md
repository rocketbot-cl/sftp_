# SFTP
  
Connect and manage a SFTP  

*Read this in other languages: [English](Manual_sftp_.md), [Português](Manual_sftp_.pr.md), [Español](Manual_sftp_.es.md)*
  
![banner](imgs/Banner_sftp_.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Connect to SFTP
  
Connect to SFTP
|Parameters|Description|example|
| --- | --- | --- |
|Server|Server address|test.sftp.com|
|Port|Server port|22|
|User|Sftp user|user@test.com|
|Password|Sftp password|******|
|.pem File Path|.pem file path for SFTP connection|.C:/Users/User/file.pem|
|Server's operative system|Server's SFTP operative system||
|Assign result to variable|Variable where the result of the connection will be stored|Variable|

### Go to directory
  
Go to directory indicated by name or absolute path
|Parameters|Description|example|
| --- | --- | --- |
|Directory name|Directory name or absolute path|test|
|Save current directory in variable|Variable name where the current directory will be saved|Variable|

### Upload file
  
Upload file to current directory
|Parameters|Description|example|
| --- | --- | --- |
|File to upload|Select the file to upload|C:/Users/User/Desktop/test.png|
|Directory name|Directory name where the file will be uploaded|/home/ftp/uploads|
|Assign result to variable|Assign the result of the operation to a variable|Variable|

### Upload folder
  
Upload folder to current directory
|Parameters|Description|example|
| --- | --- | --- |
|Folder to upload|Select the folder to upload|C:/Users/User/Desktop/test|
|Directory name|Directory name where the folder will be uploaded|/home/ftp/uploads|
|Assign result to variable|Assign the result of the operation to a variable|Variable|

### Rename file
  
Rename a file that is in the current directory
|Parameters|Description|example|
| --- | --- | --- |
|File to rename|Name of the file that will be renamed. It must be in the current directory|test.txt|
|New name|New file name|test2.txt|
|Assign result to variable|Variable where the result will be stored|Variable|

### Download file
  
Download file from the current directory or from the specified absolute path
|Parameters|Description|example|
| --- | --- | --- |
|File name to download|File name to download|test.png|
|Path to download|Path where the file will be downloaded|C:/Users/User/Desktop|
|Assign result to variable|Assigns the result of the script execution to the indicated variable|Variable|

### Delete file
  
Delete file from the current directory or from the specified absolute path
|Parameters|Description|example|
| --- | --- | --- |
|File name to delete|File name to delete|test.png|
|Assign result to variable|Assigns the result of the script execution to the indicated variable|Variable|

### List files in directory
  
Lists files inside a folder
|Parameters|Description|example|
| --- | --- | --- |
|Directory name|Directory name from which the files will be listed|/home/test|
|Save listed files in variable|Name of the variable where the listed files will be saved|Variable|

### Close connection
  
Close the connection to the server
|Parameters|Description|example|
| --- | --- | --- |
|Save result of disconnection|Variable where the result of the disconnection will be saved|Variable|
