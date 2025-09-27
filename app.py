""" from abc import ABC, abstractmethod
class Persona:
    # Costruttore della classe
    def __init__(self, nome, eta):
        self.nome = nome        # Attributo pubblico
        self.eta = eta          # Attributo pubblico
        self._id = 0           # Attributo protetto (convenzione)
        self.__password = ""   # Attributo privato
    
    # Metodo pubblico
    def saluta(self):
        return f"Ciao, sono {self.nome} e ho {self.eta} anni"
    
    # Metodo per modificare l'età (getter/setter)
    def compleanno(self):
        self.eta += 1
        print(f"Buon compleanno {self.nome}! Ora hai {self.eta} anni")
    
    # Metodo privato
    def __metodo_privato(self):
        return "Questo è un metodo privato"

# Creazione di oggetti
persona1 = Persona("Mario", 25)
persona2 = Persona("Lucia", 30)

print(persona1.saluta())
print(persona2.saluta())
persona1.compleanno()

class Studente(Persona):
    def __init__(self, nome, eta, corso):
        super().__init__(nome, eta)  # Chiama il costruttore della classe padre
        self.corso = corso
        self.voti = []
    
    def aggiungi_voto(self, voto):
        if 0 <= voto <= 10:
            self.voti.append(voto)
        else:
            print("Voto non valido!")
    
    def media_voti(self):
        if self.voti:
            return sum(self.voti) / len(self.voti)
        return 0
    
    # Override del metodo saluta
    def saluta(self):
        return f"Ciao, sono {self.nome}, studio {self.corso} e ho {self.eta} anni"

class Docente(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.materia = materia
        self.stipendio = 0
    
    def insegna(self):
        return f"{self.nome} insegna {self.materia}"
    
    def saluta(self):
        return f"Buongiorno, sono il/la prof. {self.nome}, insegno {self.materia}"

# Esempio di utilizzo
studente = Studente("Anna", 20, "Informatica")
docente = Docente("Prof. Rossi", 45, "Matematica")

print(studente.saluta())
print(docente.saluta())
print(docente.insegna())

studente.aggiungi_voto(8)
studente.aggiungi_voto(9)
print(f"Media voti: {studente.media_voti()}")

def presenta_persona(persona):

    print(persona.saluta())  # Ogni classe ha la sua implementazione

# Lista di oggetti di classi diverse
persone = [
    Persona("Giovanni", 35),
    Studente("Sofia", 19, "Fisica"),
    Docente("Prof. Bianchi", 50, "Storia")
]

print("\n--- Esempio di Polimorfismo ---")
for persona in persone:
    presenta_persona(persona)

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
    
    def area(self):
        return self.base * self.altezza
    
    def perimetro(self):
        return 2 * (self.base + self.altezza)

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio
    
    def area(self):
        return 3.14159 * self.raggio ** 2
    
    def perimetro(self):
        return 2 * 3.14159 * self.raggio

# Esempio di utilizzo
rettangolo = Rettangolo(5, 3)
cerchio = Cerchio(4)

print(f"\nRettangolo - Area: {rettangolo.area()}, Perimetro: {rettangolo.perimetro()}")
print(f"Cerchio - Area: {cerchio.area():.2f}, Perimetro: {cerchio.perimetro():.2f}") """

""" class Materia:
    def __init__(self, nome, coeff):
        self.nome=nome
        self.coeff=coeff
        self._difficoltà="Alta"
        self.__credit=10
    def dim_coeff(self):
        self.coeff-=1
        return f" Sono la Materia {self.nome}, adesso il mio coeff è {self.coeff}"
    def _boh(self):
        return f"Sono {self.nome} e tutti hanno paura di me!!!"
    def get_credit(self):
        return self.__credit
    def set_credit(self,credit):
        self.__credit=credit
    
materia=Materia("Math", 6)
print(materia.get_credit())
materia.set_credit(11)
print(materia.get_credit())

#print(materia._Materia_difficoltà)
#print(materia.dim_coeff()) """


""" import json

studenti_data={
    "studenti":[
         {
            "nome": "Mario",
            "eta": 20,
            "corso": "Informatica",
            "voti": [8, 9, 7, 10]
        },
        {
            "nome": "Lucia",
            "eta": 19,
            "corso": "Matematica",
            "voti": [9, 8, 9, 7]
        },
        {
            "nome": "Giovanni",
            "eta": 21,
            "corso": "Fisica",
            "voti": [7, 8, 6, 9]
        }
    ]

}

def scrivi_file_json(data,filename):
    try:
        with open(filename,"w", encoding="UTF-8") as file:
            json.dump(data,file,indent=3,ensure_ascii=False)
    except Exception as e:
        print(e)


def leggi_file_json(filename):
    with open(filename,"r",encoding="UTF-8") as file:
        data=json.load(file)
        print(data)
leggi_file_json("studenti.json")

data_dict={
    "boh1":12,
    "boh2":"boh2",
    "boh3":False,
    "boh4":12.6

}

print(json.loads(json.dumps(data_dict))) """
import csv
from datetime import datetime

# Dati di esempio
studenti_csv = [
    ["Nome", "Eta", "Corso", "Voto1", "Voto2", "Voto3", "Media"],
    ["Mario", 20, "Informatica", 8, 9, 7, 8.0],
    ["Lucia", 19, "Matematica", 9, 8, 9, 8.7],
    ["Giovanni", 21, "Fisica", 7, 8, 6, 7.0],
    ["Anna", 22, "Chimica", 10, 9, 8, 9.0]
]

