from modeltranslation.translator import register, TranslationOptions
from app.AboutAcademy.models import *

@register(AboutUs)
class AboutUsTranslationOption(TranslationOptions):
    fields = ('title', 'description', 'title_phone_number', 'phone_number', 'title_adress', 'adress', 'title_operating_mode', 'operating_mode', 'link_map')

@register(DevStrategy)
class DevStrategyTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(Mission)
class MissionTranslationOption(TranslationOptions):
    fields = ('title', 'description')

@register(Document)
class DocumentTranslationOption(TranslationOptions):
    fields = ('title','file')

@register(Achievements)
class AchievementsTranslationOption(TranslationOptions):
    fields = ('title','description')

@register(History)
class HistoryTranslationOption(TranslationOptions):
    fields = ('title','description')