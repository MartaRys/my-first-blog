from django.contrib import admin
from .models import Post

#polecenie rejestracji modelu, żeby był widoczny w panelu admina :

# Register your models here.
admin.site.register(Post)