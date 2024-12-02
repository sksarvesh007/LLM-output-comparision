import gradio as gr
from groq import Groq
import os
import dotenv
import json

dotenv.load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
client = Groq()

def get_responses_and_compare(context, questions_text, ground_truth_text):
    questions = [q.strip() for q in questions_text.splitlines() if q.strip()]
    ground_truth = [gt.strip() for gt in ground_truth_text.splitlines() if gt.strip()]
    models = ["llama-3.2-1b-preview", "llama-3.1-70b-versatile"]
    
    response_1 = []
    response_2 = []
    
    for model_index, model_name in enumerate(models):
        for question in questions:
            completion = client.chat.completions.create(
                model=model_name,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an AI designed to extract boolean information from text with extreme precision. \n\nRules:\n1. Respond ONLY in JSON format\n2. Use exactly this structure: {\"answer\": \"Yes\"} or {\"answer\": \"No\"}\n3. Base your answer solely on the literal text of the paragraph\n4. Be strict - only respond Yes if the information is explicitly present\n5. If there's any doubt, respond with {\"answer\": \"No\"}. This is the knowledgebase which you are supposed to take into the context \n, if the answer of the question asked is not in the paragraph then return with No in json output as said else yes. This is the context : " + context
                    },
                    {
                        "role": "user",
                        "content": question
                    }
                ],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )

            response_content = ""
            for chunk in completion:
                response_content += chunk.choices[0].delta.content or ""

            try:
                answer = json.loads(response_content).get("answer", "")
                if model_index == 0:
                    response_1.append(answer)
                else:
                    response_2.append(answer)
            except json.JSONDecodeError as e:
                print(f"Error parsing response: {e}")

    accuracy_1 = sum(1 for r, g in zip(response_1, ground_truth) if r == g) / len(ground_truth)
    accuracy_2 = sum(1 for r, g in zip(response_2, ground_truth) if r == g) / len(ground_truth)
    
    comparison_result = f"""
Model 1 (llama-3.2-1b-preview):
Responses: {response_1}
Accuracy: {accuracy_1:.2%}

Model 2 (llama-3.1-70b-versatile):
Responses: {response_2}
Accuracy: {accuracy_2:.2%}

Ground Truth: {ground_truth}
"""
    
    return comparison_result

iface = gr.Interface(
    fn=get_responses_and_compare,
    inputs=[
        gr.Textbox(label="Context", lines=5, placeholder="Enter the context here..."),
        gr.Textbox(label="Questions (one per line)", lines=4, placeholder="Enter questions, one per line..."),
        gr.Textbox(label="Ground Truth (one Yes/No per line)", lines=4, placeholder="Enter ground truth answers, one per line...")
    ],
    outputs=gr.Textbox(label="Comparison Results"),
    title="Groq AI Boolean Information Extractor with Ground Truth Comparison",
    description="Enter the context, questions (one per line), and ground truth (one per line) to get boolean responses from the AI models and see their accuracy."
)

iface.launch()
