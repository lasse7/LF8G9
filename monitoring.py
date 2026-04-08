import time                                                             # timer für Intervall
import psutil                                                           # Bibliothek für Hardware-Werte
import os                                                               # Betriebssystem für Disk-Pfad
import argparse                                                         # Bibliothek für Parameter-Übergabe
from alarm import check_value                                           # import benutzter Funktion


def check_memory(soft, hard):
    memory = psutil.virtual_memory().percent                            # speichern des RAM-Verbrauchs in %
    return check_value(memory, soft, hard, "Memory usage (%)")          # Rückgabe von check_memory = prüfen des Wertes auf Alarm-Grenzen (Rückgabe von check_value mit aktuellem Wert)


def check_processes(soft, hard):
    processes = len(psutil.pids())                                      # speichern der Anzahl der laufenden Prozesse
    return check_value(processes, soft, hard, "Process count")          # Rückgabe von check_processes = prüfen des Wertes auf Alarm-Grenzen (Rückgabe von check_value mit aktuellem Wert)
    
def check_disk(soft, hard):
    path = "/"                                                          # setzen des Pfades der Haupt-Festplattenpartition (hier standard Linux)
    if os.name == "nt":                                                 # prüfen ob Betriebssystem Windows ist
        path = "C:"                                                     # falls ja: ändern des Pfades auf C:
   # else:  
   #     path = "/"
    
    disk = psutil.disk_usage(path).percent                              # speichern des Festplatten-Verbrauchs in %
    return check_value(disk, soft, hard, "Disk usage (%)")              # Rückgabe von check_disk = prüfen des Wertes auf Alarm-Grenzen (Rückgabe von check_value mit aktuellem Wert)


def main():
    parser = argparse.ArgumentParser()                                  # setzen von Standardwerten und Ermöglichung von Parameter-Übergabe bei Skript-Aufruf
    parser.add_argument("--mem-soft", type=int, default=70)
    parser.add_argument("--mem-hard", type=int, default=90)
    parser.add_argument("--proc-soft", type=int, default=150)
    parser.add_argument("--proc-hard", type=int, default=300)
    parser.add_argument("--disk-soft", type=int, default=70)
    parser.add_argument("--disk-hard", type=int, default=90)
    parser.add_argument("--interval", type=int, default=10)             # Sekunden

    args = parser.parse_args()

    try:                                                                # Schleife in try verpacken für manuellen Abbruch des Skripts
        while True:                                                     # Dauerschleife des Hauptprogramms
            print("---- Monitoring ----")                               # Start Ausgabe

            print("Memory:", check_memory(args.mem_soft, args.mem_hard))            # Ausgabe der Prüfung des RAM-Verbrauchs mit übergebenen Parametern oder Standardwert
            print("Processes:", check_processes(args.proc_soft, args.proc_hard))    # Ausgabe der Prüfung der Prozess-Anzahl  mit übergebenen Parametern oder Standardwert
            print("Disk:", check_disk(args.disk_soft, args.disk_hard))              # Ausgabe der Prüfung des Festplatten-Verbrauchs mit übergebenen Parametern oder Standardwert

            time.sleep(args.interval)                                   # Dauerschleife für Intervall-Sekunden aussetzen

    except KeyboardInterrupt:                                           # Abbruch bei Strg+C
        print("Monitoring beendet")                                     # Ausgabe Abbruch

if __name__ == "__main__":                                              # Aufruf der Hauptfunktion bei Skript-Start
    main()