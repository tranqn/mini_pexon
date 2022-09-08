import pytest
import flaskr.pexon

def test_create(client):
    assert client.get('/').status_code == 200
    client.post('/test', data={'name': 'test'})


def test_update(client):
    assert client.post('/update').status_code == 403


def test_delete(client):
    assert client.post('/delete').status_code == 403