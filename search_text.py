import os

# Katalog z plikami tekstowymi
search_directory = 'matura_pdfs'

# Funkcja do przeszukiwania plików tekstowych pod kątem określonej frazy
def search_text_in_files(directory, search_phrase):
    results = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line_number, line in enumerate(lines, start=1):
                        if search_phrase.lower() in line.lower():
                            results.append((file, line_number, line.strip()))
    
    return results

# Przykład użycia funkcji
search_phrase = 'binarn'
results = search_text_in_files(search_directory, search_phrase)

# Wyświetlanie wyników
for result in results:
    print(f"Plik: {result[0]}, Linia: {result[1]}, Tekst: {result[2]}")

