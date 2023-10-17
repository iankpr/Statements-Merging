import pandas as pd
import win32com.client
import os

df = pd.read_excel('database.csv')
df['pay_by'] = df['pay_by'].dt.strftime('%B %d, %Y')


# Get the email address and password for sending emails
email_address = "your_email@example.com"  # Replace with your email address
email_password = "your_password"  # Replace with your email password

for r in df.itertuples():
    name = r[1]
    plural = r[2]
    date = r[3]
    property = r[4]
    email = r.email

    msg = f"""
Dear {name},

Trust this email finds you well.

Kindly find attached Statement of Account for your {plural} as of {date}.

Thank you so much,
Kennedy Property Rentals L.L.C.

"""
    print(msg)

#To use Outlook Email

def send_outlook(msg, property, to_address):
    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.To = to_address
    mail.Subject = f'Statement of Account - {property} - {date}'
    mail.Body = msg
    #mail.Attachments.Add(attachment)
    attachment_path = 'path_to_attachment.pdf'
    if os.path.exists(attachment_path):
        mail.Attachments.Add(attachment_path)

    # Send the email using your email address and password
    mail.SendUsingAccount = outlook.Session.Accounts(email_address)
    mail.Send()

# Please note that you need to replace "your_email@example.com" and "your_password" with your actual email address and password. 
#     It's essential to ensure that you use a dedicated email account for sending automated emails and not your personal email account, 
#       as it may require special settings to allow automated access. 
# Additionally, you need to replace 'path_to_attachment.pdf' with the actual file path of the attachment you want to send.
