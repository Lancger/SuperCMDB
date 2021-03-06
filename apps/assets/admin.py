from django.contrib import admin
from assets.models.book import *
from assets.models.server import *

admin.site.register(Publisher)
admin.site.register(Book)

admin.site.register(Server)
admin.site.register(ServerGroup)
admin.site.register(ServerAuthRule)
admin.site.register(Tag)
admin.site.register(AdminUser)

admin.site.register(Log)
admin.site.register(TtyLog)
admin.site.register(RecorderLog)