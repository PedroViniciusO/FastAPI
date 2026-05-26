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


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            },
        ],
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'novasenha'
        }
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted successfully'}


# # Exercício

# def test_update_user_should_not_found_exercicio(client):
#     response = client.put(
#         '/users/999',
#         json={
#             'username': 'alice',
#             'email': 'alice@example.com',
#             'password': 'secret',
#         }
#     )
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# def test_delete_user_should_not_found_exercicio(client):
#     response = client.delete('/users/999')

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# def test_get_user_should_not_found_exercicio(client):
#     response = client.get('/users/999')

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# # def test_get_user_exercicio(client):
# #     response = client.get('/users/1')

# #     assert response.status_code == HTTPStatus.OK
# #     assert response.json() == {
# #     'username': 'alice',
# #     'email': 'alice@example.com',
# #     'password': 'secret',
# #     'id': 1,
# #     }
