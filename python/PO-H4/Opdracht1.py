import math # Importeer math

print("LET OP: Voer decimalen in als \"5.2\", niet als \"5,2\"") # Om fouten te voorkomen

oppervlakte = float(input("Wat is de oppervlakte van de kamer in m²?") ) # Vraag om de opervlakkte van de kamer

if not oppervlakte: # Als er GEEN oppervlakte is
    print("geen geldige input!")

print("De kamer is "+ str(oppervlakte) +" m²")

oppervlakte = oppervlakte * 1.1 # Doe de oppervlakte keer 1.1   OF  oppervlakte *= 1.1

oppervlakte = round(oppervlakte, 2) # Rond de oppervlakte af naar 2 decimalen 
print("Er is "+ str(oppervlakte) +" m² nodig.")

pakken = math.ceil(oppervlakte/2.47) # Bereken het aantal pakken. Je kan geen halve pakken hebben, dus rond je af naar het eerstvolgende pak
print("Je hebt "+str(pakken)+" pakken nodig.")

prijs = pakken * 29.62 # Bereken de prijs
print("Het kost je €" +str(prijs))

print("\nGemaakt door [NAAM]")