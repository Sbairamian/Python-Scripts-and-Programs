import os
from pypdf import PdfWriter, PdfReader

pdf_directory = r"C:\Users\SevBairamian\Desktop\CMMC Evidence\3.1.x - Access Controls\3.1.19"
output_pdf = r"C:\Users\SevBairamian\Desktop\CMMC Evidence\3.1.x - Access Controls\3.1.19\3.1.19 - Intune - No Mobile"

print("=== PATH CHECK ===")
print("Input folder exists:", os.path.exists(pdf_directory))
print("Output folder exists:", os.path.exists(os.path.dirname(output_pdf)))
print("Output path:", output_pdf)

print("\n=== LISTING FILES IN INPUT FOLDER ===")
try:
    files = os.listdir(pdf_directory)
    for f in files:
        print("FOUND:", f)
except Exception as e:
    print("ERROR listing directory:", e)

pdf_files = [
    os.path.join(pdf_directory, f)
    for f in os.listdir(pdf_directory)
    if f.lower().endswith(".pdf")
]

print("\nPDF files detected:", len(pdf_files))
for f in pdf_files:
    print("PDF:", f)

if not pdf_files:
    print("❌ No PDFs found. Nothing to merge.")
    exit()

writer = PdfWriter()

print("\n=== READING PDFs ===")
for pdf in pdf_files:
    try:
        reader = PdfReader(pdf)
        print(f"Loaded {pdf} with {len(reader.pages)} pages")
        for page in reader.pages:
            writer.add_page(page)
    except Exception as e:
        print(f"❌ ERROR reading {pdf}:", e)

print("\n=== WRITING OUTPUT ===")
try:
    os.makedirs(os.path.dirname(output_pdf), exist_ok=True)

    with open(output_pdf, "wb") as f:
        writer.write(f)

    print("File exists after write:", os.path.exists(output_pdf))
    print("Saved at:", os.path.abspath(output_pdf))

except Exception as e:
    print("❌ ERROR writing output:", e)