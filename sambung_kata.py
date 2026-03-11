import os
import urllib.request
import random
from dotenv import load_dotenv

load_dotenv()

DICT_URL = os.environ.get("ID_DICT_URL")
if not DICT_URL:
    print("Error: ID_DICT_URL environment variable is not set. Please set it in your .env file.")
    exit(1)

DICT_FILE = "kbbi.txt"

def load_dictionary():
    if not os.path.exists(DICT_FILE):
        print(f"Mengunduh kamus dari {DICT_URL}...")
        try:
            urllib.request.urlretrieve(DICT_URL, DICT_FILE)
            print("Kamus berhasil diunduh!")
        except Exception as e:
            print(f"Gagal mengunduh kamus: {e}")
            return list()
            
    try:
        with open(DICT_FILE, 'r', encoding='utf-8') as f:
            words = list(set(line.strip().lower() for line in f if line.strip() and ' ' not in line and '-' not in line))
            words.sort()
        return words
    except Exception as e:
        print(f"Gagal membaca kamus: {e}")
        return list()

def main():
    print("="*40)
    print("=== SAMBUNG KATA HELPER ===")
    print("="*40)
    print("Ketik huruf/suku kata untuk mencari kata yang BERAWALAN atau BERAKHIRAN dengan teks tersebut.")
    print("Ketik 'exit' untuk keluar.")
    print("="*40)
    print()
    
    words = load_dictionary()
    if not words:
        print("Kamus tidak tersedia. Keluar...")
        return
        
    print(f"Berhasil memuat {len(words)} kata ke kamus.\n")

    while True:
        query = input("\nMasukkan huruf/suku kata: ").strip().lower()
        
        if query == 'exit':
            print("Terima kasih telah menggunakan helper ini!")
            break
            
        if not query:
            continue
            
        starts_with = [w for w in words if w.startswith(query)]
        ends_with = [w for w in words if w.endswith(query)]
        contains = [w for w in words if query in w and not w.startswith(query) and not w.endswith(query)]
        
        print("\n" + "-"*40)
        
        print(f"Menemukan {len(starts_with)} kata yang BERAWALAN '{query.upper()}':")
        if starts_with:
            formatted_starts = []

            def get_game_rule(word):
                vowels = "aiueo"
                for i in range(len(word)-1, -1, -1):
                    if word[i] in vowels:
                        return word[i:]
                return word[-1] 
                
            for w in starts_with:
                predictions = []
                game_rule_part = get_game_rule(w)

                candidates = []
                if game_rule_part not in candidates: candidates.append(game_rule_part)
                for length in [3, 2, 1]:
                    if len(w) >= length and w[-length:] not in candidates:
                        candidates.append(w[-length:])
                        
                for part in candidates:
                    possible_answers = [x for x in words if x.startswith(part)]
                    if possible_answers:
                        sample_answers = random.sample(possible_answers, min(len(possible_answers), 3))
                        label = f"*{part.upper()}*" if part == game_rule_part else f"'{part.upper()}'"
                        predictions.append(f"{label} -> {', '.join(sample_answers)}")
                
                if predictions:
                    formatted_starts.append(f"{w} (Lanjut: {'; '.join(predictions)})")
                else:
                    formatted_starts.append(w)
                
            print("\n".join(formatted_starts))
        else:
            print("-")
            
        print()
        
        print(f"Menemukan {len(ends_with)} kata yang BERAKHIRAN '{query.upper()}':")
        if ends_with:
            sample = random.sample(ends_with, min(len(ends_with), 20))
            sample.sort()
            print(", ".join(sample))
            if len(ends_with) > 20:
                print("... (masih ada lagi)")
        else:
            print("-")

        print("-" * 40)

if __name__ == "__main__":
    main()
