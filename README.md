# AI-Vtuber
This code is designed to read chat messages from the text box and then utilize Bard's language model to generate responses. The output from Bard is then read out loud using a TTS (Text-to-Speech) engine provided by ElevenLabs.

# Usage

Edit the variables `EL_key` and `OAI_key` in `config.json`

`EL_key` is the API key for [ElevenLabs](https://beta.elevenlabs.io/). Found in Profile Settings

`OAI_key` is the API key for OpenAI. Found [here](https://platform.openai.com/account/api-keys)

Then run `run.py`

## Notes
You can change the voice by changing `voice` in `config.json`. You can find the ID's [here](https://api.elevenlabs.io/docs) in `Get Voices`

# Other
I used [This VTS plugin](https://lualucky.itch.io/vts-desktop-audio-plugin) and [VTube Studio](https://denchisoft.com/) to make the AI's TTS be able to move the mouth on VTube studio

# License
This program is under the [MIT license](/LICENSE) 
