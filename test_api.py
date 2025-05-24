from apiPYTHON import app

def test_hello():
    client = app.test_client()
    response = client.get('/api')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}

def test_soma():
    client = app.test_client()
    response = client.get('/api/soma?a=10&b=5')
    assert response.status_code == 200
    assert response.json == {"result": 15}
    