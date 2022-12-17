import unittest
from client import create_presence_message, process_answer


class TestClient(unittest.TestCase):
    def test_presence_message(self):
        test = create_presence_message()
        self.assertEqual(test, {'action': 'presence',
                         'user': {'account_name': 'Guest'}})

    def test_process_answer_200(self):
        self.assertEqual(process_answer({'response': 200}), '200: OK')

    def test_process_answer_400(self):
        self.assertEqual(process_answer(
            {'response': 400, 'error': 'Bad request'}), '400: Bad request')

    def test_process_no_answer(self):
        self.assertRaises(ValueError, process_answer, {'error': 'Bad Request'})
