from abc import ABC, abstractmethod
class Notification:

    def send(self,message_type:str, message:str):
        if message_type == "email":
            print(f"Sent email with message: {message}")
        elif message_type == "sms":
            print(f"Sent SMS with message: {message}")
        elif message_type == "push":
            print(f"Sent push notification with message: {message}")

# Instantiate the class
notification = Notification()
notification.send("email", "This is an email message")
notification.send("sms", "This is an SMS message")
notification.send("push", "This is a push notification message")

# with OCP
class Notification(ABC):
    @abstractmethod
    def send(self,message_type:str):
        pass

class EmailNotification(Notification):
    def send(self,message:str):
        print(f"Sent email with message: {message}")

class SMSNotification(Notification):
    def send(self,message:str):
        print(f"Sent SMS with message: {message}")

class PushNotification(Notification):
    def send(self,message:str):
        print(f"Sent push notification with message: {message}")

email_notification = EmailNotification()
email_notification.send("This is an email message")
sms_notification = SMSNotification()
sms_notification.send("This is an SMS message")
push_notification = PushNotification()
push_notification.send("This is a push notification message")
