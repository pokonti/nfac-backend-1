import whisper

model = whisper.load_model("base")

# def transcribe(file_path: str) -> str:
#     try:
#         result = model.transcribe(file_path)
#         return result["text"]
#     except Exception as e:
#         return f"Transcription failed: {str(e)}"
def transcribe(file_path: str) -> str:
    try:
        result = model.transcribe(file_path)
        full_text = ""
        for seg in result["segments"]:
            full_text += f"[{seg['start']:.2f} - {seg['end']:.2f}] {seg['text']}\n"
        return full_text
    except Exception as e:
        return f"Transcription failed: {str(e)}"