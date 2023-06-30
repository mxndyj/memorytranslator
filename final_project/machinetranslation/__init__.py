import unittest
from .translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        english_text = "Hello"
        expected_result = "Bonjour"
        translated_text = englishToFrench(english_text)
        self.assertEqual(translated_text, expected_result)

    def test_frenchToEnglish(self):
        french_text = "Bonjour"
        expected_result = "Hi"
        translated_text = frenchToEnglish(french_text)
        self.assertEqual(translated_text, expected_result)

    def test_englishToFrench_reverse(self):
        english_text = "Hello"
        expected_result = "Bonjour"
        translated_text = englishToFrench(english_text)
        self.assertEqual(translated_text, expected_result)

    def test_frenchToEnglish_reverse(self):
        french_text = "Pomme"
        expected_result = "Apple"
        translated_text = frenchToEnglish(french_text)
        self.assertEqual(translated_text, expected_result)

if __name__ == '__main__':
    unittest.main()
