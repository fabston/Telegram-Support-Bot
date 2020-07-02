# Telegram Support Bot

![Python3.8](https://img.shields.io/badge/python-3.8-blue.svg) ![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

This is a Telegram Support Bot written in Python. It's meant to help you manage your support inquiries on Telegram.

## Features
- Spam protection (sensitivity can be set in `config.py`)
- Bad words filter (using regex, words can be set in `config.py`)
- List all open/unanswered tickets (time passed since ticket opened is being shown as well)
- Ban / Un-ban users (via reply or user id). User won't be able to interact with the bot anymore
- List banned users, with last interaction point
- Detect the users language and display it as an emoji

## Bot commands
| Command | Description |
| --- | --- |
| /ban | Ban user by ID or reply |
| /unban | Un-ban user by ID or reply |
| /banned | List banned users |
| /tickets or /t | List open tickets |


## Usage
1. Create and setup a MySQL database and it's table `users`. The required fields can be found [here](https://i.imgur.com/cP15QfD.png)
1. Clone this repository `git clone https://github.com/sixBit/Telegram-Support-Bot`
2. Create your virtual environment `python3.8 -m venv TradingView-Webhook-Bot`
3. Activate it `source TradingView-Webhook-Bot/bin/activate`
4. Install all requirements `pip install -r requirements.txt`
5. Edit and update the `config.py` file
6. Run the bot `python main.py`


## Images
![Telegram Support Bot](https://i.imgur.com/z2bSKvz.jpg)

## Donations
If you find the bot suitable for your needs, please consider donating whatever amount you like to:

#### Bitcoin (BTC)
```
bc1q33xz5sdqqku3629mkeksdglvq3th4l59de8qpz
```