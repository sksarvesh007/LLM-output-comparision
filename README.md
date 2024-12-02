Groq AI Boolean Information Extractor
A sophisticated web application that leverages Groq's LLM models to perform boolean information extraction from text, featuring real-time accuracy comparison and ground truth validation.
Overview
This application serves as a powerful tool for:
Evaluating LLM performance in boolean information extraction
Comparing different Groq model versions
Validating AI responses against ground truth
Analyzing model accuracy in real-time
The system currently implements two Groq models:
llama-3.2-1b-preview (faster, lighter model)
llama-3.1-70b-versatile (more powerful, comprehensive model)
Features
Advanced LLM Integration: Direct integration with Groq's state-of-the-art language models
Real-time Processing: Stream-based response processing for immediate feedback
Structured Output: JSON-formatted responses ensuring consistency and reliability
Accuracy Metrics: Automatic calculation of model performance against ground truth
User-friendly Interface: Clean, intuitive Gradio web interface
Multi-question Support: Process multiple questions simultaneously
Comparative Analysis: Side-by-side model performance comparison
Prerequisites
Python 3.8 or higher
Active Groq API account and key
Internet connection for API access
Required Dependencies
Environment Setup
Clone the repository:
Create and configure your environment file:
Usage Guide
Start the application:
Navigate to the web interface (default: http://localhost:7860)
Input your data:
Context: Paste your reference text
Questions: Enter your Yes/No questions (one per line)
Ground Truth: Provide correct answers (Yes/No format)
Example inputs:
Output Interpretation
The system provides detailed output including:
Performance Considerations
llama-3.2-1b-preview:
Faster response time
Suitable for simple queries
Lower resource consumption
llama-3.1-70b-versatile:
More nuanced understanding
Better for complex contexts
Higher accuracy on ambiguous questions
Error Handling
The application includes robust error handling for:
Invalid JSON responses
API connection issues
Mismatched input formats
Ground truth validation
