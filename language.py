from transformers import pipeline, MarianMTModel, MarianTokenizer
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Language code map for translation (you can expand this as needed)
language_code_map = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "nl": "Dutch",
    "ru": "Russian",
    "zh": "Chinese",
    "ar": "Arabic",
    "hi": "Hindi",
    "ja": "Japanese",
    "ko": "Korean",
    "tr": "Turkish"
}

# Step 1: Language Detection
def detect_language(text):
    try:
        detector = pipeline("text-classification", model="papluca/xlm-roberta-base-language-detection")
        result = detector(text)
        language = result[0]['label']
        confidence = result[0]['score']
        print(f"Detected language: {language} (confidence: {confidence:.2f})")
        return language
    except Exception as e:
        print(f"Error in language detection: {e}")
        return "en"

# Step 2: Translation
def translate_text(text, target_language="en"):
    source_language = detect_language(text)

    if source_language not in language_code_map or target_language not in language_code_map:
        raise ValueError(f"Unsupported language code(s). Supported languages are: {list(language_code_map.keys())}")

    model_name = f"Helsinki-NLP/opus-mt-{source_language}-{target_language}"
    try:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
    except Exception as e:
        raise RuntimeError(f"Failed to load model '{model_name}'. Error: {e}")

    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
    translated = model.generate(**inputs)
    translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
    return translated_text

# Step 3: Equation extraction
def extract_equations(text):
    return re.findall(r'\b[A-Za-z]+\s*=\s*[A-Za-z0-9^+/*\-()]+\b', text)

# Step 4: Hybrid Summarization
def extractive_summary(text, sentences_count=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join(str(sentence) for sentence in summary)

def abstractive_summary(text):
    try:
        summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
        summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Abstractive summarization failed: {e}")
        return extractive_summary(text)  # fallback

def hybrid_summarization(text):
    extractive = extractive_summary(text)
    return abstractive_summary(extractive)

# Main function
def main():
    print("Available languages:")
    for code, name in language_code_map.items():
        print(f"{code} - {name}")

    input_text = input("\nEnter the text you want to summarize: ")
    target_language = input("Enter the *target* language for translation (from the codes above, e.g., 'en'): ").strip()

    try:
        print("\nDetecting language...")
        source_language = detect_language(input_text)

        print("\nTranslating text...")
        translated_text = translate_text(input_text, target_language=target_language)
        print(f"\nTranslated Text: {translated_text}")

        print("\nExtracting mathematical/scientific content...")
        equations = extract_equations(translated_text)
        print(f"Mathematical expressions found: {equations}")

        print("\nSummarizing...")
        summary = hybrid_summarization(translated_text)
        print(f"\nFinal Summary:\n{summary}")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure your environment supports PyTorch or TensorFlow if you're running on a local machine.")

if __name__ == "__main__":
    main()
