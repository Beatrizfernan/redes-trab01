import socket
import threading

# Configurações do servidor
ENDERECO_SERVIDOR = '127.0.0.1'  # Endereço IP do servidor
PORTA_SERVIDOR = 12345           # Porta em que o servidor vai ouvir

# Função para tratar a conexão com um cliente
def lidar_com_cliente(socket_cliente):
    try:
        print(f"Conexão estabelecida com {socket_cliente.getpeername()}")

        while True:
            # Recebe dados do cliente
            dados = socket_cliente.recv(1024)
            if not dados:
                print(f"Conexão encerrada por {socket_cliente.getpeername()}")
                break

            # Processa os dados com base no protocolo
            comando = dados.decode('utf-8').strip()
            resposta = ""

            if comando == "CONSULTA":
                resposta = "DADOS: Informações fictícias."
            elif comando == "HORA":
                # Lógica para obter a hora atual
                from datetime import datetime
                hora_atual = datetime.now().strftime("%H:%M:%S")
                resposta = f"HORA_ATUAL: {hora_atual}"
            elif comando.startswith("ARQUIVO"):
                nome_arquivo = comando.split(" ")[1]
                # Lógica para ler o conteúdo do arquivo (substitua com sua implementação)
                conteudo_arquivo = f"Conteúdo do arquivo {nome_arquivo}."
                if conteudo_arquivo:
                    resposta = f"ARQUIVO {nome_arquivo} {conteudo_arquivo}"
                else:
                    resposta = "ARQUIVO_NAO_ENCONTRADO"
            elif comando == "LISTAR":
                # Lógica para listar os arquivos disponíveis (substitua com sua implementação)
                arquivos_disponiveis = "arquivo1 arquivo2 arquivo3"
                resposta = f"LISTA_ARQUIVOS: {arquivos_disponiveis}"
            elif comando == "SAIR":
                resposta = "ADEUS"
                socket_cliente.close()
                print(f"Conexão encerrada por solicitação de {socket_cliente.getpeername()}")
                break
            else:
                resposta = "COMANDO_DESCONHECIDO"

            # Envia a resposta de volta ao cliente
            socket_cliente.send(resposta.encode('utf-8'))
    except Exception as e:
        print(f"Erro na conexão com {socket_cliente.getpeername()}: {e}")
        socket_cliente.close()

# Configura e inicia o servidor
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ENDERECO_SERVIDOR, PORTA_SERVIDOR))
servidor.listen(5)  # Aceita até 5 conexões pendentes

print(f"Servidor ouvindo em {ENDERECO_SERVIDOR}:{PORTA_SERVIDOR}")

while True:
    try:
        socket_cliente, endereco = servidor.accept()
        thread_cliente = threading.Thread(target=lidar_com_cliente, args=(socket_cliente,))
        thread_cliente.start()
    except Exception as e:
        print(f"Erro ao aceitar a conexão: {e}")
