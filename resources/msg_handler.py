# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : sixBit                #
# File Name             : msg_handler.py        #
# --------------------------------------------- #

import config
from resources import mysql_handler as mysql
from resources import lang_emojis as emoji
import re
import datetime
import time
import arrow

def getReferrer(text):
    return text.split()[1] if len(text.split()) > 1 else None

def fwd_handler(user_id, bot, message):
    # Update the Spamfilter
    mysql.spam(message.chat.id)
    lang_emoji = emoji.lang_emoji(message.from_user.language_code)

    msg = bot.send_message(config.support_chat, "[{0}{1}](tg://user?id={2}) (#id{2}) | {3}\n\n{4}".format(
                          message.from_user.first_name,
                          ' {0}'.format(message.from_user.last_name) if message.from_user.last_name else '',
                          message.from_user.id, lang_emoji, message.text), parse_mode='Markdown', disable_web_page_preview=True)

    channel_id   = re.sub(r"-100(\S+)", r"\1", str(config.support_chat))
    message_id   = msg.message_id
    message_link = f'https://t.me/c/{channel_id}/{message_id}'
    mysql.post_open_ticket(message_link, user_id)

    return fwd_handler

def bad_words_handler(bot, message):
    if config.bad_words_toggle:
        if re.findall(config.regex_filter['bad_words'], message.text):
            bot.reply_to(message, '❗️ Watch your tongue...')

            return spam_handler

def time_zone():
    current_time = arrow.now(config.time_zone).strftime('%I:%M %p')
    return current_time

def repo():
    msg = '\n\n[» Source Code](github.com/sixBit/Telegram-Support-Bot)'
    return msg

def spam_handler_warning(bot, user_id, message):
    if config.spam_toggle:
        ticket_spam = mysql.user_tables(user_id)['open_ticket_spam']
        if ticket_spam > config.spam_protection:
            bot.reply_to(message, '{}, your messages are not being forwarded anymore. Please wait until the team responded. Thank you.\n\n' \
                                 f'_The support\'s local time is_ `{current_time}`.'.format(message.from_user.first_name), parse_mode='Markdown')
            return spam_handler_warning

def spam_handler_blocked(bot, user_id, message):
    if config.spam_toggle:
        ticket_spam = mysql.user_tables(user_id)['open_ticket_spam']
        if ticket_spam == config.spam_protection - 1:
            fwd_handler(user_id, bot, message)
            bot.reply_to(message, 'We will be with you shortly.\n\n{}, to prevent spam you can only send us *1* more message.\n\n' \
                                  f'_The support\'s local time is_ `{current_time}`.'.format(message.from_user.first_name), parse_mode='Markdown')
            return spam_handler_blocked


current_time   = time_zone()