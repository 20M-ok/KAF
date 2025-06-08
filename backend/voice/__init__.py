"""Voice module providing speech-to-text and text-to-speech utilities."""

from .speech_to_text import transcribe_audio
from .text_to_speech import synthesize_speech

__all__ = [
    "transcribe_audio",
    "synthesize_speech",
]
