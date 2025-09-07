# 📝 LLM Text Summarizer

This project is a simple **Text Summarization Tool** built with Python and Hugging Face Transformers.  
It uses the **facebook/bart-large-cnn** model to generate concise summaries of long text.

---

## 🚀 Features
- Summarizes long paragraphs into short, meaningful text  
- Runs locally (with Hugging Face model)  
- Easy to use with Python script  
- Extendable for custom text files or user input  

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/harshsfd/LLM-Summarizer.git
   cd LLM-Summarizer

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


3. Install dependencies:
```bash
pip install --upgrade pip
pip install torch transformers sentencepiece


4. Run the script:
```bash
python3 summarizer.py




---

🧑‍💻 Usage

By default, the script summarizes a hardcoded text.

To summarize your own text, replace the text variable in summarizer.py, or load from input.txt:

with open("input.txt", "r") as f:
    text = f.read()


---

📌 Example Output

Input:

Large language models (LLMs) are a type of artificial intelligence system
that can generate and understand human-like text. They are trained on vast
amounts of data and can perform tasks like translation, summarization,
and question answering.

Summary:

Large language models (LLMs) are AI systems trained on vast data that can
understand text and perform tasks like translation and summarization.


---

🛠️ Tech Stack

Python 3

Hugging Face Transformers

PyTorch



---

📄 License

This project is licensed under the MIT License.

---
