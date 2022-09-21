# SFTP
  
Conecta y gestiona un SFTP  

*Read this in other languages: [English](Manual_sftp.md), [Portugues](Manual_sftp.pr.md), [Español](Manual_sftp.es.md).*
  
![banner](imgs/Banner_sftp_.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Connect to SFTP
  
Connect to SFTP
|Parameters|Description|example|
| --- | --- | --- |
|Server|Server address|test.sftp.com|
|Port|Server port|22|
|User|Sftp user|user@test.com|
|Password|Sftp password|******|
|.pem File Parh|.pem file path for SFTP connection|.C:/Users/User/file.pem|
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

### Rename file
  
Rename a file from the absolute path indicated. If another absolute path is placed, the command will move the file.
|Parameters|Description|example|
| --- | --- | --- |
|File to rename|Absolute path of the file to rename|/home/test/test.txt|
|New name and location|Absolute path of the file|/home/folder/test2.txt|
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
