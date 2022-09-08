import pytest
import flaskr.pexon

def test_create(client):
    assert client.get('/').status_code == 200
    client.post('/test', data={'name': 'test'})


def test_update(client):
    assert client.post('/update').status_code == 403


def test_delete(client):
    assert client.post('/delete').status_code == 403


# class RoutesTest(unittest.TestCase):


#     # Check for response 404
#     def test_add(self):
#         tester = app.test_client(self)
#         response = tester.get("/delete")
#         statuscode = response.status_code
#         self.assertEqual(statuscode, 404)


#     # Check for response 404
#     def test_delete(self):
#         tester = app.test_client(self)
#         response = tester.get("/delete")
#         statuscode = response.status_code
#         self.assertEqual(statuscode, 404)


#     # Check for response 200
#     def test_update(self):
#         tester = app.test_client(self)
#         response = tester.get("/update")
#         statuscode = response.status_code
#         self.assertEqual(statuscode, 200)


# if __name__ == "__main__":
#     unittest.main()
