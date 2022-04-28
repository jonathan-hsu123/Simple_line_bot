# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import os
import sys
from argparse import ArgumentParser

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from pip import main
app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = '3ded155c6c5173c8dad1b247fa2bf764'
channel_access_token = 'min8EFJf+Ed4ICtUXjPzMkiKn7Xb/2My/KY4jowW6Djc2WteyNP2nxkutVpUjr54j8BS/m4uPGQCcq76KrjSI1IBaLJorcXQuxQJw9HESYTb5fKG7n6vDIoGSp3O6OxkClBVup1BAc52PFAzannmEQdB04t89/1O/w1cDnyilFU='

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

my_background_a = """Hello, my name is Jonathan Hsu, and I am a 22-year-old student in the Computer Science and Information Engineering department. I am an outgoing person with extensive experience in a variety of areas, including serving as president of the NTU Cocktail Club, competing in business competitions, and even selling on an e-commerce platform."""
my_background_b = """I enjoy taking on new challenges and am always looking for fresh ways to liven up my life. I have a strong experience in programming and data engineering, as evidenced by my good GPA. I'm also working on a number of interesting projects and studies. If you'd want to learn more about me, use the other buttons to do so!"""
GPA = "I achieved an amazing major GPA of 4.22 because I am really interested in Computer Science and study very hard. Many of my classes, such as Algorithm, System Programming, Machine Learning, and others, had good grades, and I believe that detailed training in those courses contributed to my development as an engineer. Later, I worked as a teaching assistant for the Data Structure and Algorithm classes."
data_impute = "Data Imputation was my first MSLAB project; it tries to impute Not Randomly Missing Data for a financial company's credit card records so that they may use their classification model to better accurately anticipate the risk of default. This is the first time I've met real-world data in a machine learning challenge, and I've found that processing this relevant data is quite interesting. Despite the fact that this project did not turn out well, I learned a lot from it."
AutoML = "AutoML is a project that aims to eliminate human involvement in model training by employing an automatic machine learning process. We discover in the survey phase of this study that state-of-the-art AutoML articles rarely focus on feature engineering. As a result, our study focuses on the impact of feature engineering on AutoML. Despite the fact that we discovered that the effect of feature engineering is highly dependent on the dataset, this project provided me with valuable data processing skills."
ChatBot = "ChatBot is a work-in-progress that aims to develop a chatbot flow recommendation system for various clients based on their company goals and industry. We are still in the early stages of development, thus we are primarily concerned with determining the relevance of a single module in a flow and the flow's aim. This is by far my favorite project in MSLAB because I am very interested in recommendation systems and NLP."
IR_proj = "This is my final project from a year ago for an information retrieval class in which I worked with my classmates. We learned a typical vector space model for retrieval and wanted to see if adding a natural language processing model may improve performance. The experiment results are surprisingly good, and we can back up some of them with the publications we looked at."
backtest = "When Pandemic struck last summer, my friends and I devised a stock backtesting technique, which was overseen by a quantitative analyst. In this project, we create a program that can perform backtesting on the Taiwan stock market using various techniques and parameters. In this project, we learned how to correctly build and deploy a program, and gaining a wealth of financial knowledge from our supervisor."
Horoscope = "This is a project I'm working on that seeks to provide horoscope results using NLP models. I'm currently collecting training data, but I'm hoping to launch this website this summer."
club = "In my sophomore year, I was the president of the NTU Cocktail Club. As the club's head, I not only learned a lot about drinking culture, but I also passed that knowledge on to the people who came to our events. In addition, this club provided me with valuable communication and leadership experience."
business_compet = "Last summer, I competed in a Shopee business competition. The purpose of this competition is to increase the number of people who watch Shopee Live, an E-commerce live streaming service. In this tournament, my peers and I placed in the top 25. The most important thing I learnt in this competition is how business managers evaluate whether or not to develop a software service, and it's also a lot of fun."
music = "I enjoy music and listen to more than four new albums per week. I have a wide range of musical tastes, so I can always discover something new to enjoy. \"Melt My Eyez See Your Future,\" by Florida rapper Denzel Curry, is my favorite album of the year."
pokemon = "I began collecting Pokemon cards last year because sorting and collecting these trading cards makes me feel really comfortable. My favorite Pokemon card collection is \"The Scream Collection,\" which was released in 2018."

