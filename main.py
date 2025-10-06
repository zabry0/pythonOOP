class car:
    """
    Zadejte základní parametry auta
    \nCenu auta udáváme v DPH
    """
    
    # Je možnost, kontrolovat si vstupní datové typy, které příjdou při instanci do objektu.
    # Zamezíme tím případným potížím.
    def __init__(self, znacka: str, rok: int, model: str, barva: str,typ_prevodovky: str, cena: float):
        self.znacka = str(znacka)
        self.rok = int(rok)
        self.model = str(model)
        self.barva = str(barva)
        self.typ_prevodovky = str(typ_prevodovky)
        self.cena = float(cena)

    def cena_bez_dph(self):
        """ Vypočítá cenu auta bez DPH"""
        return f" {self.cena * 0.79} kč"

    def vypis(self):
        """ Vypíše základní informace o autu"""
        return f"Název auta: {self.znacka} \nRok výroby: {self.rok} \nModel: {self.model} \nBarva: {self.barva} \n Typ převodovky: {self.typ_prevodovky} \n Cena včetně DPH: {self.cena} Kč, \n Cena bez DPH: {self.cena_bez_dph()}"

    def priplatkova_vybava(self, vybava: str, cena_vybavy: float):
        """ Přidá příplatkovou výbavu k autu"""
        return f"Připlatková výbava: {vybava}, cena příplatkové výbavy je: {cena_vybavy} Kč, celková cena auta s příplatkovou výbavou je: {self.cena + cena_vybavy} Kč"

audi = car("Audi", 2001,"A4", "stříbrná", "Manuální", 45000) #Instance
skoda = car("Škoda", 2014, "Superb II", "Bílá", "Manuální", 310000)

seznam_aut = [
    car("Audi", 2020, "A6", "Černá", "Automat", 850000),
    car("BMW", 2018, "X5", "Bílá", "Automat", 920000),
    car("Mercedes-Benz", 2019, "C-Class", "Modrá", "Automat", 780000),
    car("Volkswagen", 2017, "Passat", "Šedá", "Manuální", 430000),
    car("Škoda", 2021, "Octavia", "Červená", "Automat", 610000),
    car("Toyota", 2020, "Corolla", "Stříbrná", "Manuální", 490000),
    car("Hyundai", 2022, "Tucson", "Bílá", "Automat", 670000),
    car("Kia", 2021, "Sportage", "Zelená", "Automat", 640000),
    car("Ford", 2019, "Mondeo", "Modrá", "Manuální", 520000),
    car("Peugeot", 2018, "3008", "Černá", "Automat", 580000)
]

print("------------------------")
print(seznam_aut[0].znacka)
print("------------------------")


print(audi.rok)
print(skoda.model)
print(audi.vypis())
print(f"Cena auta bez DPH je: {audi.cena_bez_dph()}")
print(skoda.priplatkova_vybava("metalíza", 15000))

#print(seznam_aut)

for auto in seznam_aut:
    print(auto.vypis())
    print("-" * 50) 