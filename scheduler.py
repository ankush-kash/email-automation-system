import schedule
import time


from sender import send_email

def job():
    send_email(
    receiver='ankushkash98@gmail.com',
    subject='Daily Remainder',
    body = 'India become no.1 in tech field in 2035',
    attachment_path='attachments/save.pdf'
    )

schedule.every(1).minutes.do(job)

print('Schedule started...............')

while True:

    schedule.run_pending()

    time.sleep(1)