main_menu = TemplateSendMessage(
    alt_text='menu',
    template=ButtonsTemplate(
        title='Menu',
        text='Now is the prime time of my life.',
        actions=[
            PostbackAction(
                label='About me',
                data="profile menu"
            ),
            PostbackAction(
                label='My studies',
                data="study menu"
            ),
            PostbackAction(
                label='My life',
                data="life menu"
            ),
            PostbackAction(
                label='Contact me',
                data="url menu"
            )
        ]
    )             
)
start_button = TemplateSendMessage(
    alt_text='開始',
    template=ButtonsTemplate(
        title='Get started',
        text='開始認識Jonathan!',
        actions=[
            PostbackAction(
                label='Start',
                data="main menu"
            )
        ]
    )
)
return_menu = TemplateSendMessage(
    alt_text='Return to menu',
    template=ButtonsTemplate(
        title='Return to menu',
        text='This is the end of the story.',
        actions=[
            PostbackAction(
                label='Return to menu',
                data="main menu"
            )
        ]
    )
)
study_menu = TemplateSendMessage(
    alt_text='My studies',
    template=ButtonsTemplate(
        title='My studies',
        text='What I do in NTU.',
        actions=[
            PostbackAction(
                label='Major subjects',
                data="major"
            ),
            PostbackAction(
                label='MSLAB',
                data="MSLAB"
            ),
            PostbackAction(
                label='Projects',
                data="project"
            ),
            PostbackAction(
                label='Return to menu',
                data="main menu"
            )
        ]
    )
)
MSLAB_menu = TemplateSendMessage(
    alt_text='MSLAB',
    template=ButtonsTemplate(
        title='My projects in MSLAB',
        text='Machine Discovery and Social Network Mining Lab.',
        actions=[
            PostbackAction(
                label='Data imputation',
                data="data_impute"
            ),
            PostbackAction(
                label='AutoML',
                data="AutoML"
            ),
            PostbackAction(
                label='Chat bot',
                data="ChatBot"
            ),
            PostbackAction(
                label='Return to My Studies',
                data="study menu"
            )
        ]
    )
)
project_menu = TemplateSendMessage(
    alt_text='My projects',
    template=ButtonsTemplate(
        title='My side/in-class projects',
        text='What I did when I am free(not often).',
        actions=[
            PostbackAction(
                label='DRMM in IR',
                data="IR_proj"
            ),
            PostbackAction(
                label='Stock backtesting',
                data="backtest"
            ),
            PostbackAction(
                label='Horoscope NLP',
                data="Horoscope"
            ),
            PostbackAction(
                label='Return to menu',
                data="study menu"
            )
        ]
    )
)
return_study = TemplateSendMessage(
    alt_text='Return to menu',
    template=ButtonsTemplate(
        title='Return to menu',
        text='This is the end of the story.',
        actions=[
            PostbackAction(
                label='Return to menu',
                data="study menu"
            )
        ]
    )
)
return_MSLAB = TemplateSendMessage(
    alt_text='Return to menu',
    template=ButtonsTemplate(
        title='Return to menu',
        text='This is the end of the story.',
        actions=[
            PostbackAction(
                label='Return to MSLAB',
                data="MSLAB"
            )
        ]
    )
)
return_project = TemplateSendMessage(
    alt_text='Return to menu',
    template=ButtonsTemplate(
        title='Return to menu',
        text='This is the end of the story.',
        actions=[
            PostbackAction(
                label='Return to menu',
                data="project"
            )
        ]
    )
)
life_menu = TemplateSendMessage(
    alt_text='My life',
    template=ButtonsTemplate(
        title='My life',
        text='I took the one less traveled by.',
        actions=[
            PostbackAction(
                label='Club',
                data="club"
            ),
            PostbackAction(
                label='Business competition',
                data="business_compet"
            ),
            PostbackAction(
                label='Hobbies',
                data="hobby"
            ),
            PostbackAction(
                label='Return to menu',
                data="main menu"
            )
        ]
    )
)
hobby_menu = TemplateSendMessage(
    alt_text='My hobbies',
    template=ButtonsTemplate(
        title='My hobbies',
        text='I love it.',
        actions=[
            PostbackAction(
                label='Music',
                data="music"
            ),
            PostbackAction(
                label='Pokemon',
                data="pokemon"
            ),
            PostbackAction(
                label='Return to Life',
                data="life menu"
            )
        ]
    )
)
return_life = TemplateSendMessage(
    alt_text='Return to menu',
    template=ButtonsTemplate(
        title='Return to menu',
        text='This is the end of the story.',
        actions=[
            PostbackAction(
                label='Return to My Life',
                data="life menu"
            )
        ]
    )
)
return_hobby = TemplateSendMessage(
    alt_text='Return to menu',
    template=ButtonsTemplate(
        title='Return to menu',
        text='This is the end of the story.',
        actions=[
            PostbackAction(
                label='Return to menu',
                data="hobby"
            )
        ]
    )
)
url_menu = TemplateSendMessage(
    alt_text='URLs',
    template=ButtonsTemplate(
        title='Contact',
        text='Contact me via these methods!',
        actions=[
            URIAction(
                label='Github',
                uri="https://github.com/jonathan-hsu123"
            ),
            URIAction(
                label='LinkedIn',
                uri="https://www.linkedin.com/in/jonathan-hsu-697a71171/"
            ),
            URIAction(
                label='Email',
                uri="mailto:jonathanhsu8924@gmail.com"
            ),
            PostbackAction(
                label='Return to menu',
                data="main menu"
            )
        ]
    )
)



