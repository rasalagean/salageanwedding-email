from http import HTTPStatus
import os
import requests

def main(args):
    '''
    Takes in the email address, subject, and message to send an email using SendGrid, 
    returns a json response letting the user know if the email sent or failed to send.

        Parameters:
            args: Contains the from email address, to email address, subject and message to send

        Returns:
            json body: Json response if the email sent successfully or if an error happened
    '''
    key = os.getenv('API_KEY')
    domain = os.getenv('DOMAIN')
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

    return requests.post(
            f"https://api.mailgun.net/v3/{domain}/messages",
            auth=("api", key),
            data={"from": f"{user_from} <{domain}>",
                "to": [user_to],
                "subject": "SalageanWedding RSVP",
                "text": content})