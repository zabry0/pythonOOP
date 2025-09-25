class Car:
    def __init__(self, znacka: str, rok: int, model: str, barva: str, typ_prevodovky: str, cena: float):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena

    def cena_bez_dph(self):
        return self.cena / 1.21

    def Vypis(self):
        return f"""--- Auto ---
Značka: {self.znacka}
Rok výroby: {self.rok}
Model: {self.model}
Barva: {self.barva}
Typ převodovky: {self.typ_prevodovky}
Cena bez DPH: {self.cena_bez_dph():.2f} Kč
"""

audi = Car("Audi", 1999, "A4", "stříbrná", "Manuální", 45000)
skoda = Car("Škoda", 2014, "Superb II", "Bílá", "Manuální", 31000)
bmw = Car("BMW", 2020, "X5", "Černá", "Automatická", 1200000)

print(audi.Vypis())
print(skoda.Vypis())
print(bmw.Vypis())
