from pexon import app
import unittest


class RoutesTest(unittest.TestCase):

    # Check for response 404
    def test_delete(self):
        tester = app.test_client(self)
        response = tester.get("/delete")
        statuscode = response.status_code
        self.assertEqual(statuscode, 404)

    # Check for response 200
    def test_update(self):
        tester = app.test_client(self)
        response = tester.get("/update")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__ == "__main__":
    unittest.main()
