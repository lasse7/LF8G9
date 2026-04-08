from monitoring import check_memory, check_processes, check_disk          # zu benutzende Funktionen importieren

def test_memory():
    result = check_memory(0, 100)                                         # zu testende Funktion mit entsprechenden Werten aufrufen
    assert result in ["OK", "SOFT", "HARD"]                               # prüfe, ob Rückgabewert innerhalb dieser Ausgaben

def test_processes():
    result = check_processes(0, 10000)                                    # zu testende Funktion mit entsprechenden Werten aufrufen
    assert result in ["OK", "SOFT", "HARD"]                               # prüfe, ob Rückgabewert innerhalb dieser Ausgaben
    
    
def test_disk():
    result = check_disk(0, 100)                                           # zu testende Funktion mit entsprechenden Werten aufrufen
    assert result in ["OK", "SOFT", "HARD"]                               # prüfe, ob Rückgabewert innerhalb dieser Ausgaben