def mijn_functie_1(getal):
    return getal ** 2

def mijn_functie_2(a, b):
    return [a + b, a - b, a * b, a // b]

print("Argumenten\tTeruggeefwaarde")
print("-----------------------------")

argumenten = [2, 4, 10, 12]

for getal in argumenten:
    resultaat = mijn_functie_1(getal)
    print(f"{getal}\t\t{resultaat}")

print("\nArgumenten\tTeruggeefwaarde")
print("-----------------------------------------")

argumenten_2 = [(12, 3), (12, 2), (10, 5), (100, 20)]

for a, b in argumenten_2:
    resultaat = mijn_functie_2(a, b)
    print(f"{a}, {b}\t\t{resultaat}")