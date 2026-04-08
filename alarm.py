import datetime                                                                 # Bibliothek für aktuellen Zeitstempel
import socket                                                                   # Bibliothek für Hostname
from email.message import EmailMessage                                          # Bibliothek für EMail Nachricht
import smtplib                                                                  # Bibliothek für EMail Versand

LOGFILE = "monitor.log"                                                         # Variable für Dateinamen der Log-Datei

#  (von KI)
last_states = {}                                                                # Variable für Speichern des letzten Zustands gegen Spam-Mails

def log_message(message):                                                       # Funktion für schreiben der Log-Datei
    with open(LOGFILE, "a") as f:                                               # Erstelle/öffne Datei ("a" für Text anhängen)
        f.write(message + "\n")                                                 # schreibe in die Datei ("\n" = Zeilenumbruch)


def send_email(message):                                                        # Funktion für EMail Versand
    msg = EmailMessage()                                                        # Speichern der Email-Formation in Variable msg
    msg.set_content(message)                                                    # schreiben der Nachricht in die EMail-Formation
    msg["Subject"] = "Monitoring Alarm"                                         # setzen des Betreffs
    msg["From"] = "p_lasse@yahoo.de"                                            # setzen des Absenders
    msg["To"] = "lf8g9@yahoo.com"                                               # setzen des Empfängers

    try:                                                                        # Senden in try setzen, um Fehlermitteilungen ermitteln zu können
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as server:                # setzen des SMTP-Servers
            server.starttls()
            server.login("p_lasse@yahoo.de", "frhxninmqnovtkwj")                 
            server.send_message(msg)                                            # Nachricht senden
    except Exception as e:
        print("E-Mail Fehler:", e)                                              # Ausgabe der Fehlermeldung


def check_value(value, soft_limit, hard_limit, text):                           # Funktion zur Prüfung auf Alarm-Werte
    hostname = socket.gethostname()                                             # Ermittlung des Gerätenamens
    timestamp = datetime.datetime.now()                                         # Ermittlung des aktuellen Zeitstempels

    msg = f"{timestamp} | {hostname} | {text}: {value}"                         # Speichern der Nachricht für Log-Datei und EMail

 #   if value >= hard_limit:                                                     # Prüfen ob aktueller Wert >= Alarm-Obergrenze
 #       log_message("HARD ALARM: " + msg)                                       # Aufruf der Log-Datei-Funktion
 #       send_email(msg)                                                         # Aufruf der EMail-Senden-Funktion
 #       return "HARD"                                                           # Rückgabewert / exit aus dieser Funktion falls if = ja

 #   elif value >= soft_limit:                                                   # Prüfen ob aktueller Wert >= Alarm-Warngrenze
 #       log_message("WARNUNG: " + msg)                                          # Aufruf der Log-Datei-Funktion
 #       return "SOFT"                                                           # Rückgabewert / exit aus dieser Funktion falls if = ja

 #   return "OK"                                                                 # Rückgabewert / exit aus dieser Funktion falls beide if = nein
    
    if value >= hard_limit:                                                     # Prüfen ob aktueller Wert >= Alarm-Obergrenze
        state = "HARD"                                                          # Setzen des Rückgabewertes
    elif value >= soft_limit:                                                   # Prüfen ob aktueller Wert >= Alarm-Warngrenze
        state = "SOFT"                                                          # Setzen des Rückgabewertes
    else:                                                                       # falls beide if = nein
        state = "OK"                                                            # Setzen des Rückgabewertes

    # alter Zustand  (von KI)
    last_state = last_states.get(text)

    # nur reagieren wenn sich Zustand ändert  (von KI)
    if state != last_state:

        if state == "HARD":
            log_message("HARD ALARM: " + msg)
            send_email(msg)

        elif state == "SOFT":
            log_message("WARNUNG: " + msg)

        elif state == "OK":
            log_message("INFO: Zustand wieder OK: " + msg)

    # Zustand speichern  (von KI)
    last_states[text] = state

    return state