# 1. SCRIVERE CSV
def scrivi_csv(data, filename):
    """Scrive dati in formato CSV"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"CSV scritto correttamente in {filename}")
    except Exception as e:
        print(f"Errore nella scrittura CSV: {e}")

# 2. LEGGERE CSV
def leggi_csv(filename):
    """Legge dati da file CSV"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            data = list(reader)
        print(f"CSV letto correttamente da {filename}")
        return data
    except FileNotFoundError:
        print(f"File {filename} non trovato")
        return None

# 3. LAVORARE CON DIZIONARI (DictReader/DictWriter)
def scrivi_csv_dict(data, filename):
    """Scrive CSV usando dizionari"""
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ["nome", "eta", "corso", "media"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()  # Scrive l'intestazione
            for row in data:
                writer.writerow(row)
        print(f"CSV con dizionari scritto in {filename}")
    except Exception as e:
        print(f"Errore: {e}")

def leggi_csv_dict(filename):
    """Legge CSV come dizionari"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        return data
    except FileNotFoundError:
        print(f"File {filename} non trovato")
        return None

# 4. ANALISI DATI CSV
def analizza_studenti_csv(filename):
    """Analizza i dati degli studenti dal CSV"""
    data = leggi_csv_dict(filename)
    if not data:
        return
    
    print("\n--- Analisi Studenti ---")
    medie = []
    corsi = {}
    
    for studente in data:
        nome = studente["nome"]
        eta = int(studente["eta"])
        corso = studente["corso"]
        media = float(studente["media"])
        
        medie.append(media)
        corsi[corso] = corsi.get(corso, 0) + 1
        
        print(f"{nome} ({eta} anni) - {corso} - Media: {media}")
    
    print(f"\nMedia generale: {sum(medie)/len(medie):.2f}")
    print("Distribuzione per corso:")
    for corso, count in corsi.items():
        print(f"  {corso}: {count} studenti")

# Esempi di utilizzo
if __name__ == "__main__":
    # Scrivere CSV normale
    scrivi_csv(studenti_csv, "studenti.csv")
    
    # Leggere CSV normale
    dati_csv = leggi_csv("studenti.csv")
    if dati_csv:
        print("\n--- Dati CSV ---")
        for row in dati_csv:
            print(row)
    
    # Preparare dati per CSV con dizionari
    studenti_dict = [
        {"nome": "Mario", "eta": 20, "corso": "Informatica", "media": 8.0},
        {"nome": "Lucia", "eta": 19, "corso": "Matematica", "media": 8.7},
        {"nome": "Giovanni", "eta": 21, "corso": "Fisica", "media": 7.0},
        {"nome": "Anna", "eta": 22, "corso": "Chimica", "media": 9.0}
    ]
    
    # Scrivere e leggere con dizionari
    scrivi_csv_dict(studenti_dict, "data_studenti.csv")
    analizza_studenti_csv("data_studenti.csv")

        
""" # Dati di esempio
studenti_data = {
    "studenti": [
        {
            "nome": "Mario",
            "eta": 20,
            "corso": "Informatica",
            "voti": [8, 9, 7, 10]
        },
        {
            "nome": "Lucia",
            "eta": 19,
            "corso": "Matematica",
            "voti": [9, 8, 9, 7]
        },
        {
            "nome": "Giovanni",
            "eta": 21,
            "corso": "Fisica",
            "voti": [7, 8, 6, 9]
        }
    ],
    "data_creazione": "2025-09-27",
    "totale_studenti": 3
}

# 1. SCRIVERE JSON SU FILE
def scrivi_json(data, filename):
   #Scrive i dati in formato JSON su file
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Dati scritti correttamente in {filename}")
    except Exception as e:
        print(f"Errore nella scrittura: {e}")

# 2. LEGGERE JSON DA FILE
def leggi_json(filename):
    #Legge i dati JSON da file
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"Dati letti correttamente da {filename}")
        return data
    except FileNotFoundError:
        print(f"File {filename} non trovato")
        return None
    except json.JSONDecodeError as e:
        print(f"Errore nel parsing JSON: {e}")
        return None

# 3. CONVERTIRE DA/A STRINGA JSON
def json_to_string_example():
    #Esempi di conversione JSON
    # Da oggetto Python a stringa JSON
    student = {"nome": "Anna", "eta": 22, "voti": [8, 9, 10]}
    json_string = json.dumps(student, indent=2)
    print("JSON come stringa:")
    print(json_string)
    
    # Da stringa JSON a oggetto Python
    parsed_data = json.loads(json_string)
    print("\nOggetto Python:")
    print(parsed_data)
    print(f"Nome: {parsed_data['nome']}")

# Esempi di utilizzo
if __name__ == "__main__":
    # Scrivere i dati
    scrivi_json(studenti_data, "studenti.json")
    
    # Leggere i dati
    dati_letti = leggi_json("studenti.json")
    if dati_letti:
        print("\n--- Studenti caricati ---")
        for studente in dati_letti["studenti"]:
            media = sum(studente["voti"]) / len(studente["voti"])
            print(f"{studente['nome']} - Corso: {studente['corso']} - Media: {media:.2f}")
    
    print("\n" + "="*50)
    json_to_string_example()
 """

