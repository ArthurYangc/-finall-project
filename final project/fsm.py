from transitions.extensions import GraphMachine

from utils import send_text_message, send_carousel_message, send_button_message, send_image_message
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"
    
    def on_enter_start(self, event):
        title = '你好，這裡是生活小助手，請選擇需要的服務\n輸入"start"可回到初始頁面'
        text = '輸入"天氣"可看天氣\n輸入"貓咪"可看貓咪\n輸入"吃飯"選擇類型'
        btn = [
            MessageTemplateAction(
                label = 'start',
                text ='start'
            ),
            MessageTemplateAction(
                label = '天氣',
                text = '天氣'
            ),
            MessageTemplateAction(
                label = '貓咪',
                text = '貓咪'
            ),
            MessageTemplateAction(
                label = '吃飯',
                text = '吃飯'
            ),
        ]
        url = 'https://cdn-icons-png.flaticon.com/512/5331/5331483.png'
        send_button_message(event.reply_token, title, text, btn, url)
        
        
        
        
    def is_going_to_weather(self, event):
        text = event.message.text
        return text.lower() == "天氣"
    
    def on_enter_weather(self, event):
        print("I'm entering weather")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com/search?q=%E5%A4%A9%E6%B0%A3&oq=%E5%A4%A9%E6%B0%A3&aqs=chrome..69i57j0i131i433i512j46i433i512j0i131i433i512l3j0i131i433j69i61.3697j1j7&sourceid=chrome&ie=UTF-8")
        self.go_back()
        
    def is_going_to_cat(self, event):
        text = event.message.text
        return text.lower() == "貓咪"
    
    def on_enter_cat(self, event):
        print("I'm entering cat")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.youtube.com/results?search_query=%E8%B2%93%E5%92%AA%E5%BD%B1%E7%89%87")
        self.go_back()
        
    def is_going_to_eat(self, event):
        text = event.message.text
        return text.lower() == "吃飯"
    
    def on_enter_eat(self, event):
        title = '請選擇想吃的類型\n輸入"start"可回到初始頁面'
        text = '輸入"飯"可看飯類\n輸入"麵"可看麵類\n輸入"水餃"可看餃類'
        btn = [
            MessageTemplateAction(
                label = '飯',
                text ='飯'
            ),
            MessageTemplateAction(
                label = '麵',
                text = '麵'
            ),
            MessageTemplateAction(
                label = '水餃',
                text = '水餃'
            ),
            MessageTemplateAction(
                label = 'start',
                text = 'start'
            ),
        ]
        url = 'https://ideapit.com/article/img/201511/14484612361.gif'
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_rice(self, event):
        text = event.message.text
        return text.lower() == "飯"
    
    def on_enter_rice(self, event):
        print("I'm entering rice")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com.tw/maps/search/%E9%A3%AF/@22.998014,120.2236654,14.75z?hl=zh-TW&authuser=0")
        self.go_back()
        
    def is_going_to_noodle(self, event):
        text = event.message.text
        return text.lower() == "麵"
    
    def on_enter_noodle(self, event):
        print("I'm entering noodle")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com.tw/maps/search/%E9%BA%B5/@22.9980601,120.2236654,14z/data=!3m1!4b1?hl=zh-TW&authuser=0")
        self.go_back()
        
    def is_going_to_dumpling(self, event):
        text = event.message.text
        return text.lower() == "水餃"
    
    def on_enter_dumpling(self, event):
        print("I'm entering dumpling")

        reply_token = event.reply_token
        send_text_message(reply_token, "https://www.google.com.tw/maps/search/%E6%B0%B4%E9%A4%83/@22.9981372,120.2236654,14z/data=!3m1!4b1?hl=zh-TW&authuser=0")
        self.go_back()
        
        
