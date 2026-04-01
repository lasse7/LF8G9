import datetime
import socket

LOGFILE = "monitor.log"


def log_message(message):
    with open(LOGFILE, "a") as f:
        f.write(message + "\n")
        
        

def check_value(value, soft_limit, hard_limit, text):
    hostname = socket.gethostname()
    timestamp = datetime.datetime.now()

    msg = f"{timestamp} | {hostname} | {text}: {value}"

    if value >= hard_limit:
        log_message("HARD ALARM: " + msg)
        send_email(msg)
        return "HARD"

    elif value >= soft_limit:
        log_message("WARNUNG: " + msg)
        return "SOFT"

    return "OK"