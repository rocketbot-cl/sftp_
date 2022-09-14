# SFTP
  
Conectar e administrar um SFTP 

*Read this in other languages: [English](Manual_sftp.md), [Portugues](Manual_sftp.pr.md), [Español](Manual_sftp.es.md).*
  
![banner](imgs/Banner_sftp_.png)
## Como instalar este módulo
  
__Baixe__ e __instale__ o conteúdo na pasta 'modules' no caminho do Rocketbot  



## Descrição do comando

### Conectar com SFTP
  
Conectar com SFTP
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Servidor|Endereço do servidor|test.sftp.com|
|Porta|Porta do servidor|22|
|Usuário|Usuário de sftp|user@test.com|
|Senha|Senha de sftp|******|
|Caminho do arquivo .pem|Caminho do arquivo .pem para conexão com SFTP|C:/Users/Usuário/arquivo.pem|
|Sistema operacional do servidor|Sistema operacional do servidor SFTP||
|Atribuir resultado a variável|Variável onde o resultado da conexão será armazenado|Variável|

### Ir para o diretório
  
Mova-se para o diretório indicado pelo nome ou caminho absoluto
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do diretório|Nome do diretório ou caminho absoluto|test|
|Salvar diretório atual na variável|Nome da variável onde o diretório atual será salvo|Variável|

### Carregar arquivo
  
Carrega o arquivo para o diretório atual
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Arquivo para carregar|Selecione o arquivo para carregar|C:/Users/Usuário/Desktop/test.png|
|Nome do diretório|Nome do diretório onde o arquivo será carregado|/home/ftp/uploads|
|Atribuir resultado a variável|Atribui o resultado da operação a uma variável|Variável|

### Renomear arquivo
  
Renomeie um arquivo do caminho absoluto indicado. Se outro caminho absoluto for colocado, o comando moverá o arquivo.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Arquivo para renomear|Caminho absoluto do arquivo para renomear|/home/test/test.txt|
|Novo nome e localização|Caminho absoluto do arquivo|/home/pasta/test2.txt|
|Atribuir resultado à variável|Variável onde o resultado será armazenado|Variável|

### Baixar arquivo
  
Baixe o arquivo do diretório atual ou do caminho absoluto especificado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do arquivo para baixar|Nome do arquivo para baixar|test.png|
|Caminho para baixar|Caminho onde o arquivo será baixado|C:/Users/Usuário/Desktop|
|Atribuir resultado à variável|Atribui o resultado da execução do script à variável indicada|Variável|

### Eliminar archivo
  
Elimina um arquivo do diretório atual ou do caminho absoluto dado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do arquivo a ser excluído|Nome do arquivo a ser excluído|test.png|
|Atribuir resultado à variável|Atribui o resultado da execução do script à variável indicada|Variável|

### Listar arquivos em diretório
  
Lista os arquivos contidos em uma pasta
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome do diretório|Nome do diretório do qual os arquivos serão listados|/home/test|
|Salvar arquivos listados na variável|Nome da variável onde os arquivos listados serão salvos|Variável|