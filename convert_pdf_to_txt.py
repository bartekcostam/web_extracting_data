import fitz  # PyMuPDF
import os

# Katalog główny z maturami
main_download_dir = 'matura_pdfs'

# Funkcja do wyodrębniania tekstu z plików PDF
def extract_text_from_pdfs(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                doc = fitz.open(pdf_path)
                
                text = ""
                for page in doc:
                    text += page.get_text()
                
                # Zapisywanie wyodrębnionego tekstu do pliku
                text_filename = pdf_path.replace('.pdf', '.txt')
                with open(text_filename, 'w', encoding='utf-8') as text_file:
                    text_file.write(text)

                print(f'Przetworzono: {pdf_path}')

extract_text_from_pdfs(main_download_dir)
