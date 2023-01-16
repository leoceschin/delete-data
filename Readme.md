# Delete Data
O Delete Data é uma solução para manter a sua privacidade um pouco mais intacta. Os metadados são uma grande fonte de informação tanto para empresas como para potenciais atacantes.
Limpar os seu arquivos desses metadados que podem acabar mostrando pontos de falha é essencial.

## Configuração
- Clone o projeto
- crie uma pasta chamada "upload" na raiz do projeto
- Crie um ambiente virtual
```
$python3 -m venv venv
```
- Ative o ambiente conforme sua plataforma
Linux/MacOS (não utilizo windows atualmente)
```
$source venv/bin/activate
```
- Instale as dependências
```
$pip install -r requirements.txt
```
- Antes de rodar a aplicação, verifique se a ferramenta "exiftool" está instalada na sua máquina. Caso não esteja, realize a instalação.
- Rode como um projeto flask
```
$export FLASK_APP=app.py
$flask run
```
Abra a aplicação no endereço <u>127.0.0.1:5000</u>.
![Captura de Tela 2023-01-16 às 02 09 23](https://user-images.githubusercontent.com/16521256/212619773-012da750-9a51-4f69-b870-2bc6882b4feb.png)

## Funcionamento
Ao fazer o upload de um arquivo e clicar em "Erase", a aplicação chama um subprocesso do sistema executando a ferramenta exiftool, ela remove os metadados do arquivo e o devolve para download.

<b>Antes</b>
![Captura de Tela 2023-01-16 às 04 12 28](https://user-images.githubusercontent.com/16521256/212620047-37ab3ea4-db67-4b92-8f71-060f86df740f.png)
![Captura de Tela 2023-01-16 às 04 23 10](https://user-images.githubusercontent.com/16521256/212620363-b6c042fb-2410-40b0-9303-e6c28a663b1e.png)


<b>Depois</b>
![Captura de Tela 2023-01-16 às 04 12 48](https://user-images.githubusercontent.com/16521256/212620392-4e4a4d3e-025a-4b27-8fb6-57dd7c6e4b8f.png)

Projeto desenvolvido por [Leona Ceschin](https://linkedin.com/in/leonaceschin)
