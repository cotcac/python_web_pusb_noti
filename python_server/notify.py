from pywebpush import webpush, WebPushException
info1={
        "endpoint":"https://fcm.googleapis.com/fcm/send/whGH...",
        "expirationTime":None,
        "keys":{
        "p256dh":"8Tu2fdazh9kJSekw...",
        "auth":"S61a2bw..."}
        }
try:
    webpush(
        subscription_info=info1,
        data="Mary had a little lamb, with a nice mint jelly",
        vapid_private_key="IBCme...",
        vapid_claims={
                "sub": "mailto:YourNameHere@example.org",
            }
    )
except WebPushException as ex:
    print("I'm sorry, Dave, but I can't do that: {}", repr(ex))
    # Mozilla returns additional information in the body of the response.
    if ex.response and ex.response.json():
        extra = ex.response.json()
        print("Remote service replied with a {}:{}, {}",
              extra.code,
              extra.errno,
              extra.message
              )