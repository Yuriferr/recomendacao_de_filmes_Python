# Sistema de Recomendação de Filmes

Este é um projeto em Python que utiliza a técnica de filtragem colaborativa para recomendar filmes para os usuários com base nas avaliações que eles deram para outros filmes.

## Requisitos

Para rodar este projeto, você precisa ter instalado:

- Python 3.x
- Bibliotecas: pandas, numpy, scikit-learn e Flask

## Como usar

Para utilizar o sistema, siga os passos abaixo:

1. Clone este repositório em sua máquina.
2. Instale as bibliotecas necessárias: `pip install pandas numpy scikit-learn Flask`.
3. Execute o script `prepare_data.py` para preparar os dados.
4. Execute o script `train_model.py` para criar o modelo de filtragem colaborativa.
5. Execute o script `app.py` para iniciar o servidor web.
6. Envie uma requisição POST para a rota `/recommendations` com o ID do usuário para o qual você deseja obter as recomendações.
7. O servidor irá retornar uma lista de filmes recomendados para aquele usuário.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues se tiver sugestões ou encontrar algum problema no código.

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo `LICENSE` para mais detalhes.
