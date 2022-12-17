import logging


format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(module)s - %(message)s ")
client_log = logging.FileHandler('client_log')
client_log.setFormatter(format)

log = logging.getLogger('log')
log.addHandler(client_log)
log.setLevel(logging.DEBUG)
