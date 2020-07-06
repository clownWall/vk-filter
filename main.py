#   Библеотеки   #
import vk_api, random, math, plyer, tkinter
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime

#   Подключение вк:   #
session = vk_api.VkApi(token='1234')
session_api = session.get_api()
longpoll = VkLongPoll(session)

#   Код:   #
while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            response = event.text.lower()

            #   Логи:  #
            print('\nСообщение пришло в: ' + str(event.datetime))
            print('Текст сообщения:\n' + str(event.text))

            #   Ответы:   #
            if event.from_user and not event.from_me:
                if response == '!код 1334' or response == '!код 2134':
                    session.method('messages.send', {'user_id':event.user_id,'message':'Пользователь увидит ваше сообщение!','random_id':0})
                    plyer.notification.notify(message='Тебе написал человек! Проверь свой ВКонтакте!',app_name='SPAM FILTER by clownWall',title='SPAM FILTER by clownWall', )
                elif response.find('!код') != -1:
                    session.method('messages.send', {'user_id':event.user_id,'message':'Неправильный код! Попробуйте ещёь','random_id':0})
                else:
                    session.method('messages.send', {'user_id':event.user_id,'message':'Здравствуй, пользователь!\n----------\nЯ - бот-фильтр написанный\n    https://clck.ru/PV4jC\n----------\nЕсли ты по поводу, то\nу тебя должен быть 4-х\nзначный код\nДля того чтобы его ввести - введи\n!код ТвОйКоД','random_id':0})
