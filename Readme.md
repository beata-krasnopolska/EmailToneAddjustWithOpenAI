# SimpleUIStreamlit

A lightweight Streamlit application that uses LangChain and OpenAI to help users
improve their emails by rewriting them with different tones and English
dialects. Users provide an email body, select a tone (Formal, Informal,
Friendly, or Professional) and dialect (American, British, or Australian
English), and the app returns a polished version of the text.

## Features

- Prompt templating with `langchain_core`.
- Chat model integration via `langchain_openai` (GPT-3.5-Turbo).
- Environment configuration using `python-dotenv`.
- Interactive UI built with Streamlit.

## Usage

1. Set up an OpenAI API key in a `.env` file.
2. Activate the virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run the app:

   ```bash
   streamlit run main.py
   ```

## License

MIT

