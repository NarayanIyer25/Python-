from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.cliend_id= 'AC18af72981bade760928c2cd8b3181623'
        self.token = 'c9f69878481dd75b589019225a676180'
        self.client = Client(self.cliend_id,self.token)

    def send_message(self,price,from_city,to_city,from_date,to_date):
        self.client.messages.create(from_= , to=,
                                    body=f'sent from your twilio account - low price alert ! only {price} from '
                                         f'{from_city} to {to_city} from {from_date} to {to_date}')