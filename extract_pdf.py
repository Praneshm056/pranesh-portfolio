from pypdf import PdfReader

reader = PdfReader("Pranesh_M_Emertxe_resume-1.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

with open("resume_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Text extracted successfully.")
