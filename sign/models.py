from django.db import models

# Create your models here.

#创建表模型

#发布会
class Event(models.Model):
    name = models.CharField(max_length=100)  # 发布会的标题
    limit = models.ImageField()  # 参加人数
    statys = models.BooleanField()  # 签到的状态
    address = models.CharField(max_length=100) # 地址
    start_time = models.DateTimeField("events time")  # 发布会时间
    create_time = models.DateTimeField(auto_now=True) #创建时间(自动获取当前时间)


# 只返回显示名字
    def __str__(self):
        return self.name

# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event)  # 关联发布会ID
    realname = models.CharField(max_length=64) # 姓名
    phone = models.CharField(max_length=16) # 电话
    email = models.EmailField()  # 邮箱
    sign = models.BooleanField() # 签到状态
    create_time = models.DateTimeField(auto_now=True)  #创建时间(自动获取当前时间)


class Meta:
    unique_together = ("event","phone")


# 只显示用户的名字
def __str__(self):
    return self.realname

















