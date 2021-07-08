from tests.conftest import client
from io import BytesIO


def test_article_form(client):
    response = client.get('/article/create')
    assert response.status_code == 200

    with open('static/uploads/Screenshot from 2021-03-26 16-44-13.jpg', 'rb') as img:
        img_bytes = BytesIO(img.read())
    data = {
        'title': 'test record',
        'slug': 'test-record',
        'description': 'Bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla',
        'short_description': 'Bla bla bla bla bla bla',
        'img': (img_bytes, 'img.jpg')
    }

    response = client.post('/article/store', content_type='multipart/form-data', data=data)
    assert response.status_code == 302
