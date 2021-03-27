# --------------------------------------------- #
# Plugin Name           : Telegram Support Bot  #
# Author Name           : fabston               #
# File Name             : mysql_handler.py      #
# --------------------------------------------- #

import pymysql
import config
from datetime import datetime


# Connect to MySQL Database
def getConnection():
    connection = pymysql.connect(host=config.mysql_host,
                                 user=config.mysql_user,
                                 password=config.mysql_pw,
                                 db=config.mysql_db,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit=True)
    return connection


def createTables():
    connection = getConnection()
    with connection.cursor() as cursor:
        tablename = "users"
        try:
            cursor.execute(
                "	CREATE TABLE `" + tablename + "` (  `userid` int(11) DEFAULT NULL,  `open_ticket` int(4) DEFAULT 0,  `banned` int(4) DEFAULT 0,  \
                `open_ticket_spam` int(4) DEFAULT 1,  `open_ticket_link` varchar(50) DEFAULT NULL,  `open_ticket_time` datetime NOT NULL DEFAULT '1000-01-01 00:00:00')")
            return createTables
        except Exception as e:
            print(e)


def spam(user_id):
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "SELECT banned, open_ticket, open_ticket_spam FROM users WHERE userid = %s"
        cursor.execute(sql, user_id)
        data = cursor.fetchone()
        ticket_spam = data['open_ticket_spam']

        sql = "UPDATE users SET open_ticket_spam = %s WHERE userid = %s"
        spam = ticket_spam + 1
        cursor.execute(sql, (spam, user_id))
        return spam


def user_tables(user_id):
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "SELECT open_ticket, banned, open_ticket_time, open_ticket_spam, open_ticket_link FROM users WHERE userid = %s"
        cursor.execute(sql, user_id)
        data = cursor.fetchone()
        return data


def getOpenTickets():
    connection = getConnection()
    with connection.cursor() as cursor:
        tmp = []
        cursor.execute("SELECT userid FROM users WHERE open_ticket = 1")
        for i in cursor.fetchall():
            tmp.append(i['userid'])
        return tmp


def getBanned():
    connection = getConnection()
    with connection.cursor() as cursor:
        tmp = []
        cursor.execute("SELECT userid FROM users WHERE banned = 1")
        for i in cursor.fetchall():
            tmp.append(i['userid'])
        return tmp


def start_bot(user_id):
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "SELECT EXISTS(SELECT userid FROM users WHERE userid = %s)"
        cursor.execute(sql, user_id)
        result = cursor.fetchone()
        # If the User never started the bot before, add the Telegram ID to the database
        if not list(result.values())[0]:
            sql = "INSERT INTO users(userid) VALUES (%s)"
            cursor.execute(sql, user_id)


def open_ticket(user_id):
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "UPDATE users SET open_ticket = 1, open_ticket_time = %s WHERE userid = %s"
        now = datetime.now()
        cursor.execute(sql, (now, user_id))
        open_tickets.append(user_id)
        return open_ticket


def post_open_ticket(link, msg_id):
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "UPDATE users SET open_ticket_link = %s WHERE userid = %s"
        cursor.execute(sql, (link, msg_id))
        return post_open_ticket


def reset_open_ticket(user_id):
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "UPDATE users SET open_ticket = 0,  open_ticket_spam = 1 WHERE userid = %s"
        cursor.execute(sql, user_id)
        open_tickets.pop(open_tickets.index(user_id))
        return reset_open_ticket


def ban_user(user_id):
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "UPDATE users SET banned = 1 WHERE userid = %s"
        cursor.execute(sql, user_id)
        banned.append(user_id)
        return ban_user


def unban_user(user_id):
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "UPDATE users SET banned = 0 WHERE userid = %s"
        cursor.execute(sql, user_id)
        banned.pop(banned.index(user_id))
        return unban_user


createTables = createTables()
open_tickets = getOpenTickets()
banned = getBanned()
