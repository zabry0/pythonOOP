class Car:
 
    def __init__(self, znacka: str, rok: str, model: str, barva: str, typ_prevodovky: str, cena: float):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena
 
    def Vypis(self):
        return f"Název auta: {self.znacka}, Rok výroby: {self.rok}"

audi = Car("Audi", 1999, "A4", "stříbrná", "Manualní", 45000 )
skoda = Car("Škoda", 2014, "Superb II", "Bíla", "manualní", 31000)
 
print(audi.znacka)
print(skoda.znacka)
print(audi.Vypis())  
