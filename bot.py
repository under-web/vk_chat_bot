import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

main_token = 'your token'

keyboard = VkKeyboard(one_time=True)
keyboard.add_button('Да, являюсь', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Нет, не являюсь таковым', color=VkKeyboardColor.SECONDARY)

keyboard2 = VkKeyboard(one_time=True)
keyboard2.add_button('Мне уже есть 21', color=VkKeyboardColor.SECONDARY)
keyboard2.add_button('Мне больше 45', color=VkKeyboardColor.SECONDARY)

keyboard3 = VkKeyboard(one_time=True)
keyboard3.add_button('Да, есть судимость', color=VkKeyboardColor.SECONDARY)
keyboard3.add_button('Нет судимости', color=VkKeyboardColor.SECONDARY)

keyboard4 = VkKeyboard(one_time=True)
keyboard4.add_button('Нет задолженостей', color=VkKeyboardColor.SECONDARY)
keyboard4.add_button('Есть долг', color=VkKeyboardColor.SECONDARY)

keyboard5 = VkKeyboard(one_time=True)
keyboard5.add_button('Есть гражданство РФ', color=VkKeyboardColor.SECONDARY)
keyboard5.add_button('Нет гражданства РФ', color=VkKeyboardColor.SECONDARY)

keyboard6 = VkKeyboard(one_time=True)
keyboard6.add_button('Казань, РТ', color=VkKeyboardColor.SECONDARY)
keyboard6.add_button('Я из другого города', color=VkKeyboardColor.SECONDARY)

keyboard7 = VkKeyboard(one_time=True)
keyboard7.add_button('Казань, РТ', color=VkKeyboardColor.SECONDARY)
keyboard7.add_button('Я из другого города', color=VkKeyboardColor.SECONDARY)

vk_session = vk_api.VkApi(token=main_token)
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

image = 'money.jpg'
upload = VkUpload(vk_session)
attachments = []
upload_image = upload.photo_messages(photos=image)[0]
attachments.append('photo{}_{}'.format(upload_image['owner_id'], upload_image['id']))

def sender_out(id, text):
    vk_session.method('messages.send', {'user_id': id,
                                        'message': text,
                                        'random_id': 0,
                                        })


def sender(id, text):
    vk_session.method('messages.send', {'user_id': id,
                                        'message': text,
                                        'random_id': 0,
                                        'keyboard': keyboard.get_keyboard(),
                                        'attachment': ','.join(attachments)})


def sender_2(id, text):
    vk_session.method('messages.send', {'user_id': id,
                                        'message': text,
                                        'random_id': 0,
                                        'keyboard': keyboard2.get_keyboard()})


def sender_3(id, text):
    vk_session.method('messages.send', {'user_id': id,
                                        'message': text,
                                        'random_id': 0,
                                        'keyboard': keyboard3.get_keyboard()})


def sender_4(id, text):
    vk_session.method('messages.send', {'user_id': id,
                                        'message': text,
                                        'random_id': 0,
                                        'keyboard': keyboard4.get_keyboard()})


def sender_5(id, text):
    vk_session.method('messages.send', {'user_id': id,
                                        'message': text,
                                        'random_id': 0,
                                        'keyboard': keyboard5.get_keyboard()})


def sender_6(id, text):
    vk_session.method('messages.send', {'user_id': id,
                                        'message': text,
                                        'random_id': 0,
                                        'keyboard': keyboard6.get_keyboard()})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:

            msg = event.text.lower()
            id = event.user_id

            if msg == 'привет':
                txt = '''
                Юридическая компания предлагает дополнительный заработок за 14 дней!!!🔥🔥🔥
              
                Мы готовим новые компании с расчётными счётами 
                для дальнейшего переоформления на покупателя,
                через нотариальную контору( договор купли-продажи).
                Без рисков,все в рамках закона РФ 💼
    
                Пройдите короткий опрос.⤵️
              
                Являетесь ли вы зарегистрированным руководителем 
                или индивидуальным предпринимателям сейчас или
                за последние 3 года?'''
                sender(id, txt)
            elif msg == 'да, являюсь':
                sender_out(id, 'Извините вы нам не подходите')
            elif msg == 'нет, не являюсь таковым':
                sender_2(id, 'Хорошо! Ваш возраст от 21 до 45 ?')
            elif msg == 'мне больше 45':
                sender_out(id, 'К сожалению вы нам не подходите,'
                               'но вы можете порекомендовать нас друзьям и заработать')
            elif msg == 'мне уже есть 21':
                sender_3(id, 'Имеется ли у вас судимость в том числе непогашенная?')
            elif msg == 'да, есть судимость':
                sender_out(id, 'К сожалению вы нам не подходите,'
                               'но вы можете порекомендовать нас друзьям и заработать')
            elif msg == 'нет судимости':
                sender_4(id, 'Отлично! Имеется ли у вас задолженность ФССП?')
            elif msg == 'есть долг':
                sender_out(id, 'К сожалению вы нам не подходите,'
                               'но вы можете порекомендовать нас друзьям и заработать')
            elif msg == 'нет задолженостей':
                sender_5(id, 'Вы гражданин РФ?')
            elif msg == 'нет гражданства рф':
                sender_out(id, 'К сожалению вы нам не подходите,'
                               'но вы можете порекомендовать нас друзьям и заработать')
            elif msg == 'есть гражданство рф':
                sender_6(id, 'Место жительства город Казань или РТ?')
            elif msg == 'я из другого города':
                sender_out(id, 'К сожалению вы нам не подходите,'
                               'но вы можете порекомендовать нас друзьям и заработать')
            elif msg == 'казань, рт':
                txt = '''
                Отлично! Вы нам подходите!🎉🎉🎉 

                Оставьте свой номер телефона (через +7), а так же ваше Имя🎫📫📝

                Мы с вами свяжемся в кратчайшее время!!!'''
                sender_out(id, txt)
            elif '+7' in msg:
                sender_out(575062964, msg)


            else:
                sender_out(id, 'Я вас не понял, введите корректные данные')
