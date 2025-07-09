# Nvidia Canary Flash

The python code to run [Nvidia Canary Flash](https://huggingface.co/nvidia/canary-1b-flash) ASR AI (Automatic Speech Recognition and translation), in the [top ASR leaderboards](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard).

The model supports:

- Automatic speech-to-text recognition (ASR) in 4 languages: English, German, French, Spanish
- Translation from English to German/French/Spanish and from German/French/Spanish to English
- With or without punctuation and capitalization (PnC)
- Experimental feature for word-level and segment-level timestamps in English, German, French, and Spanish

For English only ASR, the best model is [Nvidia parakeet-tdt-0.6b-v2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2).

## 🏃 How to run ?

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/#installing-uv) python manager
2. Commands: `git clone https://github.com/djibe/Nvidia-Canary-Flash.git`
3. `cd Nvidia-Canary-Flash`
4. and finally `uv run main.py`

### ❓ More info

You can switch to the smaller model (`nvidia/canary-180m-flash`) to save computing resources.

The model handles voice chunks of maximum 40 seconds with mono channel, that can be computed in sequence.
