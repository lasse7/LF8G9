from alarm import check_value                                       # zu benutzende Funktionen importieren

def test_soft_limit():
    result = check_value(85, 80, 90, "Testwert")                    # zu testende Funktion mit entsprechenden Werten aufrufen
    assert result == "SOFT"                                         # prüfe, ob Rückgabewert gleich erwarteter Wert

def test_hard_limit():
    result = check_value(95, 80, 90, "Testwert")                    # zu testende Funktion mit entsprechenden Werten aufrufen
    assert result == "HARD"                                         # prüfe, ob Rückgabewert gleich erwarteter Wert

def test_ok():
    result = check_value(50, 80, 90, "Testwert")                    # zu testende Funktion mit entsprechenden Werten aufrufen
    assert result == "OK"                                           # prüfe, ob Rückgabewert gleich erwarteter Wert