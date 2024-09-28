custom_css = """
body {
    background-color: #f9fafc;
    color: #343a40;
    font-family: 'Helvetica Neue', sans-serif;
}
.gradio-container {
    max-width: 960px;
    margin: 0 auto;
    padding: 30px;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}
.chatbot {
    background-color: #ffffff;
    border: 1px solid #e9ecef;
    border-radius: 12px;
    overflow: hidden;
    padding: 15px;
}
.message {
    padding: 14px 20px;
    margin: 10px 0;
    border-radius: 20px;
    max-width: 75%;
}
.user-message {
    background-color: #007bff;
    color: white;
    align-self: flex-end;
    border-top-right-radius: 0;
}
.bot-message {
    background-color: #f8f9fa;
    color: #343a40;
    align-self: flex-start;
    border-top-left-radius: 0;
}
.submit-btn {
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border-radius: 30px;
    font-size: 16px;
}
.submit-btn:hover {
    background-color: #0056b3;
}
.input-row {
    display: flex;
    align-items: center;
    margin-top: 20px;
}

.hidden-file-input {
    display: none;
}

"""