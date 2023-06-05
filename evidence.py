from pojisteny import Pojisteny

class Evidence:
    def __init__(self):
        self.pojisteni = []

    def vytvor_pojisteneho(self):
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = input("Zadejte věk: ")
        telefon = input("Zadejte telefonní číslo: ")
        pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(pojisteny)
        print("Pojištěný byl vytvořen.")

    def zobraz_seznam(self):
        if not self.pojisteni:
            print("Seznam pojištěných je prázdný.")
        else:
            for pojisteny in self.pojisteni:
                print(pojisteny)

    def vyhledej_pojisteneho(self):
        jmeno = input("Zadejte jméno nebo příjmení pojištěného:\n ")
        for pojisteny in self.pojisteni:
            if jmeno.lower() in pojisteny.jmeno.lower() or jmeno.lower() in pojisteny.prijmeni.lower():
                print(pojisteny)
                return
        print("Pojištěný nebyl nalezen.")
