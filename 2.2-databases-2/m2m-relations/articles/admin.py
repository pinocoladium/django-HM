from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if form.cleaned_data['is_main']:
                count += 1
            if count > 1:
                raise ValidationError('Основной раздел может быть только один')
            elif count == 0:
                raise ValidationError('Нет основного раздела')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]