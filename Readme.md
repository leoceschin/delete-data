# Delete Data
O Delete Data é uma solução para manter a sua privacidade um pouco mais intacta. Os metadados são uma grande fonte de informação tanto para empresas como para potenciais atacantes.
Limpar os seu arquivos desses metadados que podem acabar mostrando pontos de falha é essencial.

## Configuração
- Clone o projeto
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



## Funcionamento
Ao fazer o upload de um arquivo e clicar em "Erase", a aplicação chama um subprocesso do sistema executando a ferramenta exiftool, ela remove os metadados do arquivo e o devolve para download.

<b>Antes</b>

<b>Depois</b>