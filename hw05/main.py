import re
s='我的电子邮件tom@gmail.com。将什么发送到jerry123@163.com或者3123432@qq.com.若遇特殊情况请打18222861716'
email1=re.compile(r'^([a-z])+@([a-z])+(.[a-z]+)')
email2=re.compile(r'^[a-z0-9]+@[0-9]+(.[a-z]+)')
email3=re.compile(r'^[0-9]+@[a-z]+(.[a-z]+)')
s1=email1.findall(s)
s2=email2.findall(s)
s3=email3.findall(s)
if email1.findall(s):
    print(s1)
elif email2.findall(s):
    print(s2)
elif email3.findall(s):
    print(s3)
else:
    print('it is phonnumber')
