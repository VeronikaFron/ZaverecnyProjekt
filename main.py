from evidence import Evidence

def main():
    evidence = Evidence()

    while True:
        print("\n----- Menu -----")
        print("1. Vytvořit pojištěného")
        print("2. Zobrazit seznam pojištěných")
        print("3. Vyhledat pojištěného")
        print("0. Ukončit program")

        volba = input("Vyberte jednu z možností:\n ")
        print("----------------")

        if volba == "1":
            evidence.vytvor_pojisteneho()
        elif volba == "2":
            evidence.zobraz_seznam()
        elif volba == "3":
            evidence.vyhledej_pojisteneho()
        elif volba == "0":
            break
        else:
            print("Neplatná volba. Zadejte prosím číslo jedné z možností v menu.")


if __name__ == "__main__":
    main()
