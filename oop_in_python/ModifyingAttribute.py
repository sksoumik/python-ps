"""
 we can change the value of attributes based on some behavior
"""


class Email:
    def __init__(self):
        self.is_sent = False

    def send_mail(self):
        self.is_sent = True


my_email = Email()
print(my_email.is_sent)

my_email.send_mail()
print(my_email.is_sent)
