from django.contrib import admin
from app.AboutAcademy.models import *
from app.AboutAcademy.translation import *
from modeltranslation.admin import TranslationAdmin
from django.forms import ModelForm, BaseInlineFormSet
# Register your models here.
class AboutUsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru',  'title_phone_number_ru', 'phone_number_ru', 'title_adress_ru', 'adress_ru', 'title_operating_mode_ru', 'operating_mode_ru', 'link_map_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky',  'title_adress_ky', 'adress_ky', 'title_operating_mode_ky', 'operating_mode_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en',  'title_adress_en', 'adress_en', 'title_operating_mode_en', 'operating_mode_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar',  'title_adress_ar', 'adress_ar', 'title_operating_mode_ar', 'operating_mode_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr',  'title_adress_tr', 'adress_tr', 'title_operating_mode_tr', 'operating_mode_tr'],
        }),
    )
admin.site.register(AboutUs, AboutUsAdmin)

class DevStrategyAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
    )
admin.site.register(DevStrategy, DevStrategyAdmin)

class DevStrategyPhotoAdmin(admin.ModelAdmin):
        fieldsets = (
        ('Фотогравия', {
            'fields': ['photo', ],
        }),
        )
admin.site.register(DevStrategyPhoto, DevStrategyPhotoAdmin)

class MissionAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
    )
admin.site.register(Mission, MissionAdmin)

class DocumentAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'file_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', ],
        }),
        ('Английский версия', {
            'fields': ['title_en', ],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', ],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', ],
        }),
    )
admin.site.register(Document, DocumentAdmin)

class AchievementsAdmin(TranslationAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
    )
admin.site.register(Achievements, AchievementsAdmin)

class HistoryObjectInlineFormSet(BaseInlineFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        if index is not None and index > 0:
            form.fields['image'].widget = admin.widgets.AdminFileWidget(attrs={'style': 'display:none;'})
            form.fields['image'].required = False

class NewsObjectInline(admin.TabularInline):
    model = HistoryObject 
    formset = HistoryObjectInlineFormSet
    extra = 1

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if qs.exists():
            first_object = qs.first()
            return qs.exclude(id=first_object.id)
        return qs

    def get_fieldsets(self, request, obj=None):
        return (
            ('Изображение', {
                'fields': ('image',),
            }),
        )
    
class HistoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Русская версия', {
            'fields': ['title_ru', 'description_ru'],
        }),
        ('Кыргызская версия', {
            'fields': ['title_ky', 'description_ky'],
        }),
        ('Английский версия', {
            'fields': ['title_en', 'description_en'],
        }),
        ('Арабский версия', {
            'fields': ['title_ar', 'description_ar'],
        }),
        ('Турецкий версия', {
            'fields': ['title_tr', 'description_tr'],
        }),
    )
    inlines = [NewsObjectInline] 

admin.site.register(History, HistoryAdmin)
