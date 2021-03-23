import requests

ALERT_URL = 'https://messages-sandbox.nexmo.com/v0.1/messages'

def send_alert(urgency):
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    alert_message_data = {
        'from': {'type': 'whatsapp', 'number': '<alert system>'},
        'to': {'type': 'whatsapp', 'number': '<my number>'},
        'message': {
            'context': {
                'type': 'text',
                'text': f'Warning! The total value of your ETF holdings is under {urgency * 100} Pounds!',  # noqa: 501
            }
        },
    }
    r = requests.post(
        url=ALERT_URL,
        data=alert_message_data,
        auth=('<usname>', '<pw>'),
        headers=headers,
    )
    return r