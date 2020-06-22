import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
#import common.config as cf

def send_mail():
mail_host = '192.168.0.211' # 邮箱服务器地址
username = 'mengdewei@zhxht.com' # 邮箱用户名
password = 'mdw@1234' # 邮箱密码
receivers = 'mengdewei@zhxht.com' # 收件人
# 创建一个带附件的实例
message = MIMEMultipart()
 message['From'] = Header(u'检测基础版测试', 'utf-8')
 message['subject'] = Header(u'检测基础版测试结果', 'utf-8') # 邮件标题
message.attach(MIMEText(u'测试结果详见附件', 'plain', 'utf-8'))# 邮件正文
# 构造附件
report_root = cf.get_value('report_path') # 获取报告路径
report_file = 'index.html' # 报告文件名称
att1 = MIMEText(open(report_root + report_file, 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename={}'.format(report_file)
  message.attach(att1)

try:
 smtp = smtplib.SMTP()
 smtp.connect(mail_host, 25) # 25为 SMTP 端口号
 smtp.login(username, password)
  smtp.sendmail(username, receivers, message.as_string())
 print ('邮件发送成功');
except Exception, e:
 print ('邮件发送失败');
raise e