import socket

# Configurações do cliente
SERVIDOR_HOST = '127.0.0.1'  # Endereço IP do servidor
SERVIDOR_PORTA = 12345        # Porta do servidor

# Cria o socket do cliente
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((SERVIDOR_HOST, SERVIDOR_PORTA))
    print(f"Conectado ao servidor em {SERVIDOR_HOST}:{SERVIDOR_PORTA}")

    while True:
        # Solicita um comando ao usuário
        mensagem = input("Digite um comando para o servidor (ou 'SAIR' para sair): ")
        cliente.send(mensagem.encode('utf-8'))

        # Recebe a resposta do servidor
        resposta = cliente.recv(1024).decode('utf-8')
        print(f"Resposta do servidor: {resposta}")

        # Encerra a conexão se o comando for SAIR
        if mensagem == "SAIR":
            cliente.close()
            print("Conexão encerrada.")
            break
except Exception as e:
    print(f"Erro na conexão com o servidor: {e}")

