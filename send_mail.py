import sys
import smtplib
import traceback
from config import sebi_config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from functions import get_data_count, send_mail
from log import log

def send_email(subject, message):
    try:
        # Email configuration
        sender_email = 'probepoc2023@gmail.com'
        receiver_email = 'probepoc2023@gmail.com'
        password = 'rovqljwppgraopla'  

        # Email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"Manual intervention required for {subject}"
        msg.attach(MIMEText(str(message), 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)

    except Exception as e:
        sebi_config.log_list[1] = "Failure"
        sebi_config.log_list[4] = get_data_count.get_data_count(sebi_config.log_cursor)
        sebi_config.log_list[5] = "error in insert part"
        print(sebi_config.log_list)
        log.insert_log_into_table(sebi_config.log_cursor, sebi_config.log_list)
        sebi_config.connection1.commit()
        sebi_config.log_list = [None] * 8
        traceback.print_exc()
        sys.exit("script error")
