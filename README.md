<p align="center"><a href="https://github.com/vsnz/Telegram-Support-Bot" target="_blank"><img src="https://raw.githubusercontent.com/vsnz/Telegram-Support-Bot/master/assets/logo.png"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.8-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/vsnz/Telegram-Support-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/vsnz/Telegram-Support-Bot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/vsnz/Telegram-Support-Bot/issues"><img src="https://img.shields.io/github/issues/vsnz/Telegram-Support-Bot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/vsnz/Telegram-Support-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/vsnz/Telegram-Support-Bot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/vsnz/Telegram-Support-Bot/stargazers"><img src="https://img.shields.io/github/stars/vsnz/Telegram-Support-Bot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/vsnz/Telegram-Support-Bot/network/members"><img src="https://img.shields.io/github/forks/vsnz/Telegram-Support-Bot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/vsnz/Telegram-Support-Bot/watchers"><img src="https://img.shields.io/github/watchers/vsnz/Telegram-Support-Bot?style=social" alt="GitHub watchers"></a>
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
The **Telegram Support Bot** 📬 helps you to manage and organize your support inquiries using the [`pyTelegramBotAPI`](https://github.com/eternnoir/pyTelegramBotAPI) libary.

## Features
- **Text**, **Photos**, **Documents** and **Stickers** are being forwarded
- Spam protection (sensitivity can be set in [`config.py`](https://github.com/vsnz/Telegram-Support-Bot/blob/master/config.py))
- Bad words filter (using regex, words can be set in [`config.py`](https://github.com/vsnz/Telegram-Support-Bot/blob/master/config.py))
- List all open/unanswered tickets (time passed since ticket opened is being shown as well)
- Ban / Un-ban users (via reply or user id). User won't be able to interact with the bot anymore
- List banned users, with last interaction point
- Customisable FAQ text
- Detect the users language and display it as an emoji

> 💡 Got a feature idea? Open an [issue](https://github.com/vsnz/Telegram-Support-Bot/issues/new) and I might implement it.

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
> ⚠️ Best to run the bot on a VPS. I can recommend [Hetzner](https://hetzner.cloud/?ref=tQ1NdT8zbfNY).
1. Log into MySQL (`sudo mysql`) and create a dedicated database and user with the following commands:
   1. `CREATE DATABASE TelegramSupportBot;`
   1. `CREATE USER 'tsbuser'@'localhost' IDENTIFIED BY 'your-password';`
   1. `GRANT ALL PRIVILEGES ON TelegramSupportBot . * TO 'tsbuser'@'localhost';`
   1. `exit;`
1. Clone this repository `git clone https://github.com/vsnz/Telegram-Support-Bot.git`
1. Create your virtual environment `python3 -m venv Telegram-Support-Bot`
1. Activate it `source Telegram-Support-Bot/bin/activate && cd Telegram-Support-Bot`
1. Install all requirements `pip install -r requirements.txt`
1. Edit and update [`config.py`](https://github.com/vsnz/Telegram-Support-Bot/blob/master/config.py)
1. Run the bot `python main.py`


## Images
![Telegram Support Bot](https://i.imgur.com/JQ7lJce.jpg)

## How can I help?
All kinds of contributions are welcome 🙌! The most basic way to show your support is to `⭐️ star` the project, or raise [`🐞 issues`](https://github.com/vsnz/Telegram-Support-Bot/issues/new). You 

***

<p align="center">
    <a href="https://liberapay.com/vsnz/donate"><img alt="Donate using LiberaPay" src="https://liberapay.com/assets/widgets/donate.svg"></a>
</p>