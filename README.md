# Projeto Sockets da Disciplina Redes de Computadores - IF975 | CIn UFPE

Alunos responsavéis pelo projeto:
- Lucas Luis de Souza
- Maiara da Silva Lira

Professor da Disciplina:
- Prof. Dr. Kelvin Lopes Dias

## Visão Geral dos Códigos de Cliente e Servidor UDP/TCP e Servidor DNS

Esta documentação explica o funcionamento e a estrutura dos códigos de cliente e servidor UDP/TCP, bem como do servidor DNS, que foram desenvolvidos para um sistema de lista de tarefas. Os principais componentes incluem:

- Cliente UDP de Lista de Tarefas que envia solicitações e mudanças referentes a uma lista de tarefas que está em um servidor UDP que exibe as respostas.
- Cliente TCP de Lista de Tarefas que envia solicitações e mudanças referentes a uma lista de tarefas que está em um servidor TCP que exibe as respostas.
- Servidor UDP de Lista de Tarefas recebe solicitações de mudança e consulta da lista e envia de volta uma resposta ao cliente UDP.
- Servidor TCP de Lista de Tarefas recebe solicitações de mudança e consulta da lista e envia de volta uma resposta ao cliente TCP.
- Servidor DNS: Um servidor que fornece informações de endereço IP e porta para os servidores de Lista de Tarefas.



### Estrutura Geral

Cliente UDP e TCP — Ambos os clientes possuem alguns pontos da estrutura com certa semelhança::

- Configuração de sockets para comunicação com o servidor DNS.
- Envio de uma solicitação ao servidor DNS para obter informações de endereço.
- Configuração de sockets para comunicação direta com o servidor de Lista de Tarefas.
- Envio de consultas e mudanças na lista para o servidor de Lista de Tarefas.
- Exibição de respostas do servidor.
- Possibilidade de encerrar a conexão.

Servidor UDP e TCP — Ambos os servidores têm alguns pontos da estrutura com certa semelhança:

- Configuração de sockets para aceitar conexões de clientes.
- Espera de solicitações de clientes.
- Processamento das requisições feitas pelos clientes e envio de respostas.
- Possibilidade de encerrar a conexão.

Servidor DNS — O servidor DNS tem a seguinte estrutura:

- Configuração de um socket para receber solicitações de registro de serviços.
- Manutenção de um registro de serviços disponíveis.
- Resposta a solicitações de clientes para obter informações de endereço.


### O funcionamento dos códigos é coordenado da seguinte forma:

1. Iniciar o Servidor DNS:

- Primeiramente, inicie o servidor DNS executando o arquivo "DNS.py". O servidor DNS é responsável por registrar e fornecer informações sobre os servidores TCP e UDP disponíveis.

2. Iniciar os Servidores TCP e UDP:

- Em seguida, inicie os servidores TCP e UDP executando os arquivos "ServerTCP.py" e "ServerUDP.py". Esses servidores devem ser registrados no servidor DNS para que os clientes possam localizá-los e se comunicar.

3. Iniciar os Clientes TCP e UDP:

- Por último, inicie os clientes TCP e UDP executando os arquivos "ClientTCP.py" e "ClientUDP.py". Esses clientes podem fazer requisições tanto ao servidor DNS quanto aos servidores TCP e UDP.


Pronto com isso toda a Aplicação vai estar Funcionando

## Capturas do Terminal

- Captura do Servidor DNS

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979578512908348/Captura_de_tela_de_2023-09-14_14-42-29.png">
<br>
<br>

- Captura do Servidor TCP

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979578164773015/Captura_de_tela_de_2023-09-14_14-42-47.png">
<br>
<br>

- Captura do Servidor UDP

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979357594722356/Captura_de_tela_de_2023-09-14_14-43-01.png">
<br>
<br>

- Captura do Cliente TCP

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979357187883098/Captura_de_tela_de_2023-09-14_14-43-16.png"> 
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979356755861524/Captura_de_tela_de_2023-09-14_14-43-23.png">
<br>
<br>

- Captura do Cliente UDP

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979356466462720/Captura_de_tela_de_2023-09-14_14-43-32.png">
<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979356105736294/Captura_de_tela_de_2023-09-14_14-43-39.png">


## Capturas do WireShark

### TCP

Essa captura mostra a requisição feita ao DNS na porta 8000 pelo cliente TCP, onde o mesmo busca receber endereço IP do servidor TCP e logo em seguida o cliente TCP estabele uma conexão cliente-servidor caracterizada pelo Three-way Handshake que inicia na linha 487 e confirma a conexão entre eles na 489, apoś isso acontece as requisições feitas pelo cliente TCP ao Servidor. Logo após o encerramento do cliente o servidor TCP também é encerrado, enviando uma mensagem para o DNS requisitanto a remoção do serviço.

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979579100115024/Captura_de_tela_de_2023-09-14_14-42-10.png">
<br>
<br>

Já nesta captura abaixo, é mostrado a finalização da conexão cliente-servidor caracterizada pelo "FIN ACK".

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979580702339092/Captura_de_tela_de_2023-09-14_14-39-40.png">


### UDP

Essa captura mostra inicialmente a requisição do cliente UDP com a porta 43874 feita ao DNS na porta 8000 para o recebimento do endereço IP do Servidor UDP mostrada na linha 575 e 576, após receber o endereço IP o cliente UDP usando inicia o seu processo de requisições feitas ao Servidor UDP iniciando na linha 577 e indo até a 659. Logo após o encerramento do cliente o servidor UDP também é encerrado, enviando uma mensagem para o DNS requisitanto a remoção do serviço.

<img src="https://cdn.discordapp.com/attachments/965066624556232737/1151979581281149038/Captura_de_tela_de_2023-09-14_14-29-09.png">