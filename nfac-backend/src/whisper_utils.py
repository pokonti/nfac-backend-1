import whisper
from faster_whisper import WhisperModel

model = whisper.load_model("base")

# def transcribe(file_path: str) -> str:
#     try:
#         result = model.transcribe(file_path)
#         return result["text"]
#     except Exception as e:
#         return f"Transcription failed: {str(e)}"
# def transcribe(file_path: str) -> str:
#     try:
#         result = model.transcribe(file_path)
#         full_text = ""
#         for seg in result["segments"]:
#             full_text += f"[{seg['start']:.2f} - {seg['end']:.2f}] {seg['text']}\n"
#         return full_text
#     except Exception as e:
#         return f"Transcription failed: {str(e)}"

# def transcribe(file_path: str):
#     try:
#         result = model.transcribe(file_path, word_timestamps=True)
#         output = []
#
#         for seg in result.get("segments", []):
#             for word in seg.get("words", []):
#                 output.append({
#                     "word": word["word"],
#                     "start": round(word["start"], 2),
#                     "end": round(word["end"], 2)
#                 })
#
#         return output
#     except Exception as e:
#         return f"Transcription failed: {str(e)}"
def transcribe(file_path: str):
    try:
        result = model.transcribe(file_path, word_timestamps=True)
        output = ""

        for seg in result.get("segments", []):
            for word in seg.get("words", []):
                output += f"[{round(word['start'], 2)} - {round(word['end'], 2)}] {word['word']}\n"

        return output.strip()
    except Exception as e:
        return f"Transcription failed: {str(e)}"
