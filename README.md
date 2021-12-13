<p align="center"><a href="https://github.com/fabston/Telegram-Support-Bot" target="_blank"><img src="https://raw.githubusercontent.com/fabston/Telegram-Support-Bot/master/assets/logo.png"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.9-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/fabston/Telegram-Support-Bot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/issues"><img src="https://img.shields.io/github/issues/fabston/Telegram-Support-Bot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/fabston/Telegram-Support-Bot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/fabston/Telegram-Support-Bot/stargazers"><img src="https://img.shields.io/github/stars/fabston/Telegram-Support-Bot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/network/members"><img src="https://img.shields.io/github/forks/fabston/Telegram-Support-Bot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/fabston/Telegram-Support-Bot/watchers"><img src="https://img.shields.io/github/watchers/fabston/Telegram-Support-Bot?style=social" alt="GitHub watchers"></a>
</p>

<p align="center">
  <a href="#about">About</a>
  •
  <a href="#features">Features</a>
  •
  <a href="#installation">Installation</a>
  •
  <a href="#images">Images</a>
  •
  <a href="#how-can-i-help">Help</a>
</p>

## About
The **Telegram Support Bot** 📬 helps you to manage and organize your support inquiries.

## Features
- **Text**, **Photos**, **Documents** and **Stickers** are being forwarded
- Spam protection (sensitivity can be set in [`config.py`](https://github.com/fabston/Telegram-Support-Bot/blob/master/config.py))
- Bad words filter (using regex, words can be set in [`config.py`](https://github.com/fabston/Telegram-Support-Bot/blob/master/config.py))
- List all open/unanswered tickets (time passed since ticket opened is being shown as well)
- Ban / Un-ban users (via reply or user id). User won't be able to interact with the bot anymore
- List banned users, with last interaction point
- Customisable FAQ text
- Detect the users language and display it as an emoji

> 💡 Got a feature idea? Open an [issue](https://github.com/fabston/Telegram-Support-Bot/issues/new?assignees=&labels=enhancement&template=feature-request---.md) and I might implement it.

### Staff commands
| Command | Description |
| --- | --- |
| /ban | Ban user by ID or reply |
| /unban | Un-ban user by ID or reply |
| /banned | List banned users |
| /tickets or /t | List open tickets |
| /close or /c | Manually close a ticket by reply |

### User commands
| Command | Description |
| --- | --- |
| /start | Starts the bot |
| /faq | Show the FAQ's |


## Installation
> ⚠️ Best to run the bot on a VPS. I can recommend <a href="https://hetzner.cloud/?ref=tQ1NdT8zbfNY" title="Get €20 in cloud credits">Hetzner</a>'s CX11 VPS for 2.89€/month. [Sign up](https://hetzner.cloud/?ref=tQ1NdT8zbfNY) now and receive **€20 free** credits.
1. Log into MySQL (`sudo mysql`) and create a dedicated database and user with the following commands:
   1. `CREATE DATABASE TelegramSupportBot;`
   1. `CREATE USER 'SupportBotUser'@'localhost' IDENTIFIED BY '<YOUR PASSWORD>';`
   1. `GRANT ALL PRIVILEGES ON TelegramSupportBot . * TO 'SupportBotUser'@'localhost';`
   1. `exit;`
1. Clone this repository `git clone https://github.com/fabston/Telegram-Support-Bot.git`
1. Create your virtual environment `python3 -m venv Telegram-Support-Bot`
1. Activate it `source Telegram-Support-Bot/bin/activate && cd Telegram-Support-Bot`
1. Install all requirements `pip install -r requirements.txt`
1. Edit and update [`config.py`](https://github.com/fabston/Telegram-Support-Bot/blob/master/config.py)
1. Run the bot `python main.py`


## Images
![Telegram Support Bot](https://raw.githubusercontent.com/fabston/Telegram-Support-Bot/master/assets/about.jpg)

## How can I help?
All kinds of contributions are welcome 🙌! The most basic way to show your support is to `⭐️ star` the project, or raise [`🐞 issues`](https://github.com/fabston/Telegram-Support-Bot/issues/new/choose). 

***

<p align="center">
    <a href="https://www.buymeacoffee.com/fabston"><img alt="Buy Me A Coffee" title="☕️" src="https://github.com/fabston/Telegram-Airdrop-Bot/blob/main/assets/bmac.png?raw=true" width=200px></a>
</p>