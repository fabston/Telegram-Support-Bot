# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : vsnz                  #
# File Name             : main.py               #
# --------------------------------------------- #

import config
from resources import mysql_handler as mysql
from resources import markups_handler as markup
from resources import msg_handler as msg

import telebot
from datetime import datetime
import arrow

bot = telebot.TeleBot(config.token)

mysql.createTables

# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
     if call.message:
        if call.data == "faqCallbackdata":
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=config.text_messages['faqs'], parse_mode='Markdown', disable_web_page_preview=True)

# Start Command
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, config.text_messages['start'].format(message.from_user.first_name) + msg.repo(), parse_mode='Markdown', disable_web_page_preview=True, reply_markup=markup.faqButton())
        mysql.start_bot(message.chat.id)
    else:
        bot.reply_to(message, 'Please send me a PM if you\'d like to talk to the Support Team.')

# FAQ Command
@bot.message_handler(commands=['faq'])
def start(message):
    if message.chat.type == 'private':
        bot.reply_to(message, config.text_messages['faqs'], parse_mode='Markdown', disable_web_page_preview=True)
    else:
        pass

# Get All Open Tickets
@bot.message_handler(commands=['tickets', 't'])
def ot_handler(message):
    if message.chat.id == config.support_chat:
        if not mysql.open_tickets:
            bot.reply_to(message, "ℹ️ Great job, you answered all your tickets!")
            return
        
        ot_msg = '📨 *Open tickets:*\n\n'
        for user in mysql.open_tickets:
            bot.send_chat_action(message.chat.id, 'typing')
            ot_link = mysql.user_tables(int(user))['open_ticket_link']

            now = arrow.now()
            diff = datetime.now() - mysql.user_tables(int(user))['open_ticket_time']
            diff.total_seconds()/3600    # seconds to hour
            time_since_secs = float(diff.seconds)
            time_since = now.shift(seconds=-time_since_secs).humanize()

            # Bring attention to 1 day old tickets
            if time_since_secs > config.open_ticket_emoji * 3600:
                alert = ' ↳ ⚠️ '
            else:
                alert = ' ↳ '

            ot_msg += "• [{0}{1}](tg://user?id={2}) (`{2}`)\n{5}_{3}_ [➜ Go to msg]({4})\n".format(
                bot.get_chat(int(user)).first_name,
                ' {0}'.format(bot.get_chat(int(user)).last_name) if bot.get_chat(int(user)).last_name else '',
                int(user), time_since, ot_link, alert)

        bot.send_message(message.chat.id, ot_msg, parse_mode='Markdown')
    else:
        pass

# Close a ticket manually
@bot.message_handler(commands=['close', 'c'])
def ot_handler(message):
    if message.chat.id == config.support_chat:
        if message.reply_to_message and '(#id' in message.reply_to_message.text:
            bot.send_chat_action(message.chat.id, 'typing')
            user_id = int(message.reply_to_message.text.split('(#id')[1].split(')')[0])
            ticket_status = mysql.user_tables(user_id)['open_ticket']

            if ticket_status == 0:
                bot.reply_to(message, '❌ That user has no open ticket...')
            else:
                # Reset Open Tickets as well as the Spamfilter
                mysql.reset_open_ticket(user_id)
                bot.reply_to(message, '✅ Ok, closed that users ticket!')
        else:
            bot.reply_to(message, 'ℹ️ You\'d have to reply to a message')
    else:
        pass

# Get Banned User
@bot.message_handler(commands=['banned'])
def ot_handler(message):
    if message.chat.id == config.support_chat:
        if not mysql.banned:
            bot.reply_to(message, "ℹ️ Great news, nobody got banned... Yet.")
            return
        
        ot_msg = '⛔️ *Banned users:*\n\n'
        for user in mysql.banned:
            bot.send_chat_action(message.chat.id, 'typing')
            ot_link = mysql.user_tables(int(user))['open_ticket_link']
                
            ot_msg += "• [{0}{1}](tg://user?id={2}) (`{2}`)\n[➜ Go to last msg]({3})\n".format(
                bot.get_chat(int(user)).first_name,
                ' {0}'.format(bot.get_chat(int(user)).last_name) if bot.get_chat(int(user)).last_name else '',
                int(user), ot_link)

        bot.send_message(message.chat.id, ot_msg, parse_mode='Markdown')
    else:
        pass

