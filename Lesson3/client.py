import socket
import json
import sys
from func import send_message, get_message


def create_presence_message(account_name='Guest'):
    result = {
        'action': 'presence',
        'user': {
            'account_name': account_name
        }
    }
    return result


def process_answer(message):
    if 'response' in message:
        if message['response'] == 200:
            return '200: OK'
        return f'400: {message["error"]}'


def main():
    try:
        server_addr = sys.argv[1]
        server_port = sys.argv[2]
        if int(server_port) < 1024 or int(server_port) > 65535:
            raise ValueError
    except IndexError:
        server_address = '127.0.0.1'
        server_port = 7777
    except ValueError:
        print(
            'В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_addr, int(server_port)))
    message_to_server = create_presence_message()
    send_message(transport, message_to_server)
    try:
        answer = process_answer(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
