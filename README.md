# Speech-to-Text with LLM Response and Text-to-Speech

This project converts audio input to text using Whisper, generates a response using a Large Language Model (LLM) via Cohere API, and converts the response back to speech using a Text-to-Speech (TTS) engine.

## Features

- Audio to text transcription with Whisper (OpenAI)
- Response generation using Cohere's LLM API
- Text-to-Speech output for the generated response
- Secure API key management using `.env` file

## Prerequisites

- Python 3.8 or higher
- `ffmpeg` installed and added to your system PATH (required for Whisper and TTS)
- A Cohere API key (sign up at [https://cohere.ai/](https://cohere.ai/))

## Installation

1. Clone this repository or download the source code.

2. Install required Python packages: requirements.txt

 ## Notes
The .env file is included in .gitignore to keep your API key secure.

Whisper may show a warning about FP16 not supported on CPU; this is normal if you are running on CPU.

Make sure you have a stable internet connection to use Cohere's API.
