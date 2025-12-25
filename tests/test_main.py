from main import greet

def test_greet(capsys):
    # Appel de la fonction
    greet("Alice")
    
    # Capture de la sortie standard (print)
    captured = capsys.readouterr()
    
    # Vérification que la sortie correspond à ce qui est attendu
    assert captured.out == "Bonjour, Alice!\n"