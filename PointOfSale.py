# Program deur Gerrit Smuts
#
# ====INSTRUKSIES====
# Die POS moet hardloop op "command line" (CMD)
# Die POS moet elke item in 'n List stoor
# Die POS moet die uitset kan verwyder
# Elke POS bewerking moet in 'n funksie wees.
# Maak gebruik van 'n "for" of "for each loop" met 'n "sentinel variable" wat gebruik kan word om die "loop" te exit.
# Gebruik # kommentaar met 'n volledige beskrywing van kode se funksie.
# Al die produkte met hul pryse saam met die  totaal moet vertoon word van al die produkte wat gestoor is bv:
# Kaas   R50.00
# Melk   R30.00
# Brood R15.00
# ---------------
# Totaal R95.00
# ===================

print("====WELKOM====")
# verlaat = False
items = []
pryse = []

"""
while not verlaat:

    try: # Toets vir ValueError
        hoeveel = int(input("Hoeveel items het die kliënt? "))
        for x in range(hoeveel):
            # items.append(input("Item naam: "))
            item = input("Item: ")
            if item == "" or item == " ":
                print("FOUT! Verskaf asseblief \'n naam vir die item.")
                break
            else:
                items.append(item)

            pryse.append(float(input(f"Prys van '{items[x]}': "))) # Toets vir ValueError
            x += 1
    except ValueError:
        print("FOUT! Probeer asseblief weer.")
    else:

        x = 0

        for x in range(hoeveel):
            print(f"{items[x]}   R{pryse[x]}")
        print("---------------")
        print(f"Totaal R{sum(pryse)}")
        print("# ===================")
"""

print("Gebruik enige tyd 'klaar' or 'verlaat' om die program te verlaat.")

x = 0
for x in range(999): # Die loop gaan vir 'n baie lang tyd aangaan, of todat die gebruiker besluit om die loop te verlaat.
    item = input("Item: ")
    """
    if item == "" or item == " ":
        raise ValueError("FOUT! Die item moet \'n naam hê.")
    """
    if item == "klaar" or item == "Klaar" or item == "verlaat" or item == "Verlaat":
        print("Bereken totale prys...")
        break
    else:
        items.append(item)
        pryse.append(float(input(f"Prys van '{item}': ")))
        x += 1
        """
        nog = input("Is daar nog \'n item? (ja/nee): ")
        if nog == "ja" or nog == "Ja" or nog == "y":
            x += 1
            # continue
        else:
            break
        """

"""
print()
x = ""
try:
    for x in items:
        pryse.append(float(input(f"Prys van '{x}': ")))


except ValueError:
    print("FOUT! Die item moet \'n prys hê.")
"""

print()

x = 0
for x in range(len(items)):
    print(f"{items[x]}      R{pryse[x]}")

print("---------------")
print(f"Totaal R{sum(pryse)}")
print("===================")
