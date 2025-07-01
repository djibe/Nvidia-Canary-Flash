import torch

# Load the model - Alternatives: canary-1b-flash, nvidia/canary-180m-flash
from nemo.collections.asr.models import EncDecMultiTaskModel
map_location = 'cuda' if torch.cuda.is_available() else 'cpu'
canary_model = EncDecMultiTaskModel.from_pretrained('nvidia/canary-180m-flash', map_location=map_location)

# Transcribe
audio_path = "audio.wav"
# listen_to_audio(audio_path)

# To transcribe in a particular language; this example is for English, but will work well for Spanish, French, and German
transcript = canary_model.transcribe(
  audio=[audio_path],
  batch_size=1,
  source_lang='en',	# en: English, es: Spanish, fr: French, de: German
  target_lang='en',	# should be same as "source_lang" for 'asr'
  pnc='False',
)

print("\n\nEnglish speech recognition without PnC:")
print(f'  \"{transcript[0].text}\"')
