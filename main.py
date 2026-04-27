
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

def calculate():
    length = get_user_input("\nGeben Sie die Länge des Rechtecks ein: ")
    width = get_user_input("\nGeben Sie die Breite des Rechtecks ein: ")

    perimeter = 2 * (length + width)
    area = length * width
    print ("\n---------\n")
    print (f"Der Umfang des Rechtecks beträgt: {perimeter}")
    print (f"Die Fläche des Rechtecks beträgt: {area}")
    print ("\n---------\n")

def menu():
    while True:
        print ("\n**************************\n")
        print ("1 - Berechnung durchführen")
        print ("2 - Programm beenden")
        print ("\n**************************\n")
        choice = input("\nBitte wählen Sie eine Option: ")
        if choice == "1":
            calculate()
        elif choice == "2":
            print ("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print ("Ungültige Option. Bitte wählen Sie 1 oder 2.")

print("\033c", end="")


print ("\n===============================\n")
print ("Herzlich Willkommen zum Programm Rectangle Lab!")
print ("\nDieses Programm berechnet den Umfang und die Fläche eines Rechtecks.")
print ("\nBitte geben Sie die Länge und die Breite des Rechtecks ein, um fortzufahren.")

print ("\n===============================\n")

menu()
