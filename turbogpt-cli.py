#!/usr/bin/env python3
import argparse
import csv
import datetime
import os
import sys
import dotenv
from colorama import Fore
from pystyle import Center

from turbogpt import TurboGpt

presets = {
    "Grammar Correction": {
        "message": "Correct this to standard English:\n",
        "inject": {
            "state": True
        }
    },
    "Summarize for a second-grade student": {
        "message": "Summarize this for a second-grade student:\n",
        "inject": {
            "state": True,
        }
    },
    "Translate To English": {
        "message": "Translate this to English:\n",
        "inject": {
            "state": True,
        }
    },
    "Custom": {
        "message": "",
        "inject": {
            "state": False
        }
    },
}


def load_dotenv():
    dotenv.load_dotenv()
    if os.getenv("ACCESS_TOKEN") is None:
        print("Please set the ACCESS_TOKEN environment variable.")
        sys.exit(1)
    if os.getenv("PUID") is None:
        print("Please set the PUID environment variable.")
        sys.exit(1)
    if not os.path.exists("conversations.csv"):
        with open("conversations.csv", "w") as f:
            f.write("message,response,time\n")


def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    center = Center.XCenter("""

  ______           __          ______      __ 
 /_  __/_  _______/ /_  ____  / ____/___  / /_
  / / / / / / ___/ __ \/ __ \/ / __/ __ \/ __/
 / / / /_/ / /  / /_/ / /_/ / /_/ / /_/ / /_  
/_/  \__,_/_/  /_.___/\____/\____/ .___/\__/  
                                /_/           
""")
    print(Fore.BLUE + center)
    print(Fore.WHITE + Center.XCenter(f"\tTurboGpt - A {Fore.BLUE}CLI{Fore.RESET} for chatGPT plus users"))
    print(Fore.RESET)


def start_session():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", help="gpt4 or gpt3")
    args = parser.parse_args()
    conversation = []
    print(Fore.YELLOW + "Starting session...")
    if args.model == "gpt4":
        turbogpt = TurboGpt(model="gpt-4")
    else:
        turbogpt = TurboGpt()
    response = turbogpt.start_session()
    print(Fore.GREEN + "Session started!")
    print(Fore.WHITE + "You can now start talking to chatGPT.")
    print(Fore.WHITE + f"Type {Fore.RED}'exit'{Fore.WHITE} to quit.\n")
    while True:
        message = input(f"{Fore.CYAN}You: {Fore.WHITE}")
        if message == "exit":
            sys.exit(0)
        if message == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            welcome()
            continue
        if message == "help":
            print(f"{Fore.RED}exit{Fore.WHITE} - exit the program")
            print(f"{Fore.RED}clear{Fore.WHITE} - clear the screen")
            print(f"{Fore.RED}preset{Fore.WHITE} - show this help message")
            print(f"{Fore.RED}history{Fore.WHITE} - show the last 5 messages")
            print(f"{Fore.RED}retry or r{Fore.WHITE} - retry the last command")
            print(f"{Fore.RED}help{Fore.WHITE} - show this help message")
            continue
        if message == "history":
            print(f"{Fore.WHITE}Showing last 5 messages:")
            for i in range(1, 6):
                try:
                    print(f"{Fore.BLUE}You: {Fore.WHITE}{conversation[-i]['message']}")
                    print(f"{Fore.RED}ChatGPT: {Fore.WHITE}{conversation[-i]['response']}")
                except IndexError:
                    print("No more messages.")
            continue
        if message == "retry" or message == "r":
            print(f"{Fore.WHITE}Retrying last message...")
            message = conversation[-1]['message']
            response = turbogpt.send_message(message, response)
            print(f"{Fore.RED}ChatGPT: {Fore.WHITE}{response['message']['content']['parts'][0]}")
            conversation.append({
                "message": message,
                "response": response['message']['content']['parts'][0],
                "time": datetime.datetime.utcnow().isoformat()
            })
            with open("conversations.csv", "a") as f:
                writer = csv.DictWriter(f, fieldnames=["message", "response", "time"])
                writer.writerow(conversation[-1])
            continue
        if message == "preset" or message == "presets":
            print(f"{Fore.WHITE}Available presets:")
            i = 0
            for preset in presets:
                i += 1
                print(f"{Fore.BLUE}[{i}] - {Fore.RED}{preset}{Fore.WHITE}")
            preset = input(f"{Fore.CYAN}Preset: {Fore.WHITE}")
            if preset.isnumeric():
                preset = int(preset)
                if preset > len(presets):
                    print(f"{Fore.RED}Invalid preset.")
                    continue
                preset = list(presets)[preset - 1]

            if preset in presets:
                message = presets[preset]["message"]
                if "inject" in presets[preset]:
                    if presets[preset]["inject"]["state"]:
                        message += input(f"{Fore.CYAN}Message: {Fore.WHITE}")
            else:
                print(f"{Fore.RED}Invalid preset.")
                continue
        response = turbogpt.send_message(message, response)
        response = response
        print(f"{Fore.RED}ChatGPT: {Fore.WHITE}{response['message']['content']['parts'][0]}")
        conversation.append({
            "message": message,
            "response": response['message']['content']['parts'][0],
            "time": datetime.datetime.utcnow().isoformat()

        })
        with open("conversations.csv", "a") as f:
            writer = csv.DictWriter(f, fieldnames=["message", "response", "time"])
            writer.writerow(conversation[-1])


def main():
    load_dotenv()
    welcome()
    start_session()


if __name__ == '__main__':
    main()
