from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):
    """
    Translates English text to French using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    frenchText = translator.translate(englishText)
    return frenchText

def frenchToEnglish(frenchText):
    """
    Translates French text to English using MyMemoryTranslator.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    englishText = translator.translate(frenchText)
    return englishText