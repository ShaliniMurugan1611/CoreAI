from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

model = genai.GenerativeModel("models/gemini-1.0-pro")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate-text", methods=["POST"])
def generate_text():
    try:
        data = request.get_json()
        prompt = data.get("prompt")

        response = model.generate_content(prompt)

        return jsonify({
            "result": response.text
        })

    except Exception as e:
        return jsonify({
            "result": f"Error: {str(e)}"
        })


if __name__ == "__main__":
    app.run(debug=True)