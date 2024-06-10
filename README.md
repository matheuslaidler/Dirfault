# Dirfault-Search
A python script to Search Default Directories and robots.txt

### README (Português)

#### Search Default Directories - Meu script em python

Este script foi originalmente desenvolvido em 2020 durante o trabalho final de Computação I na UFRJ. No entanto, acabou sendo deixado de lado e esquecido no HD, pois acabou não saindo na versão final do script. A ideia era deixar uma ferramenta externa e específica para isso. 

O script visa realizar uma busca de diretórios em um site especificado pelo usuário. Ele utiliza uma técnica de brute force para verificar a existência de diretórios comuns, como "wp-admin", "admin", "robots.txt", entre outros. 
(Aviso> o arquivo robots tem o objetivo de identificar quais diretórios podem não ser visíveis para mecanismos de busca).

Ao resgatar o código jogado em meu HD e ter postado no github, atualmente dei uma melhorada nele para ampliar mais os resultados em relação aos status code dos requests. Penso em colocar uma opção futuramente para podermos utilizar uma wordlist externa para o bruteforce, assim a ferramenta seria mais maleável e poderia ser usada com as mesmas listas do dirbuster, por exemplo.

Para utilizar o script, basta executá-lo como qualquer script python3 e inserir a URL do site que deseja verificar. 
O script então realizará a busca nos diretórios e informará se cada diretório existe ou não no site dependendo do status code.

#### Modo de uso

```bash
python3 dirfault.py
```
```bash
DIRFAULT by matheuslaidler 
 Type the full website link you want without the last slash '/' and use 'www' sub just when necessary
  ( e.g. https://matheuslaidler.github.io/ || https://www.google.com/ )

 Enter a valid URL> https://**********.net
 * https://**********.net/wp-admin was not found => [status code 404 - client error]
 * https://**********.net/admin exists => [status code 200 - successful!!]
 * https://**********.net/login exists => [status code 200 - successful!!]
 * https://**********.net/register exists => [status code 200 - successful!!]
 * https://**********.net/robots.txt exists => [status code 200 - successful!!]
 * https://**********.net/ftp was not found => [status code 404 - client error]
 * https://**********.net/hpp was not found => [status code 404 - client error]
 * https://**********.net/archives was not found => [status code 404 - client error]
 * https://**********.net/.aws/ was not found => [status code 404 - client error]
 * https://**********.net/.git/ was not found => [status code 404 - client error]
 * https://**********.net/.htaccess/ was not found => [status code 404 - client error]
                         
 Do you want to exit? (yes/no):
```
 - AVISO> NUNCA coloque o `/` no final do link para ser uma URL válida, sem falar que precisa colocar o protocolo `http://` ou `https://` antes do site, podendo colocar com o subdomínio antes também, se precisar no caso - como colocando o `www.` apenas quando necessário, ou seja, se o serviço padrão usa o subdomínio, coloque com ele no script para evitar erro ma execução.

### README (English)

#### Search Default Directories - My python script

This script was originally developed in 2020 during the final project of "Computação I" at UFRJ. However, it ended up being set aside and forgotten on my HD.

This script aims to perform a search for default directories on a specified website (input by user). It uses a brute force technique to check for the existence of common directories such as "wp-admin", "admin", "robots.txt", among others. (Warning> The robots.txt file is used to identify which directories may not be visible to search engines).

To use the script, simply execute it and input the URL of the site you want to check. The script will then search through the predefined directories and report whether each directory exists on the site or not.

### Credits
Matheus Laidler
