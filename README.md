# Rag-template

This template demonstrates a FastAPI server with **Retrieval-Augmented Generation (RAG)**. 
It uses **LlamaIndex** for efficient retrieval of relevant documents, enabling the generation of accurate and context-aware responses based on indexed data using the **OpenAI API**.

## Features

- **Query Endpoint**: Accepts a user query, retrieves relevant information from the LlamaIndex, and generates a GPT-based response.
- **Rebuild Index**: Allows rebuilding the document index to reflect updated data.
- **LlamaIndex Integration**: Uses `llama_index` for efficient document storage and retrieval.
- **GPT Response Generation**: Leverages OpenAI's GPT API to generate contextually relevant answers.

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
   
2. **Install dependencies**: Ensure you have Python 3.8+ and `pip` installed, then run:
    ```bash
   pip install -r requirements.txt
    ```

3. **Set up OpenAI API key**: Add your OpenAI API key to the environment variable `OPENAI_API_KEY`. This can be done by adding the following line to your `.bashrc`, `.zshrc`, or creating a `.env` file:
    ```bash
   export OPENAI_API_KEY="your_openai_api_key"
   ```

## Usage

### Start the Server

Run the FastAPI app with uvicorn:

```bash
uvicorn src.app:app --reload
```
The server will be available at `http://127.0.0.1:8000`.

