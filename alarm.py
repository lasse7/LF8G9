import datetime
import socket
import smtplib

LOGFILE = "monitor.log"

last_states = {}

def log_message(message):
    with open(LOGFILE, "a") as f:
        f.write(message + "\n")


def send_email(message):
    sender = "lf8g9@yahoo.de"
    receiver = "lf8g9@yahoo.de"

    try:
        with smtplib.SMTP("smtp.mail.yahoo.com", 465) as server:
            server.starttls()
            server.login("lf8g9@yahoo.de", "Anfang-1")
            server.sendmail(sender, receiver, message)
    except Exception as e:
        print("E-Mail Fehler:", e)


def check_value(value, soft_limit, hard_limit, text):
    hostname = socket.gethostname()
    timestamp = datetime.datetime.now()

    msg = f"{timestamp} | {hostname} | {text}: {value}"

 #   if value >= hard_limit:
 #       log_message("HARD ALARM: " + msg)
 #       send_email(msg)
 #       return "HARD"

 #   elif value >= soft_limit:
 #       log_message("WARNUNG: " + msg)
 #       return "SOFT"

 #   return "OK"
    
    if value >= hard_limit:
        state = "HARD"
    elif value >= soft_limit:
        state = "SOFT"
    else:
        state = "OK"

    # alter Zustand
    last_state = last_states.get(text)

    # nur reagieren wenn sich Zustand ändert
    if state != last_state:

        if state == "HARD":
            log_message("HARD ALARM: " + msg)
            send_email(msg)

        elif state == "SOFT":
            log_message("WARNUNG: " + msg)

        elif state == "OK":
            log_message("INFO: Zustand wieder OK: " + msg)

    # Zustand speichern
    last_states[text] = state

    return state