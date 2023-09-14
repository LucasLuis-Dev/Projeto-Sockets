import socket
import time
import pickle

class ClienteUDP():

    def __init__(self, IpServidorDNS, portaServidorDNS):
        self.IpServidorUDP = ""
        self.portaServidorUDP = 0
        self.IpServidorDNS = IpServidorDNS
        self.portaServidorDNS = portaServidorDNS
        self.clienteDNS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def requisitarEnderecoDoServidorAoDNS(self):
        servico = "servidorUDP"
        self.clienteDNS.sendto(servico.encode(), (self.IpServidorDNS, self.portaServidorDNS))
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("Requisição do endereço IP do servidor feita ao DNS")
        ip, _ = self.clienteDNS.recvfrom(1024)
        host = ip.decode()
        lista = host.split(":")
        self.IpServidorUDP, self.portaServidorUDP = str(lista[1]), int(lista[2])
        print("Endereço IP do Servidor Recebido")

    def conectarAoServidor(self):
        print()
        print('Conectado ao Servidor')
        print(f"Endereço e porta do servidor: {self.IpServidorUDP}:{self.portaServidorUDP}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    def fazerRequisicoesAoServidor(self, requisicoes):
        print("Servidor pronto para receber requisições")
        print()

        for requisicao in requisicoes:
            tempoIncial = time.perf_counter()

            self.socketCliente.sendto(requisicao.encode(), (self.IpServidorUDP, self.portaServidorUDP))
            response, _ = self.socketCliente.recvfrom(4096)

            print("Resposta do Servidor Recebida")
            print()
            print(f"A requisição feita foi {requisicao}")
            print()
            

            tempoFinal = time.perf_counter()

            if "Consulta" in requisicao:
                resposta = pickle.loads(response)

                print('Lista de Tarefas Recebida, segue abaixo a lista')
                print()

                for tarefa in resposta:
                    
                    if tarefa["concluida"]:
                        print(f"- [X] {tarefa['tarefa']}")
                    else:
                        print(f"- [ ] {tarefa['tarefa']}")
                    print(f"Tempo total para o recebimento da resposta: {tempoFinal - tempoIncial:.6f} segundos")
                    print()

                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            
            elif "Adicionar" in requisicao or "Marcar" in requisicao:
                print(response.decode())
                print()
                print(f"Tempo total para o recebimento da resposta: {tempoFinal - tempoIncial:.6f} segundos")
                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")




        message = input('Digite "finalizar" para encerrar a conexão: ').lower()
        self.socketCliente.sendto(message.encode(), (self.IpServidorUDP, self.portaServidorUDP))
        servico = 'Cliente UDP Encerrado'
        self.clienteDNS.sendto(servico.encode(), (self.IpServidorDNS, self.portaServidorDNS))

        self.clienteDNS.close()
        self.socketCliente.close()

if __name__ == "__main__":
    IpServidorDNS = "127.0.0.1"
    portaServidorDNS = 8000
   
    clienteUDP = ClienteUDP(IpServidorDNS, portaServidorDNS)
    clienteUDP.requisitarEnderecoDoServidorAoDNS()
    clienteUDP.conectarAoServidor()

    requisicoes = ["Consultar Tarefas", "Adicionar Atividade: Limpar a Casa", "Consultar Tarefas","Marcar a Atividade: 2 como concluida", "Consultar Tarefas"]
    clienteUDP.fazerRequisicoesAoServidor(requisicoes)
