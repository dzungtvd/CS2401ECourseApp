from django.contrib import admin
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Course, Lesson, Tag

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'

class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ['id','subject','active','created_date','updated_date']
    search_fields = ['subject', 'context']
    list_filter = ['id','subject','created_date']

    def image_view(self, lesson):
        return mark_safe(f'<img src="/static/{lesson.image.name}" />')

    class Media:
        css = {
            'all': ('/static/css/styles.css',)
        }

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
