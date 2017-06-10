from django.contrib import admin
from zhidaily.models import *

# Register your models here.
# 库中超级用户名密码: Admin/Admin123456

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Best)
admin.site.register(UserProfile)
admin.site.register(Comment)
