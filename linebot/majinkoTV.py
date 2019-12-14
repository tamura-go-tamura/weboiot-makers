from flask import Flask,request,abort
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage,BeaconEvent
import os
import motor

app=Flask(__name__)
#環境変数の取得
YOUR_CHANNEL_ACCESS_TOKEN=""
YOUR_CHANNEL_SECRET=""

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



@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    text = event.text

    if text == "あけ"：
        motor.motor("open")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

    elif text == "しめ":
        motor.motor("close")
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))

    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))



@handler.add(BeaconEvent)
def handle_beacon(event):
    #print(event.source.userid)
    motor.motor("open")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(
            text='Got beacon event. hwid={}, device_message(hex string)={}, event_type={}'.format(
                event.beacon.hwid, event.beacon.dm, event.beacon.type)))


if __name__=="__main__":
    port=int(os.getenv("PORT",5000))
    app.debug=True
    app.run()#host="0.0.0.0",port=port)
