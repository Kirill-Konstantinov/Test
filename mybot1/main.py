from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time


token = "4654feccf6d0dd1dc77c06b81cf564bb780975f38aa84e6c5ece587e969708f976abf5eb332947297005e"
vk_session = vk_api.VkApi(token = token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while (True):
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "здравствуй":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, друг!', 'random_id': 0})