@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(FollowEvent)
def handle_follow(event):
    if isinstance(event.source, SourceUser):
        profile = line_bot_api.get_profile(event.source.user_id)
        line_bot_api.reply_message(
            event.reply_token, [
                TextSendMessage(text= "歡迎" + profile.display_name + "加入，這裡可以知道很多Jonathan的資訊!"),
                start_button
            ]
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text="歡迎加入，這裡可以知道很多Jonathan的資訊!"),
                start_button
            ]
        )

@handler.add(PostbackEvent)
def handle_postback(event):
    print(event.postback)
    if event.postback.data == 'main menu':
        line_bot_api.reply_message(
            event.reply_token,[
                main_menu
            ]
        )
    elif event.postback.data == 'profile menu':
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=my_background_a),
                TextSendMessage(text=my_background_b),
                return_menu
            ]
        )
    elif event.postback.data == 'study menu':
        line_bot_api.reply_message(
            event.reply_token,[
                study_menu
            ]
        )
    elif event.postback.data == 'major':
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=GPA),
                return_study
            ]
        )
    elif event.postback.data == 'MSLAB':
        line_bot_api.reply_message(
            event.reply_token,[
                MSLAB_menu
            ]
        )
    elif event.postback.data == 'data_impute':
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=data_impute),
                return_MSLAB
            ]
        )
    elif event.postback.data == 'AutoML':
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=AutoML),
                return_MSLAB
            ]
        )
    elif event.postback.data == 'ChatBot':
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=ChatBot),
                return_MSLAB
            ]
        )
    elif event.postback.data == 'project':
        line_bot_api.reply_message(
            event.reply_token,[
                project_menu
            ]
        )
    elif event.postback.data == 'IR_proj':
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=IR_proj),
                return_project
            ]
        )
    elif event.postback.data == 'backtest':
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=backtest),
                return_project
            ]
        )
    elif event.postback.data == 'Horoscope':
        line_bot_api.reply_message(
            event.reply_token,[
                TextSendMessage(text=Horoscope),
                return_project
            ]
        )
    elif event.postback.data == 'life menu':
        line_bot_api.reply_message(
            event.reply_token,[
                life_menu
            ]
        )
    elif event.postback.data == 'club':
        line_bot_api.reply_message(
            event.reply_token,[
                ImageSendMessage(request.url_root + '/static/club.jpg', request.url_root + '/static/club.jpg'),
                TextSendMessage(text=club),
                return_life
            ]
        )
    elif event.postback.data == 'business_compet':
        line_bot_api.reply_message(
            event.reply_token,[
                ImageSendMessage(request.url_root + '/static/shopee.jpg', request.url_root + '/static/shopee.jpg'),
                TextSendMessage(text=business_compet),
                return_life
            ]
        )
    elif event.postback.data == 'hobby':
        line_bot_api.reply_message(
            event.reply_token,[
                hobby_menu
            ]
        )
    elif event.postback.data == 'music':
        line_bot_api.reply_message(
            event.reply_token,[
                ImageSendMessage(request.url_root + '/static/music.jpg', request.url_root + '/static/music.jpg'),
                TextSendMessage(text=music),
                return_hobby
            ]
        )
    elif event.postback.data == 'pokemon':
        line_bot_api.reply_message(
            event.reply_token,[
                ImageSendMessage(request.url_root + '/static/pokemon.jpg', request.url_root + '/static/pokemon.jpg'),
                TextSendMessage(text=pokemon),
                return_hobby
            ]
        )
    elif event.postback.data == 'url menu':
        line_bot_api.reply_message(
            event.reply_token,[
                url_menu
            ]
        )
    
    
        

@handler.add(MessageEvent, message=TextMessage)
def message_text(event):
    text_massage = event.message.text
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )


if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    )
    arg_parser.add_argument('-p', '--port', default=8000, help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)