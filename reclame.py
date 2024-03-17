from algemene_functies import mijn_functie_2

def aanbieding_1 (smaak, prijs, korting):
    if smaak == "aardbei" and prijs == 4 and korting == 0.1:
        return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs-(prijs*korting)} euro."
    
def inkomsten_totaal (inkomsten, btw):
    totaal = sum(inkomsten)
    return f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal*btw} euro btw betaald dient te worden."

def laag_en_hoog (mijn_lijst):
    uitersten = [max(mijn_lijst), min(mijn_lijst)]
    return uitersten

def gemiddelde (mijn_lijst):
    gemiddelde_inkomst = sum(mijn_lijst)/len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_inkomst} euro."

def meervoudig (invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie (invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
