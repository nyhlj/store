import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.application import MIMEApplication

def send_email(smtpHost,port, sendAddr, password, recipientAddrs, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'html', 'utf-8')
    msg.attach(txt)
    part = MIMEApplication(open(r'C:\Users\29406\Desktop\1\计算器.html','rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="计算器.html")
    msg.attach(part)
    smtp = smtplib.SMTP_SSL(smtpHost, port)
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs.split(";"), str(msg))
    print("发送成功！")
    smtp.quit()

if __name__ == "__main__":
    try:
        smtpHost = 'smtp.qq.com'
        port = 465
        sendAddr ='2940637357@qq.com'
        password = 'swgemcjcuxvhdcec'
        recipientAddrs = '2431320433@qq.com'
        subject='python test from yangjian'
        content='测试报告'
        send_email(smtpHost, port, sendAddr, password, recipientAddrs, subject, content)
    except Exception as err:
        print(err)