import re
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def bionic_reading(text):
    words = text.split()
    emphasized_words = []
    for word in words:
        if len(word) > 3:
            emphasized_word = f"{word[0].upper()}{word[1:]}"
        else:
            emphasized_word = word
        emphasized_words.append(emphasized_word)
    return " ".join(emphasized_words)

# Function to save the provided text as a PDF
def save_as_pdf(text, output_file):
    # Create a new PDF canvas with the specified output file and page size
    c = canvas.Canvas(output_file, pagesize=letter)

    # Create a text object and set its position and font
    text_object = c.beginText()
    text_object.setTextOrigin(30, 750)
    text_object.setFont("Helvetica", 12)

    # Add each line from the input text to the text object
    for line in text.split('\n'):
        text_object.textLine(line)

    # Draw the text object on the canvas, finalize the page, and save the PDF
    c.drawText(text_object)
    c.showPage()
    c.save()

def main():
    file_path = input("Enter the file path: ")

    # Process a .txt file
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            bionic_content = bionic_reading(content)
            save_as_pdf(bionic_content, 'bionic_output.pdf')

    # Process a .docx file
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        bionic_content = ""

        # Convert each paragraph in the .docx file to Bionic Reading format
        for paragraph in doc.paragraphs:
            bionic_paragraph = bionic_reading(paragraph.text)
            bionic_content += bionic_paragraph + "\n"

        # Save the Bionic Reading content as a PDF
        save_as_pdf(bionic_content, 'bionic_output.pdf')

    # Handle unsupported file formats
    else:
        print("Unsupported file format. Please provide a .txt or .docx file.")

if __name__ == "__main__":
    main()
