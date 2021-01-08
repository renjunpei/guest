from django.contrib import admin
from sign.models import Event,Guest

# Register your models here.


#  django自带的admin后台增加显示的字段
class EventAdmin(admin.ModelAdmin):
    list_display = ["id","name","statys","address","start_time"]
    search_fields = ["name"]  # 搜索栏
    list_filter = ["statys"]  # 过滤器



class GuestAdmin(admin.ModelAdmin):
    list_display = ["realname","phone","email","sign","create_time","event"]
    search_fields = ["realname","phone"]  # 搜索栏
    list_filter = ["sign"]  # 过滤器


admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)




