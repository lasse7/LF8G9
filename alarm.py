import datetime
import socket
from email.message import EmailMessage
import smtplib

LOGFILE = "monitor.log"

last_states = {}

def log_message(message):
    with open(LOGFILE, "a") as f:
        f.write(message + "\n")


def send_email(message):
    msg = EmailMessage()
    msg.set_content(message)
    msg["Subject"] = "Monitoring Alarm"
    msg["From"] = "p_lasse@yahoo.de"
    msg["To"] = "lf8g9@yahoo.com"

    try:
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:
            server.starttls()
            server.login("p_lasse@yahoo.de", "frhxninmqnovtkwj")
            server.send_message(msg)
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