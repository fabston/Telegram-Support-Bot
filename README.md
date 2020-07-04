<p align="center"><a href="https://github.com/sixbit/Telegram-Support-Bot" target="_blank"><img src="https://i.imgur.com/vft81xp.png"></a></p>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-380/"><img src="https://img.shields.io/badge/python-3.8-blue.svg?style=plastic" alt="Python version"></a>
    <a href="https://github.com/sixBit/Telegram-Support-Bot/blob/master/LICENSE"><img src="https://img.shields.io/github/license/sixbit/Telegram-Support-Bot?style=plastic" alt="GitHub license"></a>
    <a href="https://github.com/sixBit/Telegram-Support-Bot/issues"><img src="https://img.shields.io/github/issues/sixbit/Telegram-Support-Bot?style=plastic" alt="GitHub issues"></a>
    <a href="https://github.com/sixBit/Telegram-Support-Bot/pulls"><img src="https://img.shields.io/github/issues-pr/sixbit/Telegram-Support-Bot?style=plastic" alt="GitHub pull requests"></a>
    <br /><a href="https://github.com/sixBit/Telegram-Support-Bot/stargazers"><img src="https://img.shields.io/github/stars/sixbit/Telegram-Support-Bot?style=social" alt="GitHub stars"></a>
    <a href="https://github.com/sixBit/Telegram-Support-Bot/network/members"><img src="https://img.shields.io/github/forks/sixbit/Telegram-Support-Bot?style=social" alt="GitHub forks"></a>
    <a href="https://github.com/sixBit/Telegram-Support-Bot/watchers"><img src="https://img.shields.io/github/watchers/sixbit/Telegram-Support-Bot?style=social" alt="GitHub watchers"></a>
    <br /><a href="https://sixbit.io/telegram"><img src="https://img.shields.io/badge/Join-Server-00457c.svg?logo=telegram&style=plastic" alt="Join Telegram Server"></a>
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
- Spam protection (sensitivity can be set in [`config.py`](https://github.com/sixBit/Telegram-Support-Bot/blob/master/config.py))
- Bad words filter (using regex, words can be set in [`config.py`](https://github.com/sixBit/Telegram-Support-Bot/blob/master/config.py))
- List all open/unanswered tickets (time passed since ticket opened is being shown as well)
- Ban / Un-ban users (via reply or user id). User won't be able to interact with the bot anymore
- List banned users, with last interaction point
- Detect the users language and display it as an emoji

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


## Installation
> 💡 Best to run the bot on a VPS. My recommendation would be [vultr](sixbit.io/vultr)
1. Create and setup a MySQL database and it's table `users`. The required fields can be found [here](https://i.imgur.com/cP15QfD.png)
2. Clone this repository `git clone https://github.com/sixBit/Telegram-Support-Bot.git`
3. Create your virtual environment `python3 -m venv Telegram-Support-Bot`
4. Activate it `source Telegram-Support-Bot/bin/activate && cd Telegram-Support-Bot`
5. Install all requirements `pip install -r requirements.txt`
6. Edit and update [`config.py`](https://github.com/sixBit/Telegram-Support-Bot/blob/master/config.py)
7. Run the bot `python main.py`


## Images
![Telegram Support Bot](https://i.imgur.com/z2bSKvz.jpg)

## How can I help?
All kinds of contributions are welcome! The most basic way to show your support is to `⭐️ star` the project, or to raise [issues](https://github.com/sixBit/Telegram-Support-Bot/issues/new).