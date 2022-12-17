import logging


format = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(module)s - %(message)s ")
server_log = logging.FileHandler('server_log')
server_log.setFormatter(format)

log = logging.getLogger('log')
log.addHandler(server_log)
log.setLevel(logging.DEBUG)
