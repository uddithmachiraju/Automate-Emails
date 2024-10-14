# Automate Emails 📧  
A Python script utilizing SMTP for sending emails with automated attachments, such as cover letters and resumes. It leverages SSL/TLS encryption for secure connections and MIME for handling file attachments. Ideal for job applications or bulk email dispatch.

## Features:
- Send automated emails using **SMTP**.
- Attach files such as **Cover Letter** and **Resume**.
- Secure connections with **SSL/TLS encryption**.
- Easy integration and customization for different use cases (e.g., job applications, bulk emails).

## Prerequisites:
- Python 3.x
- Required Python libraries:
  - `ssl`
  - `smtplib`
  - `email.mime` for building multipart email messages
- Gmail SMTP settings (or any other SMTP server settings):
  - SMTP server: `smtp.gmail.com`
  - Port: `587`

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/uddithmachiraju/Automate-Emails.git

## Usage:
```python
from main import Email

# Initialize Email class
email = Email()

# Define recipient, subject, and message
person = "recipient_email@example.com"
subject = "Important Email"  
message = "This is an Automated Email"

# Send the email
email.send_email(person, subject, message)
