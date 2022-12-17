import unittest
from server import process_client_message


class TestServer(unittest.TestCase):

    error_dict = {
        'response': 400,
        'error': 'Bad Request'
    }
    good_response_dict = {
        'response': 200
    }

    def test_process_no_action(self):
        self.assertEqual(process_client_message(
            {'user': {'account_name': 'Guest'}}), self.error_dict)

    def test_process_no_user(self):
        self.assertEqual(process_client_message(
            {'action': 'presence'}), self.error_dict)

    def test_wrong_action(self):
        self.assertEqual(process_client_message(
            {'action': 'Wrong', 'user': {'account_name': 'Guest'}}), self.error_dict)

    def test_process_good(self):
        self.assertEqual(process_client_message({'action': 'presence', 'user': {
                         'account_name': 'Guest'}}), self.good_response_dict)

    def test_process_wrong_user(self):
        self.assertEqual(process_client_message(
            {'action': 'presence', 'user': {'account_name': 'Guest1'}}), self.error_dict)
