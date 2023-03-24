# TurboGpt-cli

A CLI for openAI's GPT4 & GPT3.5 plus models. Based on [turboGPT](https://github.com/daan-dj/TurboGpt) by [daan-dj](https://github.com/daan-dj)

## Install

This script assumes that you have a GPT Plus subscription. If you don't, you can get one [here](https://beta.openai.com/pricing).


```
git clone 
cd TurboGpt-cli
pip install -r requirements.txt
```

### Getting the PUID & ACCESS_TOKEN
```
1. Head over to https://chat.openai.com/chat
2. Open the developer console (F12)
3. Go to the application tab
4. Go to local cookies
5. Copy the value of the _puid cookie
6. Copy the value of the __Secure-next-auth.session-token cookie
7. Paste the values into the .env file like so:

ACCESS_TOKEN=__Secure-next-auth.session-token cookie
PUID=_puid
```

### Starting the script (GPT3.5)
```python turbogpt-cli.py```

### For GPT4
```python turbogpt-cli.py -m gpt4```


## Usage

```bash
$ turbogpt-cli.py
                         ______           __          ______      __ 
                        /_  __/_  _______/ /_  ____  / ____/___  / /_
                         / / / / / / ___/ __ \/ __ \/ / __/ __ \/ __/
                        / / / /_/ / /  / /_/ / /_/ / /_/ / /_/ / /_  
                       /_/  \__,_/_/  /_.___/\____/\____/ .___/\__/  
                                                       /_/           
                     	TurboGpt - A CLI for chatGPT plus users

Starting session...
Session started!
You can now start talking to chatGPT.
Type 'exit' to quit.

You: help
exit - exit the program
clear - clear the screen
preset - show this help message
history - show the last 5 messages
retry or r - retry the last command
help - show this help message
You: 1+1?
ChatGPT: The sum of 1+1 is 2. Is there anything else I can help you with?
You: what was my last question?
ChatGPT: Your last question was "1+1?"
You: 
```


## Demo video

[![vimeo](https://i.imgur.com/pXHedmt.png)](https://player.vimeo.com/video/811337197?h=0ec3196060&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479)
