from alerts.whatsapp import send_alert

def check_and_send(value):
    if value < 100:
        send_alert(100)
    elif value < 200:
        send_alert(200)