
class Car:
    def __init__(
        self,
        znacka: str,
        rok: int,
        model: str,
        barva: str,
        typ_prevodovky: str,
        cena: float
    ):
        self.znacka: str = znacka
        self.rok: int = rok
        self.model: str = model
        self.barva: str = barva
        self.typ_prevodovky: str = typ_prevodovky
        self.cena: float = cena


    def cena_bez_dph(self) -> float:
        return self.cena / 1.21


    def Vypis(self) -> str:
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


auto = [
    Car("Audi", 1999, "A4", "stříbrná", "Manuální", 45000),
    Car("Škoda", 2014, "Superb II", "Bílá", "Manuální", 31000),
    Car("BMW", 2020, "X5", "Černá", "Automatická", 1200000),
    Car("Ford", 2018, "Focus", "Modrá", "Manuální", 250000),
    Car("Toyota", 2021, "Corolla", "Červená", "Automatická", 600000),
    Car("Honda", 2017, "Civic", "Šedá", "Manuální", 300000),
    Car("Mercedes", 2019, "C-Class", "Bílá", "Automatická", 800000),
    Car("Volkswagen", 2015, "Golf", "Zelená", "Manuální", 200000),
    Car("Nissan", 2022, "Altima", "Modrá", "Automatická", 700000),
    Car("Hyundai", 2016, "Elantra", "Stříbrná", "Manuální", 220000)
]
for a in auto:
    print(a.Vypis())

