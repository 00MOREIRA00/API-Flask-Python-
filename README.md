# API-administrar-livros
Esse desenvolvimento foi utilizado para o estudo da linguagem Python e da criação de APIS utilizando Flask. 

## Como foi feito? 
Para o desenvolvimento da API utilizamos o Flask, porem o que é Flask? 

Flask é um microframework para desenvolvimento web em Python. Ele fornece as ferramentas básicas para criar aplicações web, como gerenciamento de rotas e requisições HTTP, sem fornecer muitos recursos adicionais ou configurações complexas.

Para o desenvolvimento devemos focar nesses 4 pilares:

1. Objetivo - Criar uma api que disponibiliza a consulta, criação, edição e exclusão de livros.

2. URL - localhost

3. Enpoints - 
    * localhost/livros (GET)
    * localhost/livros/id (GET)
    * localhost/livros (POST)
    * localhost/livros/id (PUT)
    * localhost/livros/id (DELETE)

4. Quais recursos - Livros

Para o desenvolvimento de APIs usando Python temos algumas possibilidades, dentre elas tive como opção o flask e django, porém optei pela utilização do flask.

```
1º Passo 
Inicialmente o instalei usando o terminal


PIP INSTALL FLASK
```
 
```
2º Passo
Após a instalação é necessário que importemos algumas funcionalidades da biblioteca para que sejam utilizadas no desenvolvimento

from flask import Flask, jsonify, request

Flask - Utilizamos para desenvolver a API;
Jsonify - Utilizamos para que possamos usar o Json;
Request - Utilizamos para obter as informações que estão trafegando nas requisições;
```

```
3º Passo 
Criamos uma aplicação Flask com o nome do arquivo atual

app = Flask(__name__)
```

```
4º Passo 
Criamos uma lista com livros para que possamos fazer nossas operações em cima delas, sem a necessidade da criação de um banco.

livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter - A Pedra Filosofal',
        'autor': 'J.K Rowling'
    }
]
```

```
5º Passo 
Criamos a rota principal da API que será consumida

app.run(port=5000, host='localhost', debug=True)
```

```
6º Passo 
As chamadas da API com seus diferentes métodos funcionam através de funções, então criamos uma parada cada uma delas, criando sempre uma rota especifica para cada uma delas e especificando um método que será usada para cada função criada.

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)
```






