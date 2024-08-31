from AppOpener import open, close

from modules.logging import logging_error

def open_app(app_name):
    try:
        open(app_name, throw_error=True)
        return True
    except Exception as e:
        logging_error(e)
        return False

def close_app(app_name):
    try:
        close(app_name, throw_error=True)
        return True
    except Exception as e:
        logging_error(e)
        return False