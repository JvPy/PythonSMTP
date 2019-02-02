import smtplib
from email.mime.text import MIMEText

fromaddr = 'bar@foo.com'

with open('emails.txt') as f:
    for line in f:
        toaddrs = line
        print '[*]Sending email to ' + toaddrs + '',

        fp = open('email.html', 'rb')
        msg = MIMEText(fp.read(), 'html')
        fp.close
        msg['Subject'] = 'Mail subject'
        msg['From'] = fromaddr
        msg['To'] = toaddrs

        try:
            username = 'userbar'
            password = 'passwordbar'
            server = smtplib.SMTP('smtp.foo.com', 587)
            server.ehlo()
            server.starttls()
            server.login(username,password)
            server.sendmail(fromaddr, toaddrs, msg.as_string())
            server.quit()
            print '[+]Email send to ' + toaddrs
        except:
            print '[-]Email send failed to ' + toaddrs
