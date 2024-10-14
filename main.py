# Simple Mail Transfer Protocol
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

class Email:
    def __init__(self):
        self.port = 587
        self.server = "smtp.gmail.com"
        self._from = "your_email@gmail.com"
        self.passKey = "your_passkey"
        self.email_context = ssl.create_default_context()

    def send_email(self, to, subject, message):
        try:

            # Structure the Email
            msg = MIMEMultipart()
            msg['From'] = self._from
            msg['To'] = to
            msg['subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Add Attachments
            cover_letter = 'CoverLetter.pdf'
            resume = 'Resume.pdf' 

            # Add Attachments to the Email
            cover_letter_attachment = open(cover_letter, 'rb')
            resume_attachment = open(resume, 'rb')

            # For adding Cover Letter
            CLA_package = MIMEBase('application', 'octet-stream')
            CLA_package.set_payload((cover_letter_attachment).read())
            encoders.encode_base64(CLA_package)
            CLA_package.add_header('Content-Disposition', "cover_letter_attachment; filename = " + cover_letter)
            msg.attach(CLA_package)

            # For adding Resume
            RA_package = MIMEBase('application', 'octet-stream')
            RA_package.set_payload((resume_attachment).read())
            encoders.encode_base64(RA_package)
            RA_package.add_header('Content-Disposition', "resume_attachment; filename = " + resume)
            msg.attach(RA_package)

            text = msg.as_string()

            TIE_server = smtplib.SMTP(self.server, self.port)
            TIE_server.starttls(context = self.email_context)
            TIE_server.login(self._from, self.passKey)

            TIE_server.sendmail(self._from, to, text)
            TIE_server.quit()

        except Exception as e:
            return e


