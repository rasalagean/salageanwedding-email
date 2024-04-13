from http import HTTPStatus
import os
from mailersend import emails

def main(args):
    '''
    Takes in the email address, subject, and message to send an email using SendGrid, 
    returns a json response letting the user know if the email sent or failed to send.

        Parameters:
            args: Contains the from email address, to email address, subject and message to send

        Returns:
            json body: Json response if the email sent successfully or if an error happened
    '''
    print(args)
    key = os.getenv('API_KEY')
    user_from = args.get("from")
    user_to = args.get("to")
    content = args.get("content")

    if not user_from:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no user email provided"
        }
    if not user_to:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no receiver email provided"
        }
    if not content:
        return {
            "statusCode" : HTTPStatus.BAD_REQUEST,
            "body" : "no content provided"
        }

    mailer = emails.NewEmail(key)
    mail_body = {}

    mailer.set_mail_from(user_from, mail_body)
    mailer.set_mail_to(user_to, mail_body)
    mailer.set_subject("SalageanWedding RSVP", mail_body)
    mailer.set_plaintext_content(content, mail_body)

    print(mailer.send(mail_body))

    return {
        "statusCode" : HTTPStatus.ACCEPTED,
        "body" : {"msg": "success"}
    }