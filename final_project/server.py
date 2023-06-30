from flask import Flask, render_template, request
from deep_translator import MyMemoryTranslator

app = Flask(__name__)

API_KEY='d5e7bc5b47e8e1e5bfc2'


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translate_english_to_french(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translate_french_to_english(textToTranslate)
    return translated_text

def translate_english_to_french(english_text):
    """
    Translates English text to French using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='en-US', target='fr-FR', api_key=API_KEY)
    french_text = translator.translate(english_text)
    return french_text

def translate_french_to_english(french_text):
    """
    Translates French text to English using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-US', api_key=API_KEY)
    english_text = translator.translate(french_text)
    return english_text

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)