import requests
import time

def bruteforceDir():
    '''
    Função que realiza um brute force em um site indicado para verificar
    a existência de determinados diretórios ou do arquivo robots.txt, 
    a fim de identificar quais diretórios não podem ser vistos por 
    mecanismos de busca.
    '''
    # Solicita ao usuário que insira o site alvo
    site = input("Digite um site> ")

    # Lista de diretórios e arquivos a serem testados
    lista = ["/wp-admin", "/admin", "/login", "/register", "/robots.txt", "/ftp", "/hpp", "/archives"]

    # Itera sobre cada diretório na lista
    for diretorio in lista:
        # Concatena o diretório ao site
        url = site + diretorio
        # Realiza a requisição GET ao site
        response = requests.get(url)
        # Verifica o código de status da resposta
        status = response.status_code
        # Verifica se o diretório existe (código de status 200)
        if status == 200:
            print(f"O diretório {diretorio} existe.")
        else:
            print(f"O diretório {diretorio} não foi encontrado.")

    # Aguarda 1 segundo antes de continuar
    time.sleep(1)
    print("                         ")
    return leave()

def leave():
    '''
    Função para solicitar ao usuário se deseja sair do programa ou continuar.
    '''
    resposta = input("Deseja sair? (sim/não): ")
    if resposta.lower() == "sim":
        print("Programa encerrado.")
        exit()
    else:
        bruteforceDir()

# Chamada da função principal
bruteforceDir()
