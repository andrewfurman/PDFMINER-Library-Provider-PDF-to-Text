import os
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

def pdf_to_text(pdf_path, txt_path):
    # Open the input PDF file in binary read mode
    with open(pdf_path, 'rb') as input_file:
        # Open the output text file
        with open(txt_path, 'w', encoding='utf-8') as output_file:
            # Extract text from PDF to the output file
            extract_text_to_fp(input_file, output_file, laparams=LAParams(
                line_margin=0.5,
                word_margin=0.1,
                char_margin=2.0,
                all_texts=True
            ))

# Set the paths for input PDF and output text file
current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_path = os.path.join(current_dir, 'input.pdf')
txt_path = os.path.join(current_dir, 'output.txt')

# Convert PDF to text
pdf_to_text(pdf_path, txt_path)

print(f"Conversion complete. Text saved to {txt_path}")