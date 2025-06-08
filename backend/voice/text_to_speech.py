from typing import Optional

try:
    import boto3
except ImportError:  # pragma: no cover
    boto3 = None


def synthesize_speech(text: str, voice_id: str = "Joanna", output_format: str = "mp3") -> Optional[bytes]:
    """Synthesize speech using Amazon Polly.

    Parameters
    ----------
    text: str
        Text to synthesize.
    voice_id: str
        Polly voice ID.
    output_format: str
        Audio format.

    Returns
    -------
    Optional[bytes]
        Audio data in the requested format or ``None`` if the client is unavailable.
    """
    if boto3 is None:
        raise ImportError("boto3 is not installed")

    polly = boto3.client("polly")
    response = polly.synthesize_speech(Text=text, OutputFormat=output_format, VoiceId=voice_id)
    return response.get("AudioStream").read() if "AudioStream" in response else None


__all__ = ["synthesize_speech"]
