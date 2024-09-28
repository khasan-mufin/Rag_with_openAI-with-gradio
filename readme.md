# AI File Assistant

AI File Assistant is a Gradio-based web application that allows users to upload documents, ask questions about their content, and receive AI-generated answers. It also includes a document review feature for tracking the status of uploaded documents.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)

## Features

- File Upload: Support for uploading .txt, .pdf, and .docx files
- AI-Powered Q&A: Ask questions about uploaded documents and receive AI-generated answers
- Document Review: Track the review status of uploaded documents and add review notes
- User-Friendly Interface: Clean and intuitive Gradio-based UI for easy interaction

## Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Required Python packages (see `requirements.txt`)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-file-assistant.git
   cd ai-file-assistant
   ```

2. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project root directory
   - Add your OpenAI API key and other necessary variables:
     ```
     OPENAI_API_KEY=your_api_key_here
     ASSISTANCE_ID=your_assistant_id_here
     VECTOR_ID=your_vector_id_here
     ```

## Usage

1. Run the application:
   ```sh
   python gradio_app
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (usually `http://127.0.0.1:7860`).

3. Use the interface to:
   - Upload documents
   - Ask questions about the documents
   - Review document status and add notes

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI API for document processing and question answering
- Gradio library for building the user interface

## Contact

For questions or feedback, please open an issue on the GitHub repository.
