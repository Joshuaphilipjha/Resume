from flask import Flask, render_template, request
from tika import parser

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    extracted_text = None  # Initialize extracted_text

    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename != "":
            file_path = "uploads/" + uploaded_file.filename
            uploaded_file.save(file_path)
            extracted_text = extract_text_from_pdf(file_path)

    return render_template("upload.html", text=extracted_text)

def extract_text_from_pdf(file_path):
    try:
        parsed_pdf = parser.from_file(file_path)
        text = parsed_pdf["content"]
        return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return "Text extraction failed."

if __name__ == "__main__":
    app.run(debug=True)
