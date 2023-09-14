import socket
import threading
import pickle

class ServidorUDPListaDeTarefas():

    def __init__(self):
        self.serverIp = "127.0.0.1"
        self.serverPort = 8080
        self.servidorDNS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_thread = threading.Thread(target=self.server_thread)
        self.listaTarefas = [
            {"tarefa": "Jogar o lixo pra fora", "concluida": False}, 
            {"tarefa": "Fazer o L", "concluida": False}, 
            {"tarefa": "Estudar Programação", "concluida": False}
            ]

    def registrarComDNS(self):
        mensagem = f"Registrar servidorUDP {self.serverIp} {self.serverPort}"
        self.servidorDNS.sendto(mensagem.encode(), ("127.0.0.1", 8000))
        data, _ = self.servidorDNS.recvfrom(1024)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(f"Conexão DNS estabelecida {_}")
        print(data.decode())

    def iniciarServidor(self):
        self.socketServidor.bind((self.serverIp, self.serverPort))
        print()
        print(f"Servidor UDP ouvindo no endereço: {self.serverIp}:{self.serverPort}")
        print("Esperando uma Solicitação...")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        self.server_thread.start()

   
    def consultarTarefas(self, enderecoCliente):
        tarefas = pickle.dumps(self.listaTarefas)
        self.socketServidor.sendto(tarefas, enderecoCliente)
        

    def adicionarTarefa(self,operacao, enderecoCliente):
        novaTarefa = operacao[21:] 
        self.listaTarefas.append({"tarefa": novaTarefa, "concluida": False})
        mensagem = "Nova Tarefa Adicionada com Sucesso!"
        self.socketServidor.sendto(mensagem.encode(), enderecoCliente)

    
    def marcarTarefaComoConcluida(self,operacao, enderecoCliente):
        posicaoTarefaMarcadaComoConcluida = operacao[20]
        posicaoTarefaMarcadaComoConcluida = int(posicaoTarefaMarcadaComoConcluida)

        if posicaoTarefaMarcadaComoConcluida >= 0 and posicaoTarefaMarcadaComoConcluida < len(self.listaTarefas):

            self.listaTarefas[posicaoTarefaMarcadaComoConcluida]["concluida"] = True

        mensagem = "Tarefa Marcada como Concluida com Sucesso!"
        self.socketServidor.sendto(mensagem.encode(), enderecoCliente)
    


    def server_thread(self):
        while True:
            data, enderecoCliente = self.socketServidor.recvfrom(2024)
            print(f"Conexão de {enderecoCliente}")
            operacao = data.decode()
            if operacao == "finalizar":
                break

            print("Requisição Recebida")

            if "Consultar" in operacao:
               
                self.consultarTarefas(enderecoCliente)

            elif "Adicionar" in operacao:
               
                self.adicionarTarefa(operacao, enderecoCliente)

            elif "Marcar" in operacao:
                
                self.marcarTarefaComoConcluida(operacao, enderecoCliente)

        print('Resposta Enviada')
        print('Digite "Ctrl+c" para encerrar a conexão')
        self.socketServidor.close()

if __name__ == "__main__":
    servidorUDP = ServidorUDPListaDeTarefas()
    servidorUDP.registrarComDNS()
    servidorUDP.iniciarServidor()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
