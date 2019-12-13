from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage,BeaconEvent
import os

app=Flask(__name__)
#環境変数の取得
YOUR_CHANNEL_ACCESS_TOKEN="8hEM97sJovHOEVuNhHUSbvA819D+HTa6GQ2qFrUbuyVU37GthqeN7S/u/V155tCO2D+NVy1YnVtwjte8/vufThjM6Pc53bc24XyftKnbukrhy0hgsD3RQqaH0R8KKm81R/Ir5YSzhyiz0zi2vmF5CAdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET="ecf2386eeb9fb34c9fac80e0cb96ae5a"

line_bot_api=LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler=WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback",methods=["POST"])
def callback():
    signature=request.headers["X-Line-Signature"]

    body=request.get_data(as_text=True)
    app.logger.info("Request body"+body)

    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


@app.route("/",methods=["POST","GET"])
def maijinko():
    return "majinkoTV~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
    return "majinkoTV????"


@handler.add(BeaconEvent)
def handle_beacon(event):
    #print(event.source.userid)
    #モータを動かす関数を実行
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got beacon event. hwid={}, device_message(hex string)={}, event_type={}'.format(
                event.beacon.hwid, event.beacon.dm, event.beacon.type)))


if __name__=="__main__":
    port=int(os.getenv("PORT",5000))
    app.debug=True
    app.run()#host="0.0.0.0",port=port)
