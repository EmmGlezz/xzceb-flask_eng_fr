import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def testNull(self):
        self.assertEqual(english_to_french(None), None)


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def testNull(self):
        self.assertEqual(french_to_english(None), None)


if __name__ == "__main__":
    unittest.main()
