from flask import Flask, jsonify, request

# Criando servidor que ira hospedar a API
app = Flask(__name__)


# Criando lista com livros que serão utilizados
livros = [
    {
        'id': 1,
        'titulo': 'Harry Potter - A Pedra Filosofal',
        'autor': 'J.K Rowling'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter - A Camara Secreta',
        'autor': 'J.K Rowling'
    },
    {
        'id': 3,
        'titulo': 'Harry Potter - O Prizioneiro de Azkaban',
        'autor': 'J.K Rowling'
    },
    {
        'id': 4,
        'titulo': 'Harry Potter - O Calice de Fogo',
        'autor': 'J.K Rowling'
    },
    {
        'id': 5,
        'titulo': 'Harry Potter - A Ordem da Fenix',
        'autor': 'J.K Rowling'
    },
    {
        'id': 6,
        'titulo': 'Harry Potter - O Enigma do Principe',
        'autor': 'J.K Rowling'
    },
    {
        'id': 7,
        'titulo': 'Harry Potter - As Reliquias do Morte',
        'autor': 'J.K Rowling'
    },
]

# Consultar todos 
@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livros_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
        
# Criar novo livro
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id: 
            del livros[indice]
    
    return jsonify(livros)

# Informações gerais da API
app.run(port=5000, host='localhost', debug=True)

