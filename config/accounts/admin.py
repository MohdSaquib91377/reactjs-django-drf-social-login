from django.contrib import admin
from accounts import models as accounts_models
# Register your models here.
admin.site.register(accounts_models.Account)