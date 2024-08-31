import time

def logging_error(message: Exception):
    print(message)
    with open("error_log.txt", "a") as error_log:
        error_log.write(f"{time.ctime(time.time())} ->\n{message}\n\n")