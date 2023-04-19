from flask import Flask, request, jsonify

from DataFrame import recommend_movies

app = Flask(__name__)

# Página inicial
@app.route('/')
def home():
    return 'Sistema de recomendação de filmes'

# Rota para a recomendação de filmes
@app.route('/recommendations', methods=['POST'])
def get_recommendations():
    # Obtém o ID do usuário a partir da requisição
    user_id = int(request.json['user_id'])

    # Obtém as recomendações
    recommended_movies = recommend_movies(user_id)

    # Retorna as recomendações como uma resposta JSON
    return jsonify({'movies': recommended_movies})

if __name__ == '__main__':
    app.run(debug=True)

