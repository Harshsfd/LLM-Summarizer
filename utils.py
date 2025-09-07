def chunk_text(text, max_words=800):
    """
    Splits large text into smaller chunks of words.
    """
    words = text.split()
    for i in range(0, len(words), max_words):
        yield " ".join(words[i:i+max_words])

def summarize_large_text(text, summarize_func):
    """
    Handles large text by breaking into chunks and summarizing.
    """
    chunks = list(chunk_text(text))
    summaries = [summarize_func(chunk) for chunk in chunks]

    if len(summaries) == 1:
        return summaries[0]
    
    # Summarize combined summaries into a final summary
    final_summary = summarize_func(" ".join(summaries))
    return final_summary
