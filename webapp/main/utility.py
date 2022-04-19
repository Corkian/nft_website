from flask_mail import Message, Mail


from webapp import mail


def sendContactForm(result):
    msg = Message("Contact Form GT",
                  sender='info@generation-team.com',
                  recipients=["info@generation-team.com"])

    msg.body = """
    Hello there,

    You just received a contact form from Generation Team.

    Name: {}
    Email: {}
    Message: {}

    """.format(result['name'], result['email'], result['message'])

    mail.send(msg)
    return "Mail sent"