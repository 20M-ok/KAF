import os
from typing import Optional

try:
    from google.cloud import speech
except ImportError:  # pragma: no cover - library may not be installed
    speech = None


def transcribe_audio(audio_file: str, language_code: str = "en-US") -> Optional[str]:
    """Transcribe an audio file using Google Speech-to-Text.

    Parameters
    ----------
    audio_file: str
        Path to the audio file (wav/flac/etc.).
    language_code: str
        Language code for the transcription.

    Returns
    -------
    Optional[str]
        The transcribed text or ``None`` if the client is unavailable.
    """
    if speech is None:
        raise ImportError("google-cloud-speech is not installed")

    client = speech.SpeechClient()

    with open(audio_file, "rb") as audio:
        audio_content = audio.read()

    audio = speech.RecognitionAudio(content=audio_content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code=language_code,
    )

    response = client.recognize(config=config, audio=audio)
    transcripts = [result.alternatives[0].transcript for result in response.results]
    return " ".join(transcripts)


__all__ = ["transcribe_audio"]
