from pdf_reader import extract_text_from_pdf
from relationship_extractor import extract_relationships
from graph import create_graph

pdf_path = "uploads/python_notes.pdf"

print("📄 Reading PDF...")

text = extract_text_from_pdf(pdf_path)

print("✅ Text extracted.")

print("🧠 Finding relationships...")

relationships = extract_relationships(text)

print(f"✅ Found {len(relationships)} relationships.")

print("🗺️ Creating Memory Map...")

create_graph(relationships)

print("🎉 Project Completed!")