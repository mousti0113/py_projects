import argparse 
import csv
import json

class Studente:
    def __init__(self, matricola, nome, conoscenze, classe, anno_di_nascita):
        self.matricola = matricola
        self.nome = nome
        self.conoscenze = conoscenze
        self.classe = classe
        self.anno_di_nascita = anno_di_nascita
    
    def to_dict(self):
        return {
            "matricola": self.matricola,
            "nome": self.nome,
            "conoscenze": self.conoscenze,
            "classe": self.classe,
            "anno_di_nascita": self.anno_di_nascita
        }

def leggi_da_file_csv(filename, separatore):
    try:
        with open(filename, "r", encoding="UTF-8") as file:
            reader = csv.reader(file, delimiter=separatore)
            data = list(reader)
            
            # Processa le conoscenze (skip header)
            for i in range(1, len(data)):
                if len(data[i]) >= 3:  # Validazione riga
                    conoscenze_string = data[i][2]
                    conoscenze = [k.strip() for k in conoscenze_string.split(",")]
                    data[i][2] = conoscenze
        
        return data
    except FileNotFoundError:
        print(f"Errore: File {filename} non trovato")
        return None
    except Exception as e:
        print(f"Errore nella lettura CSV: {e}")
        return None

def write_in_json_file(data, filename):
    try:
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"File JSON creato con successo: {filename}")
    except Exception as e:
        print(f"Errore nella scrittura JSON: {e}")

def crea_studenti_da_csv(data_csv):
    """Crea oggetti Studente dai dati CSV"""
    studenti = []
    
    if not data_csv or len(data_csv) <= 1:
        print("Nessun dato studente trovato")
        return studenti
    
    # Skip header (prima riga)
    for riga in data_csv[1:]:
        try:
            if len(riga) >= 5:  # Validazione colonne
                studente = Studente(
                    matricola=int(riga[0]),
                    nome=riga[1],
                    conoscenze=riga[2],  # Già processate in leggi_csv
                    classe=riga[3],
                    anno_di_nascita=int(riga[4])
                )
                studenti.append(studente)
            else:
                print(f"Riga incompleta ignorata: {riga}")
        except ValueError as e:
            print(f"Errore conversione dati in riga {riga}: {e}")
        except Exception as e:
            print(f"Errore generico nella riga {riga}: {e}")
    
    return studenti

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script per convertire CSV in JSON per studenti.")
    parser.add_argument("file_in_CSV", help="Percorso del file CSV di input")
    parser.add_argument("separatore_CSV", help="Separatore usato nel CSV (es. ',')")
    parser.add_argument("file_out_JSON", help="Percorso del file JSON di output")
    
    args = parser.parse_args()
    
    # Lettura CSV
    data_studenti = leggi_da_file_csv(args.file_in_CSV, args.separatore_CSV)
    
    if data_studenti is None:
        print("Impossibile leggere il file CSV. Terminazione.")
        exit(1)
    
    # Creazione oggetti Studente
    studenti = crea_studenti_da_csv(data_studenti)
    
    if not studenti:
        print("Nessuno studente valido trovato. Terminazione.")
        exit(1)
    
    # Conversione in dizionari e creazione JSON
    studenti_dict = [studente.to_dict() for studente in studenti]
    
    studenti_data = {
        "studenti": studenti_dict,
        "totale_studenti": len(studenti_dict),
        "file_origine": args.file_in_CSV
    }
    # Crea il file .json
    with open(args.file_out_JSON,"w",encoding="UTF-8") as file:
        pass
    # Scrittura JSON
    write_in_json_file(studenti_data, args.file_out_JSON)
    
    print(f"Elaborati {len(studenti)} studenti con successo!")

