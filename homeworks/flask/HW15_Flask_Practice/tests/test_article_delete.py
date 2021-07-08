from tests.conftest import client
from app import app
from models.models import Article


def test_delete(client):
    with app.app_context():
        article = Article.query.order_by(Article.id.desc()).first()
        if article is not None:
            response = client.delete(f"/api/articles/{article.id}")
            assert response.status_code == 204
            response = client.get(f"/api/articles/{article.id}")
            assert response.status_code == 404
        else:
            print("There is nothing here")
