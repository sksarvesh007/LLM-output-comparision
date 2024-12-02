# Groq AI Boolean Information Extractor with Ground Truth Comparison

This project is a **Gradio-based web application** designed to compare the performance of two AI models in extracting boolean information from text with extreme precision. The application takes a context, a set of questions, and ground truth answers as input and evaluates the accuracy of the models.

---

## Features

- **Boolean Information Extraction:** Extracts "Yes" or "No" responses to questions based on a given context.
- **Model Comparison:** Compares the performance of two AI models (`llama-3.2-1b-preview` and `llama-3.1-70b-versatile`).
- **Accuracy Calculation:** Measures the accuracy of each model against the provided ground truth.
- **User-Friendly Interface:** Built using Gradio for ease of use.

---

## Installation

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:
    - Create a `.env` file in the project directory and add your Groq API key:
      ```
      GROQ_API_KEY=<your_groq_api_key>
      ```

---

## Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Open the application in your browser (default URL: `http://127.0.0.1:7860`).

3. Input the following:
    - **Context:** A passage of text for the models to analyze.
    - **Questions:** A list of questions (one per line).
    - **Ground Truth:** The expected answers (one "Yes" or "No" per line).

4. View the comparison results, including:
    - Responses from both models.
    - Accuracy of each model.

---

## How It Works

1. **Input Handling:**
    - The application takes user inputs (context, questions, and ground truth).
2. **Model Interaction:**
    - Two models (`llama-3.2-1b-preview` and `llama-3.1-70b-versatile`) are queried via the Groq API.
3. **Response Parsing:**
    - AI responses are strictly in JSON format (`{"answer": "Yes"}` or `{"answer": "No"}`).
4. **Accuracy Calculation:**
    - Compares model responses with the provided ground truth.
5. **Output Results:**
    - Displays the responses, ground truth, and model accuracies.

---

## Dependencies

- `gradio`
- `groq`
- `dotenv`
- `os`
- `json`

Install all dependencies using the provided `requirements.txt`.

---

## Example

Input:
- **Context:** A paragraph of information.
- **Questions:** 

