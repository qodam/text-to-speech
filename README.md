# Text to Speech Converter

A simple and efficient text-to-speech converter using the gTTS (Google Text-to-Speech) library.

## Description

This project converts text into MP3 audio files in multiple languages. It uses the Google Text-to-Speech API to generate high-quality audio files.

## Features

- Convert text to MP3 audio format
- Multi-language support (100+ languages)
- Automatic language detection
- Customizable speech speed (slow/normal)
- Top-level domain (TLD) selection for accent variations
- Custom output filename
- Simple and easy-to-use interface

## Installation

1. Clone this repository:
```bash
git clone https://github.com/qodam/text-to-speech.git
cd text-to-speech
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```python
from gtts import gTTS

# Basic usage
texttospeech("Hello world", lang="en", filename="output.mp3")

# Using default parameters (English)
texttospeech("Hello world")
```

### Advanced Features

```python
# Slow speech
tts = gTTS("Hello world", lang="en", slow=True)
tts.save("slow_audio.mp3")

# Different accent (using TLD)
tts = gTTS("Hello world", lang="en", tld="co.uk")  # British accent
tts.save("british_audio.mp3")

# Different languages
tts = gTTS("Bonjour le monde", lang="fr")
tts.save("french_audio.mp3")

tts = gTTS("Hola mundo", lang="es")
tts.save("spanish_audio.mp3")
```

### Parameters

- `text` (str): Text to convert to audio
- `lang` (str, optional): Language code (default: "en")
- `filename` (str, optional): Output filename (default: "audio.mp3")
- `slow` (bool, optional): Use slow speech speed (default: False)
- `tld` (str, optional): Top-level domain for accent (default: "com")

### Supported Language Codes

- `en`: English
- `fr`: French
- `es`: Spanish
- `de`: German
- `it`: Italian
- `pt`: Portuguese
- `ru`: Russian
- `ja`: Japanese
- `zh-CN`: Chinese (Simplified)
- `ar`: Arabic
- And 100+ more languages!

## Project Structure

```
text-to-speech/
│
├── main.py      # Main script with text-to-speech function
├── requirements.txt      # Project dependencies
├── .gitignore           # Git ignore file
├── README.md            # Project documentation
```

## Requirements

- Python 3.6+
- gTTS library
- Internet connection (for API access)

## Acknowledgments

- [gTTS](https://github.com/pndurette/gTTS) - Google Text-to-Speech Python library
- Google Text-to-Speech API
