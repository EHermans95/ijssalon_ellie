prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: aardbeien-ijs, 1 liter - slechts € {aanbieding}"
reclame_tekst2 = reclame_tekst [:64]
reclame_tekst3 = reclame_tekst2.upper()
reclame_tekst4 = reclame_tekst3.split(" ")
for el in reclame_tekst4:
    if len(el)>=5:
        print(el.upper())
    else:
        print(el.lower())

