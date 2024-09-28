from openai import OpenAI
import os
from dotenv import load_dotenv
import time

load_dotenv()
client = OpenAI()

def save_file_to_openai(file_path):
    """
    Save a file to OpenAI's file storage.
    
    :param file_path: Path to the file to be uploaded
    :return: The file object returned by OpenAI
    """
    # try:
    file_streams = [open(path, "rb") for path in [file_path]]
    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
    vector_store_id=os.environ["VECTOR_ID"], files=file_streams
    )

    print(f"File uploaded successfully. File ID: {file_batch.id}")
    return file_batch
    # except Exception as e:
    #     print(f"An error occurred while uploading the file: {str(file_batch)}")
    #     return None

def generate_answer_from_file(message, file_id, assistant_id, vector_id):
    """
    Generate an answer from a file using OpenAI's Assistant API.
    
    :param message: The user's message or query
    :param file_id: The ID of the file to use for generating the answer
    :param assistant_id: The ID of the assistant to use
    :param vector_id: The ID of the vector store to use
    :return: The generated answer
    """
    try:
        # Create a thread
        thread = client.beta.threads.create()

        # Add a message to the thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=message
        )

        # Attach the file to the thread
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content="",
            file_ids=[file_id]
        )

        # Run the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant_id,
            instructions=f"Please answer the query based on the information in the attached file. Use the vector store with ID {vector_id} if needed."
        )

        # Wait for the run to complete
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            time.sleep(1)

        # Retrieve the assistant's response
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        
        # Get the last message from the assistant
        for message in messages.data:
            if message.role == "assistant":
                return message.content[0].text.value

        return "No response generated."
    except Exception as e:
        print(f"An error occurred while generating the answer: {str(e)}")
        return None

# Example usage:
# file_path = "path/to/your/file.pdf"
# uploaded_file = save_file_to_openai(file_path)
# if uploaded_file:
#     answer = generate_answer_from_file(
#         "What does this file contain?",
#         uploaded_file.id,
#         os.getenv("ASSISTANCE_ID"),
#         os.getenv("VECTOR_ID")
#     )
#     print(answer)
