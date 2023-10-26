import os
from pathlib import Path
from llama_index import VectorStoreIndex
from llama_hub.file.audio import AudioTranscriber


os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

audio_file = "./about-myself.mp3"

loader = AudioTranscriber()
documents = loader.load_data(file=Path(audio_file))

# Build vector store index and query engine
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

response = query_engine.query("What's person name in the audio?")

print(response)