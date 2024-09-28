import gradio as gr
import os
from dotenv import load_dotenv
from openai_work.generate import save_file_to_openai, generate_answer_from_file
from openai import OpenAI
import css

load_dotenv()
client = OpenAI()

def generate_answer_from_vector(question, vector_id):
    try:
        thread = client.beta.threads.create()
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )
        
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=os.getenv("ASSISTANCE_ID"),
            instructions=f"Use the vector store with ID {vector_id} to answer the question."
        )

        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            
        messages = list(client.beta.threads.messages.list(thread_id=thread.id))
        
        message_content = messages[0].content[0].text
        annotations = message_content.annotations
        citations = []
        
        for index, annotation in enumerate(annotations):
            message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
            if file_citation := getattr(annotation, "file_citation", None):
                cited_file = client.files.retrieve(file_citation.file_id)
                citations.append(f"[{index}] {cited_file.filename}")
        
        answer = message_content.value + "\n\n" + "\n".join(citations)
        yield answer
    except Exception as e:
        yield f"An error occurred: {str(e)}"

def upload_and_ask(file, question):
    if file is None:
        yield from generate_answer_from_vector(question, os.getenv("VECTOR_ID"))
    else:
        uploaded_file = save_file_to_openai(file.name)
        if uploaded_file:
            client.files.create(
                file=open(file.name, "rb"),
                purpose="assistants"
            )
            yield from generate_answer_from_vector(question, os.getenv("VECTOR_ID"))
        else:
            yield "Failed to upload the file. Please try again."

def add_message(history, file, question):
    if file:
        history.append(((file.name,), None))
    if question:
        history.append((question, None))
    return history

def bot(history, file, question):
    response = ""
    for chunk in upload_and_ask(file, question):
        response += chunk
        history[-1][1] = response
        yield history

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    with gr.Row():
        with gr.Column(scale=1):  # Sidebar column
            with gr.Tab("Document Review"):
                gr.Markdown("## Document Review")
                file_input = gr.File(
                    label="Upload Document",
                    file_types=[".txt", ".pdf", ".docx"],
                    elem_classes=["file-upload-btn"]
                )
                review_notes = gr.Textbox(
                    label="Review Notes",
                    placeholder="Add your review notes here...",
                    lines=5
                )

        with gr.Column(scale=3):  # Main content column
            gr.Markdown("# AI File Assistant")
            gr.Markdown("Upload a file and ask questions about its content, or ask questions directly.")
            
            chatbot = gr.Chatbot(
                elem_id="chatbot",
                bubble_full_width=False,
                height=300,
                container=True
            )

            with gr.Row(elem_classes=["input-row"]):
                with gr.Column(scale=3):
                    question_input = gr.Textbox(
                        show_label=False,
                        placeholder="Type your question here...",
                        lines=1,
                        elem_id="question-input",
                    )
                with gr.Column(scale=1):
                    submit_btn = gr.Button("Ask", variant="primary", elem_classes=["submit-btn"])
                
                    
    # Event handlers
    submit_btn.click(
        add_message,
        [chatbot, file_input, question_input],
        [chatbot]
    ).then(
        bot,
        [chatbot, file_input, question_input],
        [chatbot]
    )

# Launch the app
demo.launch()