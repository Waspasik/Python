import json
from telebot import TeleBot
import sqlite3
from telebot.types import  ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


bot = TeleBot('5646760811:AAGUT7LKb1mTtrzdeoh6-mB366WkRgHU8Ts')

fake_database = {'users':[
    {
        "id":1,
        "name":"Anna",
        "nick":"Anny42",
        "balance": 15300
     },

    {
        "id":2,
        "name":"Dima",
        "nick":"dimon2319",
        "balance": 160.23
     },
    {
        "id":3,
        "name":"Vladimir",
        "nick":"Vova777",
        "balance": 200.1
     },
    {
        "id":4,
        "name":"Anna1",
        "nick":"Anny420",
        "balance": 15300
     },

    {
        "id":5,
        "name":"Dima15",
        "nick":"dimon2342",
        "balance": 160.23
     },
    {
        "id":6,
        "name":"Vladimir666",
        "nick":"Vova13",
        "balance": 200.1
     },
    {
        "id":7,
        "name":"Anna2",
        "nick":"Anny421",
        "balance": 15300
     },

    {
        "id":8,
        "name":"Dima23",
        "nick":"dimon19",
        "balance": 160.23
     },
    {
        "id":9,
        "name":"Vladimir0nion",
        "nick":"Vova123",
        "balance": 200.1
     },
    
    ]}


@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
    query = call.data.split('_')
    query_type = call.data.split('_')[0]
	#Обработка кнопки - скрыть
    if query[0] == 'unseen':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    #Обработка кнопки - вперед и назад
    elif 'pagination' in query[0]:
        users = fake_database['users']
        json_string = json.loads(query[0])
        count = json_string['CountPage']
        page = json_string['NumberPage']
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
        if page == 1:
            markup.add(InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
        elif page == count:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '))
        else:
            markup.add(InlineKeyboardButton(text=f'<--- Назад',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page-1) + ",\"CountPage\":" + str(count) + "}"),
                       InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
                       InlineKeyboardButton(text=f'Вперёд --->',
                                            callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"))
        bot.edit_message_text(f'<b>id:</b> <i>{users[page]["id"]}</i>\n'
                              f'<b>Имя:</b> <i>{users[page]["name"]}</i>\n'
                              f'<b>Ник:</b><i>{users[page]["nick"]}</i>\n'
                              f'<b>Баланс:</b><i> {users[page]["balance"]}</i>',
                              parse_mode="HTML", reply_markup = markup,
                              chat_id=call.message.chat.id,
                              message_id=call.message.message_id)


#Обработчик входящих сообщений
@bot.message_handler(content_types=['text'])
def start(message):
    # count = len(fake_database['users']) // 4 + bool(len(fake_database['users']) % 4)
    users = fake_database['users']
    count = len(users)-1
    page = 1
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='Скрыть', callback_data='unseen'))
    markup.add(InlineKeyboardButton(text=f'{page}/{count}', callback_data=f' '),
               InlineKeyboardButton(text=f'Вперёд --->', callback_data="{\"method\":\"pagination\",\"NumberPage\":" + str(page+1) + ",\"CountPage\":" + str(count) + "}"))
    bot.send_message(message.from_user.id, f'<b>id:</b> <i>{users[page]["id"]}</i>\n'
                                    f'<b>Имя:</b> <i>{users[page]["name"]}</i>\n'
                                    f'<b>Ник:</b><i>{users[page]["nick"]}</i>\n'
                                    f'<b>Баланс:</b><i> {users[page]["balance"]}</i>',
                     parse_mode="HTML", reply_markup = markup)


if __name__ == '__main__':
    bot.polling(none_stop=True)