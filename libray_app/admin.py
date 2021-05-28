from .models import Category, Student, Book,Borrow
from django.contrib import admin

class c_admin(admin.ModelAdmin):
    list_display = ['title']


class s_admin(admin.ModelAdmin):
    list_display = ['student_id', 's_firstname', 's_lastname', 's_year', 's_section']


class b_admin(admin.ModelAdmin):
    fields=('title', 'category', 'author', 'cover', 'available')
    list_display=['title', 'author', 'cover', 'available']
class bo_admin(admin.ModelAdmin):
    list_display = ['book_list','student_list','qty','date','status']



admin.site.register(Student, s_admin)
admin.site.register(Category, c_admin)
admin.site.register(Book, b_admin)
admin.site.register(Borrow,bo_admin)
