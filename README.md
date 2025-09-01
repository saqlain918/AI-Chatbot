## Local AI Chatbot with Ollama + Streamlit

A local AI chatbot built using Ollama for running AI models locally, Streamlit for the interactive frontend, and Python for backend logic. Chat with AI models completely offline with a modern, user-friendly interface.

## What it does

- Runs AI models locally using Ollama without internet dependency
- Provides interactive chat interface with real-time streaming responses
- Supports multiple AI models with easy selection dropdown
- Maintains chat history during sessions
- Offers modern chat bubble styling with distinct user/assistant colors
- Includes chat management features like clear history

## Features

- Local AI Model Execution: Run models with Ollama locally
- Model Selection: Choose from llama2, mistral, or custom models
- Chat History: Persistent conversation history during sessions
- Streaming Responses: Messages appear while being generated
- Modern UI: Chat bubble styling with different colors for user vs assistant
- Chat Management: Clear chat button with modern styling
- Real-time Interaction: Instant responses without external API calls

## Installation

1. Clone or download this repository

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install and setup Ollama:
   Visit https://ollama.ai and follow installation instructions

## How to use

1. Start Ollama in the background:
   ```
   ollama serve
   ```

2. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

3. Open the app in your browser (usually http://localhost:8501)

4. Usage steps:
   - Select a model (llama2, mistral, or custom) from dropdown
   - Type your message in the chat input box
   - Watch assistant stream response in real-time
   - Use "Clear Chat" button to reset conversation history

## Project Structure

```
chatbot/
├── app.py            # Main Streamlit app
├── requirements.txt  # Python dependencies
└── README.txt        # Project guide
```

## Example Usage

**Model Selection:**
Choose from available models like llama2 or mistral

**Chat Interaction:**
- User: "Explain quantum computing in simple terms"
- Assistant: [Streams response in real-time with chat bubble styling]

**Chat Management:**
Use Clear Chat button to start fresh conversations

## Dependencies

- streamlit
- ollama (Python SDK)

## Requirements

- Python 3.10+
- Ollama installed locally
- Sufficient RAM for model execution
- Local storage for AI models

## Customization

**Model Options:**
- Update `model_options` in app.py to add/remove models
- Support for custom Ollama models

**UI Styling:**
- Adjust chat bubble colors in CSS section
- Modify Clear Chat button styles for your theme
- Customize overall app appearance

**Features:**
- Add new functionality to the chat interface
- Integrate additional Ollama capabilities


## Use Cases

- Local AI experimentation and development
- Privacy-focused AI interactions
- Offline AI assistance and support
- Educational AI demonstrations
- Personal AI assistant setup
- Development and testing of AI applications

## Next Steps / Enhancements

- Add support for saving chat history to files
- Allow uploading documents for context
- Improve UI with themes, icons, and animations
- Multi-user session handling
- Integration with additional AI models
- Advanced chat features and customization

## Built with

- Python
- Streamlit
- Ollama
- Local AI infrastructure

## Notes

- Completely local setup ensures data privacy
- No internet required after initial model download
- Streaming responses provide smooth user experience
- Extensible architecture for additional features
- Modern chat interface with professional styling
