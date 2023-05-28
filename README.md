# AI-Vtuber
This code is designed to read chat messages from the text box and then utilize Bard's language model to generate responses. The output from Bard is then read out loud using a TTS (Text-to-Speech) engine provided by ElevenLabs.

# Usage

Edit the variables `EL_key` and `API_key` in `AI_vtuber.py`

`EL_key` is the API key for [ElevenLabs](https://beta.elevenlabs.io/). Found in Profile Settings

`Bard_key` is the API key for Bard. Found [here](https://bard.google.com/)

Then run `AI_vtuber.py`

## Notes
You can change the voice by changing `voice` in `AI_vtuber.py`. You can find the ID's [here](https://api.elevenlabs.io/docs) in `Get Voices`

# Other
I used [This VTS plugin](https://lualucky.itch.io/vts-desktop-audio-plugin) and [VTube Studio](https://denchisoft.com/) to make the AI's TTS be able to move the mouth on VTube studio

# License
This program is under the [MIT license](/LICENSE) 
