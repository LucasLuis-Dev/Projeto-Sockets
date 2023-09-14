# Projeto Sockets da Disciplina Redes de Computadores - IF975 | CIn UFPE

Alunos responsavéis pelo projeto:
- Lucas Luis de Souza
- Maiara da Silva Lira

Professor da Disciplina:
- Prof.Dr. Kelvin Lopes Dias

## Visão Geral dos Códigos de Cliente e Servidor UDP/TCP e Servidor DNS

Esta documentação explica o funcionamento e a estrutura dos códigos de cliente e servidor UDP/TCP, bem como do servidor DNS, que foram desenvolvidos para um sistema de cálculo distribuído. Os principais componentes incluem:

- Cliente UDP de Calculadora que envia solicitações de operações matemáticas a um servidor UDP de calculadora e exibe as respostas.
- Cliente TCP de Calculador que envia solicitações de operações matemáticas a um servidor TCP de calculadora e exibe as respostas.
- Servidor UDP de Calculadora que recebe solicitações de operações matemáticas, calcula as respostas e envia de volta ao cliente UDP.
- Servidor TCP de Calculadora que recebe solicitações de operações matemáticas, calcula as respostas e envia de volta ao cliente TCP.
- Servidor DNS: Um servidor de nomes que fornece informações de endereço IP e porta para os servidores de calculadora.



### Estrutura Geral
Cliente UDP e TCP: Ambos os clientes compartilham uma estrutura semelhante, com as seguintes partes:

- Configuração de sockets para comunicação com o servidor DNS.
- Envio de uma solicitação ao servidor DNS para obter informações de endereço.
- Configuração de sockets para comunicação direta com o servidor de calculadora.
- Envio de operações matemáticas para o servidor de calculadora.
- Exibição de respostas do servidor de calculadora.
- Possibilidade de encerrar a conexão.

Servidor UDP e TCP: Ambos os servidores têm uma estrutura semelhante:

- Configuração de sockets para aceitar conexões de clientes.
- Espera de solicitações de clientes.
- Processamento de operações matemáticas e envio de respostas.
- Possibilidade de encerrar a conexão.

Servidor DNS: O servidor DNS tem a seguinte estrutura:

- Configuração de um socket para receber solicitações de registro de serviços.
- Manutenção de um registro de serviços disponíveis.
- Resposta a solicitações de clientes para obter informações de endereço.


### O funcionamento dos códigos é coordenado da seguinte forma:

1. Iniciar o Servidor DNS:

- Primeiramente, inicie o servidor DNS executando o arquivo "DNS.py". O servidor DNS é responsável por registrar e fornecer informações sobre os servidores TCP e UDP disponíveis.
2. Iniciar os Servidores TCP e UDP:

- Em seguida, inicie os servidores TCP e UDP executando os arquivos "ServerTCP.py" e "ServerUDP.py". Esses servidores devem ser registrados no servidor DNS para que os clientes possam localizá-los e se comunicar.

3. Iniciar os Clientes TCP e UDP:

- Por último, inicie os clientes TCP e UDP executando os arquivos "ClientTCP.py" e "ClientUDP.py". Esses clientes podem fazer requisições tanto ao servidor DNS quanto aos servidores TCP e UDP de cálculo.


Pronto com isso toda a Aplicação vai estar Funcionando
