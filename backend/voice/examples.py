"""Example usage of the voice module."""
from pathlib import Path

from .speech_to_text import transcribe_audio
from .text_to_speech import synthesize_speech


def demo_transcription():
    """Transcribe ``example.wav`` and print the result."""
    audio_path = Path("example.wav")
    if not audio_path.exists():
        print(f"Audio file {audio_path} does not exist.")
        return
    text = transcribe_audio(str(audio_path))
    print("Transcribed text:", text)


def demo_synthesis():
    """Synthesize speech for a demo sentence and save to ``output.mp3``."""
    text = "Hello from Amazon Polly!"
    audio = synthesize_speech(text)
    if audio is None:
        print("No audio data received from Polly.")
        return
    output_file = Path("output.mp3")
    output_file.write_bytes(audio)
    print(f"Audio saved to {output_file}")


__all__ = ["demo_transcription", "demo_synthesis"]
