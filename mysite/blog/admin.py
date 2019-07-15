from django.contrib import admin

# Register your models here.
# models.pyで自分が定義したモデルをここに追記する
from .models import Post

admin.site.register(Post)
