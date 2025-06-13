import smtplib

conn=smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()
conn.login('naiktejas1993@gmail.com', 'yeshwantrao841993')

conn.sendmail('naiktejas1993@gmail', 'yashtnaik@gmail.com', 'Subject: test \n\nDear Yash this is a test mail \n\nThanks and regards')
conn.quit()