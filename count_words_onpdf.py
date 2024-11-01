# Count how many times each word apears on a pdf and export the results in an excel file
import PyPDF2
import re
from collections import Counter
import pandas as pd
import spacy

# Load the Greek language model for POS tagging
nlp = spacy.load("el_core_news_sm")

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

# Function to clean and tokenize text
def clean_and_tokenize(text):
    # Remove non-alphabetic characters and tokenize by splitting on whitespace
    words = re.findall(r'\b\w+\b', text.lower())
    return words

# Function to count words
def count_words(word_list):
    return Counter(word_list)

# Function to get POS tags using spaCy
def get_pos_tags(words):
    pos_tags = []
    doc = nlp(" ".join(words))  # Process the entire text
    for token in doc:
        pos_tags.append((token.text, token.pos_))  # Get the word and its POS
    return pos_tags

# Function to export word counts and POS tags to Excel
def export_to_excel(word_counts, pos_tags, output_file):
    # Convert word counts to a pandas DataFrame
    df_word_counts = pd.DataFrame(word_counts.items(), columns=['Word', 'Frequency'])
    
    # Create a DataFrame for POS tags
    df_pos_tags = pd.DataFrame(pos_tags, columns=['Word', 'POS'])
    
    # Merge the two DataFrames on the 'Word' column
    df = pd.merge(df_word_counts, df_pos_tags, on='Word', how='left')

    # Save DataFrame to Excel file
    df.to_excel(output_file, index=False)
    print(f"Word counts and POS tags successfully exported to {output_file}")

# Main function
def main(pdf_path, output_file):
    # Step 1: Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)

    # Step 2: Clean and tokenize the text
    words = clean_and_tokenize(text)

    # Step 3: Count the words
    word_counts = count_words(words)

    # Step 4: Get POS tags
    pos_tags = get_pos_tags(words)

    # Step 5: Export the results to an Excel file
    export_to_excel(word_counts, pos_tags, output_file)

if __name__ == "__main__":
    # Specify the path to your PDF file and the output Excel file
    pdf_path = r'C:/Users/marie/Desktop/best_hex.pdf'
    output_file = r'C:/Users/marie/Desktop/best_hex_word_counts_v2.xlsx'

    main(pdf_path, output_file)
