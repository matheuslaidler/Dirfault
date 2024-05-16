"""
Nota de lembrete: um simples script feito originalmente em 2020 - ficou esquecido no hd
créditos: matheus laidler
-- ele veio enquanto fazia o pyckagetool script - trabalho final na ufrj
"""
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


"""
versão refeita em inglês - teste

import requests
import time

def directory_search():
    '''
    This function performs a brute force search on a specified website to check
    for the existence of certain directories or the robots.txt file, aiming to
    identify which directories may not be visible to search engines.
    '''
    # Prompt the user to input the target website
    site = input("Enter a website URL> ")

    # List of directories and files to be tested
    directories = ["/wp-admin", "/admin", "/login", "/register", "/robots.txt", "/ftp", "/hpp", "/archives"]

    # Iterate over each directory in the list
    for directory in directories:
        # Concatenate the directory with the website URL
        url = site + directory
        # Send a GET request to the URL
        response = requests.get(url)
        # Check the status code of the response
        status = response.status_code
        # Check if the directory exists (status code 200)
        if status == 200:
            print(f"The directory {directory} exists.")
        else:
            print(f"The directory {directory} was not found.")

    # Wait for 1 second before continuing
    time.sleep(1)
    print("                         ")
    return exit_or_continue()

def exit_or_continue():
    '''
    Function to ask the user whether to exit the program or continue.
    '''
    response = input("Do you want to exit? (yes/no): ")
    if response.lower() == "yes":
        print("Program terminated.")
        exit()
    else:
        directory_search()

# Call the main function
directory_search()

"""
