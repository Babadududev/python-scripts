import datetime
#class to represent an email with sender, receiver, subject, and body
class Email:
    #initialize the email with sender, receiver, subject, and body
    def __init__(self, sender, receiver, subject, body):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.timestamp = datetime.datetime.now()
        self.read = False
    #mark the email as read
    def mark_as_read(self):
        self.read = True
    
    #display the full email content, mark it as read, and print the email details
    def display_full_email(self):
        self.mark_as_read()
        print("\n--- Email ---")
        print(f"From: {self.sender.name}")
        print(f"To: {self.receiver.name}")
        print(f"Subject: {self.subject}")
        print(f"Body: {self.body}")
        print(f"Received at: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print('------------\n')
    #method to return a string representation of the email, indicating whether it has been read or not
    def __str__(self):
        status = "Read" if self.read else "Unread"
        return f" [{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}"
       

#class to represent a user with a name and an inbox for receiving emails
class User:
    #initialize the user with a name and an inbox
    def __init__(self, name):
        self.name = name
        self.inbox = Inbox()
    #method to send an email to another user, creating an Email object and adding it to the receiver's inbox   
    def send_email(self, receiver, subject, body):
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        self.inbox.receive_email(email)
        print(f"Email sent from {self.name} to {receiver.name}!\n")
    #method to check the user's inbox and list all received emails
    def check_inbox(self):
        print(f"{self.name}'s Inbox:")
        self.inbox.list_emails()
    #method to read an email from the user's inbox based on its index
    def read_email(self, index):
        self.inbox.read_email(index)
    #method to delete an email from the user's inbox based on its index
    def delete_email(self, index):
        self.inbox.delete_email(index)           
#class to represent an inbox that can receive and store emails
class Inbox:
    #initialize the inbox with an empty list of emails
    def __init__(self):
        self.emails = []
    #method to receive an email and add it to the inbox
    def receive_email(self, email):
        self.emails.append(email)
    #method to list emails in the inbox.
    def list_emails(self):
        if not self.emails:
            print("Inbox is empty.")
        else:
            for i, email in enumerate(self.emails, start=1):
                print(f"{i}. {email}")
    #method to read an email by index, displaying its full content
    def read_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        self.emails[actual_index].display_full_email()
    #method to delete an email from the inbox based on its index
    def delete_email(self, index):
        if not self.emails:
            print('Inbox is empty.\n')
            return
        actual_index = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        del self.emails[actual_index]
        print('Email deleted.\n')
# main function to demonstrate the email simulator functionality        
def main():
    #create users
    Tife = User("Tife")
    demi = User("demi")
    Tife.send_email(demi, "Hello", "i wan chop ")
    demi.send_email(Tife, "Re: Hello", "na Lore talk am.")

    Tife.read_email(1)
    demi.read_email(1)
if __name__ == "__main__":
    main()
