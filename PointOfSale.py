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
items = []
pryse = []

print("Gebruik enige tyd 'klaar' or 'verlaat' om die program te verlaat.")

x = 0
for x in range(999): # Die loop gaan vir 'n baie lang tyd aangaan, of todat die gebruiker besluit om die loop te verlaat.
    item = input("Item: ")
    if item == "klaar" or item == "Klaar" or item == "verlaat" or item == "Verlaat": # Om die loop te exit.
        print("Bereken totale prys...")
        break
    elif item == "" or item == " ": # Basiese fouthanteering.
        print("FOUT! Die item moet \'n naam hê.")
    else:
        items.append(item)

        # Nog 'n bietjie fouthanteering:
        f = False
        while not f:
            try:
                prys = float(input(f"Prys van '{item}': "))
            except ValueError:
                print("FOUT! Die item moet \'n geldige prys hê.")
            else:
                pryse.append(prys)
                break
        x += 1

print() #
x = 0 # Wis die waarde van x uit om weer die veranderlike te gebruik.
for x in range(len(items)):
    print(f"{items[x]}      R{pryse[x]}")

print("---------------")
print(f"Totaal R{sum(pryse)}")
print("===================")
