import MLrecognition
from ExtractTextFromImg import image_to_text
from textscanner import textscanner
from Translator import Translate


def main():
    textscanner()
    TextExtracted = image_to_text('ImageWithText.jpg')
    MLrecognition.prediction(TextExtracted)
    Translate(TextExtracted)


if __name__ == "__main__":
    main()
