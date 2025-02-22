def get_nome():
    nome_usuario = input("Entre com o seu nome: ")
    return nome_usuario

def print_mensagem(nome_usuario):
    print("Olá jovem padawan ", nome_usuario)

def main():
    nome_usuario = get_nome()
    print_mensagem(nome_usuario)

main()