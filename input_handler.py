def get_user_input(text):
    while True:
        value = input(text).replace(",", ".")
        try:
            number = float(value)
            
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            continue
        if number <= 0:
            print ("Ungültige Eingabe. Bitte geben Sie eine positive Zahl ein.")
            continue
        
        return number