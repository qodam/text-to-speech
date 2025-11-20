from gtts import gTTS

def texttospeech(text, lang="en", filename="audio.mp3"):
    """
    Convert text to speech and save as MP3 file.
    
    Parameters:
    -----------
    text : str
        The text to convert to speech
    lang : str, optional
        Language code (default: "en")
    filename : str, optional
        Output filename (default: "audio.mp3")
    
    Returns:
    --------
    str
        The filename of the generated audio file
    
    Examples:
    ---------
    >>> texttospeech("Hello world")
    Final audio generated : audio.mp3
    
    >>> texttospeech("Bonjour le monde", lang="fr", filename="french.mp3")
    Final audio generated : french.mp3
    """
    tts = gTTS(text, lang=lang)
    tts.save(filename)
    print("Final audio generated : " + filename)
    return filename


if __name__ == "__main__":
    # Example usage
    texttospeech("Hello world, this is a text to speech converter!", lang="en", filename="example.mp3")