from django.contrib import admin
from .models import *
from solo.admin import SingletonModelAdmin
from django.utils.html import format_html

class SingletonAdmin(admin.ModelAdmin):
    """Базовый класс для моделей, которых должна быть только одна запись."""
    def has_add_permission(self, request):
        return not self.model.objects.exists()


@admin.register(HomePage)
class HomePageAdmin(SingletonModelAdmin):
    list_display = ('hero_title',)

    fieldsets = (
        ('🇺🇦 Українська', {
            'fields': (
                'hero_title',
                'hero_text',
            )
        }),
        ('🇬🇧 English', {
            'fields': (
                'hero_title_en',
                'hero_text_en',
            )
        }),
    )


class ApproachCardPointInline(admin.TabularInline):
    model = ApproachCardPointHomePage
    extra = 1
    fields = (
        'text',
        'text_en',
    )


@admin.register(ApproachCardHomePage)
class ApproachCardHomePageAdmin(admin.ModelAdmin):
    list_display = ('teaser_title',)
    inlines = [ApproachCardPointInline]

    fieldsets = (
        ('🇺🇦 Українська', {
            'fields': (
                'teaser_title',
                'teaser_text',
                'expanded_text_begin',
                'expanded_text_end',
            )
        }),
        ('🇬🇧 English', {
            'fields': (
                'teaser_title_en',
                'teaser_text_en',
                'expanded_text_begin_en',
                'expanded_text_end_en',
            )
        }),
    )


class IndustriesFlatPointInline(admin.TabularInline):
    model = IndustriesFlatPointHomePage
    extra = 1
    fields = (
        'text',
        'text_en',
    )


class IndustriesJobPointInline(admin.TabularInline):
    model = IndustriesJobPointHomePage
    extra = 1
    fields = (
        'text',
        'text_en',
    )


@admin.register(IndustriesHomePage)
class IndustriesHomePageAdmin(SingletonModelAdmin):
    list_display = ('flat_position_title',)
    inlines = [IndustriesFlatPointInline, IndustriesJobPointInline]

    fieldsets = (
        ('🇺🇦 Українська', {
            'fields': (
                'flat_position_title',
                'flat_positon_text',
            )
        }),
        ('🇬🇧 English', {
            'fields': (
                'flat_position_title_en',
                'flat_positon_text_en',
            )
        }),
    )


class CollaborationPointHomePage(admin.TabularInline):
    model = CollaborationPointHomePage
    extra = 1
    fields = (
        'text',
        'text_en',
    )

