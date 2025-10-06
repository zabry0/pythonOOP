

# Import knihovny random pro generování náhodných čísel (pro simulaci zaspání)
import random


 # Definice třídy Zamestnanec, která reprezentuje zaměstnance firmy
class Zamestnanec:
	"""
	Zadejte základní parametry zaměstnance
	\nPlat zaměstnance je v Kč
	"""
	# Třídní proměnná pro automatické generování unikátního ID každého zaměstnance
	_id_counter = 1

	# Konstruktor třídy, inicializuje vlastnosti zaměstnance
	def __init__(self, jmeno: str, prijmeni: str, pozice: str, plat: float, vek: int, oddeleni: str):
		# Automaticky generované unikátní ID
		self.id = Zamestnanec._id_counter
		Zamestnanec._id_counter += 1
		# Jméno zaměstnance
		self.jmeno = str(jmeno)
		# Příjmení zaměstnance
		self.prijmeni = str(prijmeni)
		# Pracovní pozice
		self.pozice = str(pozice)
		# Měsíční plat v Kč
		self.plat = float(plat)
		# Věk zaměstnance
		self.vek = int(vek)
		# Oddělení, kde zaměstnanec pracuje
		self.oddeleni = str(oddeleni)

	# Vrací celé jméno zaměstnance
	def cele_jmeno(self):
		return f"{self.jmeno} {self.prijmeni}"

	# Vrací roční plat zaměstnance
	def rocni_plat(self):
		return f"{self.plat * 12} Kč"

	# Vrací textový popis zaměstnance se všemi jeho vlastnostmi
	def vypis(self):
		return (f"ID: {self.id}\nJméno: {self.cele_jmeno()}\nPozice: {self.pozice}\nPlat: {self.plat} Kč\nVěk: {self.vek}\nOddělení: {self.oddeleni}\nRoční plat: {self.rocni_plat()}")

	# Přidá příplatek k platu zaměstnance a vypíše informaci
	def priplatek(self, castka: float, duvod: str):
		return f"Příplatek: {castka} Kč za {duvod}, nový plat: {self.plat + castka} Kč"

	# Vrací True, pokud zaměstnanec zaspal (50% šance), jinak False
	def pravdepodobnost_zaspani(self) -> bool:
		return random.random() < 0.5



# Vytvoření dvou instancí zaměstnanců pro ukázku
jan = Zamestnanec("Jan", "Novák", "Programátor", 50000, 30, "IT")
petr = Zamestnanec("Petr", "Svoboda", "Analytik", 48000, 28, "IT")

# Seznam 10 zaměstnanců uložený v listu
seznam_zamestnancu = [
	Zamestnanec("Jan", "Novák", "Programátor", 50000, 30, "IT"),
	Zamestnanec("Petr", "Svoboda", "Analytik", 48000, 28, "IT"),
	Zamestnanec("Eva", "Dvořáková", "Účetní", 42000, 35, "Finance"),
	Zamestnanec("Lucie", "Králová", "HR manažer", 47000, 32, "HR"),
	Zamestnanec("Martin", "Procházka", "Tester", 43000, 27, "IT"),
	Zamestnanec("Jana", "Benešová", "Marketing", 45000, 29, "Marketing"),
	Zamestnanec("Tomáš", "Veselý", "Obchodník", 46000, 31, "Obchod"),
	Zamestnanec("Veronika", "Horáková", "Asistentka", 39000, 26, "Administrativa"),
	Zamestnanec("Karel", "Černý", "Správce sítě", 44000, 34, "IT"),
	Zamestnanec("Petra", "Kučerová", "Projektový manažer", 55000, 36, "Management"),
]

# Výpis informací a šance zaspání pro každého zaměstnance v seznamu
for zam in seznam_zamestnancu:
	# Vypíše informace o zaměstnanci
	print(zam.vypis())
	# Vypíše, zda zaměstnanec zaspal (True/False)
	print(f"Zaměstnanec {zam.cele_jmeno()} zaspal: {zam.pravdepodobnost_zaspani()}")
	# Odděluje výpisy jednotlivých zaměstnanců
	print("-" * 50)

print("------------------------")
print(seznam_zamestnancu[0].jmeno)
print("------------------------")

print(jan.vek)
print(petr.pozice)
print(jan.vypis())
print(f"Roční plat zaměstnance je: {jan.rocni_plat()}")
print(petr.priplatek(5000, "bonus za projekt"))

# Výpis všech zaměstnanců pomocí cyklu
for zam in seznam_zamestnancu:
	print(zam.vypis())
	print("-" * 50)
