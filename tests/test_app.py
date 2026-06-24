from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - Arranjo: onde preparamos o cenário para o teste
    - A: Act     - Acao: onde executamos a ação que queremos testar
    - A: Assert  - Garanta que A é A
    """
    # Arrange
    # client = TestClient(app)

    # Act
    response = client.get('/')

    # Assert
    assert response.json() == {'message': 'Olá Mundo!'}
    assert response.status_code == HTTPStatus.OK


# def test_root_html_deve_retornar_ok_e_ola_mundo():
#     """
#     Esse teste tem 3 etapas (AAA)
#     - A: Arrange - Arranjo: onde preparamos o cenário para o teste
#     - A: Act     - Acao: onde executamos a ação que queremos testar
#     - A: Assert  - Garanta que A é A
#     """
#     # Arrange
#     client = TestClient(app)

#     # Act
#     response = client.get('/html')

#     # Assert
#     assert '<h1>Olá Mundo!</h1>' in response.text
#     assert response.status_code == HTTPStatus.OK
