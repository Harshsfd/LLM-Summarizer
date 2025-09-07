from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from utils import summarize_large_text

# Model name
model_name = "facebook/bart-large-cnn"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Create summarization pipeline
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

def summarize_text(text):
    """
    Summarizes input text using local LLM.
    """
    summary = summarizer(
        text,
        max_length=60,
        min_length=20,
        do_sample=False
    )
    return summary[0]['summary_text']

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        text = f.read()

    summary = summarize_large_text(text, summarize_text)
    print("=== Original Text ===")
    print(text[:500] + "..." if len(text) > 500 else text)  # Show first 500 chars only
    print("\n=== Summary ===")
    print(summary)
