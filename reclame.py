from algemene_functies import mijn_functie_2

def aanbieding_1 (smaak, prijs, korting):
    prijs_na_korting=prijs*(1-korting)
    uitvoer_aanbieding_1 =  f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer_aanbieding_1
    
def inkomsten_totaal (inkomsten, btw):
    totaal = 0
    for bedrag in inkomsten:
        totaal+=bedrag
        btw_bedrag=totaal*btw
        uitvoer_inkomsten_totaal = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw_bedrag} euro btw betaald dient te worden."
        return totaal

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
