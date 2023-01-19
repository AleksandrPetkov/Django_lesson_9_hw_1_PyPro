import sqlite3

from django.core.exceptions import ValidationError


def validate_unique_email(value):
    db_path = '/home/oleksandr/PycharmProjects/Django_lesson_9_hw_1_PyPro/db.sqlite3'
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    db_data = cur.execute('SELECT email FROM students').fetchall()
    connection.close()
    email_list = [email[0] for email in db_data]
    if value in email_list:
        raise ValidationError('This email already is in database')
