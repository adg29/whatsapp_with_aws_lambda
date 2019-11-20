from twilio.rest import Client

def msg_mom_and_dad(event=None, context=None):
    # get twilio sid and auth token
    twilio_sid = 'AC84c9f1602d7fb6af4eda5b0c39a03b37'
    auth_token = '4a2021b28f1aa606d9c6945d3c248ebd'

    whatsapp_client = Client(twilio_sid, auth_token)

    contact_directory = {
        'dad': '+913053383064'
    }

    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
            body = 'good morning {} !'.format(key),
            from_= 'whatsapp: +14155238886',
            to= 'whatsapp:' + value
        )

        print(msg_loved_ones.sid)