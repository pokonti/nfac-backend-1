import whisper

model = whisper.load_model("base")

def transcribe(file_path: str) -> str:
    try:
        result = model.transcribe(file_path)
        return result["text"]
    except Exception as e:
        return f"Transcription failed: {str(e)}"