@admin.register(CollaborationHomePage)
class CollaborationHomePageAdmin(SingletonModelAdmin):
    list_display = ('text',)
    inlines = [CollaborationPointHomePage]

    fieldsets = (
        ('🇺🇦 Українська', {
            'fields': (
                'title',
                'text',
            )
        }),
        ('🇬🇧 English', {
            'fields': (
                'title_en',
                'text_en',
            )
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'email', 'city', 'country', 'created_at')
    list_filter = ('country', 'city')
    search_fields = ('name_surname', 'email')
    readonly_fields = ('created_at', 'ip_address')


@admin.register(AboutPage)
class AboutPageAdmin(SingletonModelAdmin):

    readonly_fields = ('img_preview',)

    fieldsets = (
        ('🇺🇦 Українська', {
            'fields': (
                'label',
                'title',
                'description',
            )
        }),
        ('🇬🇧 English', {
            'fields': (
                'label_en',
                'title_en',
                'description_en',
            )
        }),
        ('Зображення', {
            'fields': (
                'img',
                'img_preview',
            )
        }),
    )

    def img_preview(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="max-height:200px;border-radius:8px;" />',
                obj.img.url
            )
        return 'Зображення не завантажено'

    img_preview.short_description = 'Попередній перегляд'


@admin.register(OurTeamAboutPage)
class OurTeamAboutPageAdmin(admin.ModelAdmin):
    list_display = ('img_thumbnail', 'name_surname', 'profession', 'order')
    list_display_links = ('img_thumbnail', 'name_surname')
    list_editable = ('order',)
    search_fields = ('name_surname', 'profession')
    list_filter = ('profession',)
    ordering = ('order',)

    fields = (
        'img',
        'img_preview',

        'name_surname',

        'profession',
        'profession_en',

        'begin_text',
        'begin_text_en',

        'description',
        'description_en',

        'order',
    )
    readonly_fields = ('img_preview',)

    def img_thumbnail(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="height: 50px; width: 50px; object-fit: cover; border-radius: 50%;" />',
                obj.img.url
            )
        return '—'
    img_thumbnail.short_description = 'Фото'

    def img_preview(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="max-height: 250px; border-radius: 8px;" />',
                obj.img.url
            )
        return 'Зображення не завантажено'
    img_preview.short_description = 'Попередній перегляд'

class PointServicePageAdmin(admin.TabularInline):
    model = PointServicePage
    fields = (
        'text',
        'text_en',
    )

@admin.register(ServicePage)
class ServicePageAdmin(SingletonModelAdmin):

    inlines = [PointServicePageAdmin]

    fieldsets = (
        ('🇺🇦 Українська', {
            'fields': (
                'title',
                'text',
            )
        }),
        ('🇬🇧 English', {
            'fields': (
                'title_en',
                'text_en',
            )
        }),
    )

class SpecialistsPointInline(admin.TabularInline):
    model = SpecialistsPointServicePage
    extra = 1

    fields = (
        'text',
        'text_en',
        'order',
    )

    ordering = ('order',)


@admin.register(SpecialistsServicePage)
class SpecialistsServicePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'conditions', 'order')
    list_editable = ('order',)
    search_fields = ('title',)
    ordering = ('order',)
    inlines = [SpecialistsPointInline]

    fields = (
        'img',

        'title',
        'title_en',

        'text_begin',
        'text_begin_en',

        'conditions',
        'conditions_en',

        'description',
        'description_en',

        'order',
    )


class ServiceProposalPointInline(admin.TabularInline):
    model = ServiceProposalPointServicePage
    extra = 1

    fields = (
        'text',
        'text_en',
        'order',
    )

    ordering = ('order',)


@admin.register(ServiceProposalServicePage)
class ServiceProposalServicePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'position', 'price', 'order', 'preview_img')
    list_display_links = ('title',)
    list_editable = ('order',)
    ordering = ('order',)
    search_fields = ('title', 'position', 'title_main')
    readonly_fields = ('preview_img',)
    inlines = (ServiceProposalPointInline,)

    fieldsets = (

        ('Основне 🇺🇦', {
            'fields': (
                'img',
                'preview_img',

                'position',
                'title',
                'title_text',
                'price',

                'text_begin',
                'text_end',

                'title_main',
                'text_main',

                'order',
            )
        }),

        ('English 🇬🇧', {
            'fields': (
                'position_en',
                'title_en',
                'title_text_en',
                'price_en',

                'text_begin_en',
                'text_end_en',

                'title_main_en',
                'text_main_en',
            )
        }),

    )

    def preview_img(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="max-height:80px; border-radius:6px;" />', obj.img.url)
        return '—'
    preview_img.short_description = 'Прев\'ю'

@admin.register(ContactPage)
class ContactPageAdmin(SingletonModelAdmin):

    fieldsets = (
        ('🇺🇦 Українська', {
            'fields': (
                'title',
                'text',
                'adress',
                'text_under_logo',
                'text_slogan',
            )
        }),
        ('🇬🇧 English', {
            'fields': (
                'title_en',
                'text_en',
                'adress_en',
                'text_under_logo_en',
                'text_slogan_en',
            )
        }),
        ('Контакти', {
            'fields': (
                'number',
                'email',
                'linkedin',
            )
        }),
    )

@admin.register(partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('img_thumbnail', 'link')
    fields = ('link', 'img', 'img_preview')
    readonly_fields = ('img_preview',)

    def img_thumbnail(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="height:40px; width:40px; object-fit:cover; border-radius:6px;" />',
                obj.img.url
            )
        return '—'
    img_thumbnail.short_description = 'Фото'

    def img_preview(self, obj):
        if obj.img:
            return format_html(
                '<img src="{}" style="max-height:200px; border-radius:8px;" />',
                obj.img.url
            )
        return 'Зображення не завантажено'
    img_preview.short_description = 'Попередній перегляд'