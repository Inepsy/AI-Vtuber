import requests
import json
import win32com.client as wincl

history_ids = ["", "", ""]
api_keys = [
    "Put bard key here.",
    "Put bard key here."
]
at_vars = [
    "ABi_lZiMCLkX08DeqRzeeujgNLqp%3A1681341296079",
    "ABi_lZh4X1Gg449HStgiwwXbp4bo%3A1680948998927"
]
elevenlabs_api_keys = ["ElevenLabs API key here", ""]
api_key_num = 0

def main():
    #TextToSpeech("Hi")
    last_msg = "Hi, what do you think about AI?"
    while True:
        print("\n")
        last_msg = input(">> ")
        print("\n")
        last_msg = ParseResponse(GetRawResponse(last_msg.replace("\n", "") + " Respond in a chatty shortened form."))
        print(last_msg)
        TextToSpeech(last_msg)

def GetRawResponse(input):
    url = "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate?bl=boq_assistant-bard-web-server_20230404.15_p0&_reqid=1440589"
    cookie = "__Secure-1PSID=" + api_keys[api_key_num]
    headers = {
        "cookie": cookie,
        "origin": "https://bard.google.com"
    }
    body = "f.req=%5Bnull%2C%22%5B%5B%5C%22" + input + "%5C%22%5D%2Cnull%2C%5B%5C%22" + history_ids[0] + "%5C%22%2C%5C%22" + history_ids[1] + "%5C%22%2C%5C%22" + history_ids[2] + "%5C%22%5D%5D%22%5D&at=" + at_vars[api_key_num] + "&"
    response = requests.post(url, headers=headers, data=body)
    return response.content.decode()

def ParseResponse(input):
    offset = 6
    offsetted = input[offset:]
    json_data = json.loads(offsetted)
    if json_data[0][2] == None:
        return "Rate limit is reached!"
    history_data = json_data[0][2]
    history_data = json.loads(history_data)
    history_ids[0] = history_data[1][0]
    history_ids[1] = history_data[1][1]
    history_ids[2] = history_data[4][0][0]
    return json_data[0][0]

def TextToSpeech(input):
    speaker = wincl.Dispatch("SAPI.SpVoice")
    speaker.Speak(input)

if __name__ == "__main__":
    main()

