from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_verify_score():
    query = """
    mutation {
        verify(score: "3x15") {
            combinations
        }
    }
    """
    response = client.post('/graphql', json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "verify" in data["data"]
    assert "combinations" in data["data"]["verify"]
    assert data["data"]["verify"]["combinations"] == 4

def test_verify_invalid_score():
    query = """
    mutation {
        verify(score: "8x5") {
            combinations
        }
    }
    """
    response = client.post('/graphql', json={"query": query})
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert "verify" in data["data"]
    assert "combinations" in data["data"]["verify"]
    assert data["data"]["verify"]["combinations"] == 0