import socket
import threading

class DNS:

    def __init__(self):
        self.IpServidor = "127.0.0.1"
        self.portaServidor = 8000
        self.servidorDNS = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.servidorDNS.bind((self.IpServidor, self.portaServidor))
        self.servicos = {}
        self.servicosFechados = 0
        self.server_thread = threading.Thread(target=self.iniciar)

    def registrarServico(self, nome, protocolo, porta):
        self.servicos[nome] = (protocolo, porta)
        return f"Aplicacao registrada: {nome} ({protocolo}:{porta})"

    def buscarServico(self, nome):
        if nome in self.servicos:
            host, porta = self.servicos[nome]
            print(f"Endereço IP do {nome} Enviado")
            return f"{nome}:{host}:{porta}"
        return f"Serviço '{nome}' não encontrado."

    def analisarSolicitacaoCliente(self, data, enderecoCliente):
        response = ""
        if data.decode() == "servidorTCP":
            response = self.buscarServico("servidorTCP")
        elif data.decode() == "servidorUDP":
            response = self.buscarServico("servidorUDP")
        elif data.decode() == 'Cliente TCP Encerrado':
            self.servicosFechados += 1
        elif data.decode() == 'Cliente UDP Encerrado':
            self.servicosFechados += 1
        else:
            informacaoServico = data.decode().split()
            acao = informacaoServico[0]
            nome = informacaoServico[1]

            if acao == 'Registrar':
                protocolo, porta = informacaoServico[2], informacaoServico[3]
                response = self.registrarServico(nome, protocolo, porta)
            elif acao == "Consulta":
                response = self.registrarServico(nome)

        print(response)
        self.servidorDNS.sendto(response.encode(), enderecoCliente)

    def iniciar(self):
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print('Servidor DNS Iniciado...')
        print(f'Endereço IP do DNS: {self.IpServidor}, ouvindo na porta {self.portaServidor}')
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        while self.servicosFechados < 2:
            data, enderecoCliente = self.servidorDNS.recvfrom(1024)
            self.analisarSolicitacaoCliente(data, enderecoCliente)
            

        self.servicos.clear()
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print('Os Servidores Registrados Foram Encerrados')
        print(f"Serviços: {self.servicos}")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        self.servidorDNS.close()

    
if __name__ == "__main__":
    dns = DNS()
    dns.server_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
       pass