# Ban User
@bot.message_handler(commands=['ban'])
def ot_handler(message):
    try:
        if message.chat.id == config.support_chat:
            if message.reply_to_message and '(#id' in msg.msgCheck(message):
                user_id = msg.getUserID(message)
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 1:
                    bot.reply_to(message, '❌ That user is already banned...')
                else:
                    mysql.ban_user(user_id)
                    try:
                        # Reset Open Tickets as well as the Spamfilter
                        mysql.reset_open_ticket(user_id)
                    except Exception as e:
                        pass
                    bot.reply_to(message, '✅ Ok, banned that user!')

            elif msg.getReferrer(message.text):
                user_id = int(msg.getReferrer(message.text))
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 1:
                    bot.reply_to(message, '❌ That user is already banned...')
                else:
                    mysql.ban_user(user_id)
                    try:
                        # Reset Open Tickets as well as the Spamfilter
                        mysql.reset_open_ticket(user_id)
                    except Exception as e:
                        pass
                    bot.reply_to(message, '✅ Ok, banned that user!')
        else:
            bot.reply_to(message, 'ℹ️ You\'d have to either reply to a message or mention an `Users ID`.', parse_mode='Markdown')
    except TypeError:
        bot.reply_to(message, '❌ Are you sure I interacted with that user before...?')

# Un-ban Useer
@bot.message_handler(commands=['unban'])
def ot_handler(message):
    try:
        if message.chat.id == config.support_chat:
            if message.reply_to_message and '(#id' in msg.msgCheck(message):
                user_id = msg.getUserID(message)
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 0:
                    bot.reply_to(message, '❌ That user is already un-banned...')
                else:
                    mysql.unban_user(user_id)
                    bot.reply_to(message, '✅ Ok, un-banned that user!')

            elif msg.getReferrer(message.text):
                user_id = int(msg.getReferrer(message.text))
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 0:
                    bot.reply_to(message, '❌ That user is already un-banned...')
                else:
                    mysql.unban_user(user_id)
                    bot.reply_to(message, '✅ Ok, un-banned that user!')
            else:
                bot.reply_to(message, 'ℹ️ You\'d have to either reply to a message or mention an `Users ID`.', parse_mode='Markdown')
    except TypeError:
        bot.reply_to(message, '❌ Are you sure I interacted with that user before...?')


# Message Forward Handler (User - Support)
@bot.message_handler(func=lambda message: message.chat.type == 'private', content_types=['text', 'photo', 'document'])
def echo_all(message):
    while True:
        mysql.start_bot(message.chat.id)
        user_id       = message.chat.id
        message       = message
        banned        = mysql.user_tables(user_id)['banned']
        ticket_status = mysql.user_tables(user_id)['open_ticket']
        ticket_spam   = mysql.user_tables(user_id)['open_ticket_spam']

        if banned == 1:
            return
        elif msg.spam_handler_warning(bot, user_id, message): # First spam warning
            return
        elif msg.bad_words_handler(bot, message):
            return
        elif msg.spam_handler_blocked(bot, user_id, message): # Final spam warning // user cant send messages anymore
            return
        elif ticket_status == 0:
            mysql.open_ticket(user_id)
            continue        
        else:
            msg.fwd_handler(user_id, bot, message)
            return

# Message Forward Handler (Support - User)
@bot.message_handler(content_types=['text', 'photo', 'document'])
def echo_all(message):
    while True:
        try:
            try:    
                user_id       = msg.getUserID(message)
                message       = message
                text          = message.text
                msg_check     = msg.msgCheck(message)
                ticket_status = mysql.user_tables(user_id)['open_ticket']
                banned_status = mysql.user_tables(user_id)['banned']

                if banned_status == 1:
                    # If User is banned - un-ban user and sent message
                    mysql.unban_user(user_id)
                    bot.reply_to(message, 'ℹ️ *FYI: That user was banned.*\n_Un-banned and sent message!_', parse_mode='Markdown')

                elif ticket_status == 1:
                    # Reset Open Tickets as well as the Spamfilter
                    mysql.reset_open_ticket(user_id)
                    continue

                else:
                    if message.reply_to_message and '(#id' in msg_check:
                        msg.snd_handler(user_id, bot, message, text)
                        return

            except telebot.apihelper.ApiException: 
                bot.reply_to(message, '❌ I was unable to send that message...\nThe user might\'ve blocked me.')
                return
                
        except Exception as e: 
            bot.reply_to(message, '❌ Invalid command!')
            return

            
print("Telegram Support Bot started...")
bot.polling()