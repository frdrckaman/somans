from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import pandas as pd
import io
import os
import smtplib


def export_excel(df):
    with io.BytesIO() as buffer:
        with pd.ExcelWriter(buffer) as writer:
            df.to_excel(writer)
        return buffer.getvalue()


def send_mail1(from_email, to_email, subject, body, data=None):
    multipart = MIMEMultipart()

    multipart['From'] = from_email
    multipart['To'] = to_email
    multipart['Subject'] = subject
    attachment = MIMEApplication(export_excel(data))
    filename = 'dataframe.xlsx'
    attachment['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
    multipart.attach(attachment)
    multipart.attach(MIMEText(body, 'html'))

    smtp = smtplib.SMTP('10.144.27.11', 25)
    smtp.sendmail(from_email, to_email, multipart.as_string())
    smtp.quit()


def first_day_previous_month():
    first_day = (datetime.now() - timedelta(days=datetime.now().day)).replace(day=1)
    return first_day.strftime('%Y-%m-%d')


def last_day_previous_month():
    last_day = (datetime.now().replace(day=1) - timedelta(days=1))
    return last_day.strftime('%Y-%m-%d')


def get_data():
    if datetime.today().strftime('%A') == 'Monday':
        start_date = (datetime.now() - timedelta(days=7)).strftime('%d/%B/%Y')
        end_date = datetime.now().strftime('%d/%B/%Y')
        # run_weekly_tasks(start_date, end_date)
    elif datetime.now().day == 1:
        dt1 = datetime.now() + timedelta(days=10)
        start_date = (dt1 - timedelta(days=1)).strftime('%d/%B/%Y')
        end_date = ((dt1 - timedelta(days=1)) - timedelta(days=29)).strftime('%d/%B/%Y')
        # run_monthly_tasks(start_date, end_date)
    else:
        pass
        # run_daily_tasks()
