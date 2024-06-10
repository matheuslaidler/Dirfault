import requests # type: ignore
import time

def directory_search():
    '''
    This function performs a brute force search on a specified website to check
    for the existence of certain directories or the robots.txt file, aiming to
    identify which directories may not be visible to search engines.

    Função que realiza um brute force em um site indicado para verificar
    a existência de determinados diretórios ou do arquivo robots.txt, 
    a fim de identificar quais diretórios não podem ser vistos por 
    mecanismos de busca.
    '''
    # Prompt the user to input the target website || Solicita ao usuário que insira o site alvo
    print("DIRFAULT by matheuslaidler \n Type the full website link you want with the last slash '/' and use 'www' if/when necessary \n  ( e.g. https://matheuslaidler.github.io/ || https://www.google.com/ )\n")
    site = input(" Enter a valid URL> ")

    # List of directories and files to be tested || Lista de diretórios e arquivos a serem testados
    directories = ["wp-admin", "admin", "login", "register", "robots.txt", "ftp", "hpp", "archives", ".aws/", ".git/", ".htaccess/"]

    # Iterate over each directory in the list || Itera sobre cada diretório na lista
    for directory in directories:
        # Concatenate the directory with the website URL || Concatena o diretório ao site
        url = site + directory
        # Send a GET request to the URL || Realiza a requisição GET ao site
        response = requests.get(url)
        # Check the status code of the response || Verifica o código de status da resposta
        status = response.status_code
        # Check if exists (status code 200) || Verifica se o diretório existe (código de status 200)
        if status < 200:
            print(f" * {url} received the request => [status code {status} informational response]")
            #the request was received, continuing process - 1xx - example; The server responds with a 102 Processing status code, which indicates that it has received the request and is currently processing it, but has not yet completed the request. The server includes an empty response body with no content, and a few headers like Date and Server .
        elif 199 < status < 300:
            print(f" * {url} exists => [status code {status} successful] => {directory} found!!")
            #the request was successfully received, understood, and accepted - 2xx
        elif 299 < status < 400:
            print(f" * {url} is redirecting => [status code {status} redirection]")
            #further action needs to be taken in order to complete the request - 3xx
        elif 399 < status < 500:
            print(f" * {url} was not found => [status code {status} client error]")
            #the request contains bad syntax or cannot be fulfilled - 4xx
        else:
            print(f" * {url} was inaccessible => [status code {status} server error]")
            #the server failed to fulfil an apparently valid request - 5xx

    # Delay / Wait for X second(s) before continuing || Aguarda X segundo(s) antes de continuar
    time.sleep(1)
    print("                         ")
    return leave()

def leave():
    '''
    Function to ask user whether to exit the program or continue.

    Função para solicitar ao usuário se deseja sair do programa ou continuar.
    '''
    response = input(" Do you want to exit? (yes/no): ")
    if response.lower() == "yes":
        print("Program terminated.")
        exit()
    else:
        directory_search()

# Call the main function
# Chamada da função principal
directory_search()

"""
Nota de lembrete: um simples script feito originalmente em 2020 - ficou esquecido no hd
créditos: matheus laidler
-- ele veio do pyckagetool
fzr a chamada da função principal correta dps
colocar opção para uso de wordlist no script -> colocando as wordlists do dirbuster, por exemplo, no lugar da array
colocar o "#type: ignore" qnd precisar - 'erro' vstudio
"""
