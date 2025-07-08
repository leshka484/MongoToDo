
def test_read_main(client):
    response = client.get("/")
    assert response.json() == {"msg": "Hello World"}