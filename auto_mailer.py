import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Apni Details Yahan Bharein
SENDER_EMAIL = "aapka-email@gmail.com"
SENDER_PASSWORD = "xxxx xxxx xxxx xxxx" # Google App Password

def send_bulk_email(recipient_list, subject, message_body):
    try:
        # SMTP Setup
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        for email in recipient_list:
            msg = MIMEMultipart()
            msg['From'] = SENDER_EMAIL
            msg['To'] = email
            msg['Subject'] = subject
            msg.attach(MIMEText(message_body, 'plain'))
            
            server.sendmail(SENDER_EMAIL, email, msg.as_string())
            print(f"✅ Email sent to: {email}")

        server.quit()
        print("\n✨ Mission Successful: All emails sent!")
    except Exception as e:
        print(f"❌ Error: {e}")

# Run karne ke liye
if __name__ == "__main__":
    targets = ["test1@gmail.com", "test2@gmail.com"] # List of emails
    send_bulk_email(targets, "Hello from Python", "Ye ek automated email hai.")