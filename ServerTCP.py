import socket
import threading
import pickle

class ServidorTCPListaDeTarefas:

    def __init__(self):
        self.ipServidor = "127.0.0.1"
        self.portaServidor = 9090
        self.servidorDNS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_thread = threading.Thread(target=self.server_thread)
        self.listaTarefas = [
            {"tarefa": "Jogar o lixo pra fora", "concluida": False}, 
            {"tarefa": "Fazer o L", "concluida": False}, 
            {"tarefa": "Estudar Programação", "concluida": False}
            ]

    def registrarServidorComDNS(self):
        mensagem = f"Registrar servidorTCP {self.ipServidor} {self.portaServidor}"
        self.servidorDNS.sendto(mensagem.encode(), ("127.0.0.1", 8000))
        data, _ = self.servidorDNS.recvfrom(1024)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"Conexão DNS estabelecida {_}")
        print(data.decode())

    def iniciarServidor(self):
        self.socketServidor.bind((self.ipServidor, self.portaServidor))
        self.socketServidor.listen(1)
        print()
        print(f"Servidor TCP ouvindo no endereço: {self.ipServidor}:{self.portaServidor}")
        print("Esperando uma Solicitação...")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        self.server_thread.start()


    def consultarTarefas(self, socketCliente):

        tarefas = pickle.dumps(self.listaTarefas)
        socketCliente.send(tarefas)
        

    def adicionarTarefa(self,operacao, socketClient):
        novaTarefa = operacao[21:] 
        self.listaTarefas.append({"tarefa": novaTarefa, "concluida": False})
        mensagem = "Nova Tarefa Adicionada com Sucesso!"
        socketClient.send(mensagem.encode())

    
    def marcarTarefaComoConcluida(self,operacao, socketCliente):
        posicaoTarefaMarcadaComoConcluida = operacao[20]
        posicaoTarefaMarcadaComoConcluida = int(posicaoTarefaMarcadaComoConcluida)

        if posicaoTarefaMarcadaComoConcluida >= 0 and posicaoTarefaMarcadaComoConcluida < len(self.listaTarefas):

            self.listaTarefas[posicaoTarefaMarcadaComoConcluida]["concluida"] = True

        mensagem = "Tarefa Marcada como Concluida com Sucesso!"
        socketCliente.send(mensagem.encode())
    

    def server_thread(self):
        socketCliente, enderecoCliente = self.socketServidor.accept()
        print(f"Conexão de {enderecoCliente}")

        while True:
            data = socketCliente.recv(1024)
            operacao = data.decode()

            if operacao == "finalizar":
                break

            print('Requisição Recebida')

            if "Consultar" in operacao:
                self.consultarTarefas(socketCliente)

            elif "Adicionar" in operacao:
                self.adicionarTarefa(operacao, socketCliente)

            elif "Marcar" in operacao:
                self.marcarTarefaComoConcluida(operacao, socketCliente)


            print('Resposta Enviada')

        print('Digite "Ctrl+c" para encerrar a conexão')
        socketCliente.close()

if __name__ == "__main__":
    servidorTCP = ServidorTCPListaDeTarefas()
    servidorTCP.registrarServidorComDNS()
    servidorTCP.iniciarServidor()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    servidorTCP.socketServidor.close()
