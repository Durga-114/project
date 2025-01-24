import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  
EMAIL_ADDRESS = "durgasri3114@gmail.com"  
EMAIL_PASSWORD = "ddyj tzmh xmfe bgrd"  
MENTOR_EMAIL = "springboardmentor543@gmail.com"  

def send_email_notification(subject, review, sentiment, next_steps, area_responsible):
    try:
      
        message = (
            f"🚨 Negative Feedback Alert \n"
            f"📢 *Review:* {review}\n"
            f"🔍 *Sentiment:* {sentiment}\n"
            f"📋 *Next Steps:* {next_steps}\n"
            f"🏢 *Area Responsible:* {area_responsible}\n"
        )
        
        # Setup email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = MENTOR_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Email notification sent successfully!")
    except Exception as e:
        print(f"Error sending email notification: {e}")

if __name__ == "__main__":
    review = "The food served at the buffet was cold and lacked flavor."
    sentiment = "Negative sentiment detected."
    next_steps = "Ensure proper heating of dishes before serving."
    area_responsible = "Dining Services"
    email_subject = "Alert: Negative Guest Feedback"
    send_email_notification(email_subject, review, sentiment, next_steps, area_responsible)
