import itchat
import get_weather as weather
import speech


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    text = msg.text
    if text.find('电影') > -1:
        return '好看的电影呢'
    elif text.find('傻') > -1:
        return '你很聪明么？'
    elif text.find('天气') > -1:
        return weather.get_data('北京')
    elif text.find('在吗') > -1:
        return say_notice()
    return msg.text


@itchat.msg_register(itchat.content.VOICE)
def voice_reply(msg):
    voice = msg.text
    print(voice)
    return say_notice()


def say_notice():
    speech.say('您有新短消息')


itchat.auto_login(enableCmdQR=True)
itchat.run()
