from elevenlabs.client import ElevenLabs

import os

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY", "YOUR_API_KEY_HERE")
)

voices = client.voices.search()

for voice in voices.voices:
    print(voice.name, "->", voice.voice_id)