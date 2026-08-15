from django.db import models
from solo.models import SingletonModel

from .mixins import AutoTranslateMixin


class HomePage(AutoTranslateMixin, SingletonModel):

    TRANSLATABLE_FIELDS = ['hero_title', 'hero_text']

    hero_title = models.CharField(max_length=100, verbose_name='Заголовок головного банера')
    hero_title_en = models.CharField(max_length=100, blank=True)

    hero_text = models.CharField(max_length=200, verbose_name='Інформація головного банера')
    hero_text_en = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Рекрутинг для агробізнесу та суміжних галузей'
        verbose_name_plural = 'Рекрутинг для агробізнесу та суміжних галузей'
        app_label = 'home_page'

    def __str__(self):
        return self.hero_title


class ApproachCardHomePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['teaser_title', 'teaser_text', 'expanded_text_begin', 'expanded_text_end']

    teaser_title = models.CharField(max_length=100, verbose_name='Заголовок картки')
    teaser_title_en = models.CharField(max_length=100, blank=True)

    teaser_text = models.TextField(null=True, blank=True, max_length=200, verbose_name='Короткий текст')
    teaser_text_en = models.TextField(null=True, blank=True, max_length=200)

    expanded_text_begin = models.TextField(null=True, blank=True, max_length=200, verbose_name='Розгорнутий текст (початок)')
    expanded_text_begin_en = models.TextField(null=True, blank=True, max_length=200)

    expanded_text_end = models.TextField(null=True, blank=True, max_length=200, verbose_name='Розгорнутий текст (кінець)')
    expanded_text_end_en = models.TextField(null=True, blank=True, max_length=200)

    class Meta:
        verbose_name = 'Наш підхід'
        verbose_name_plural = 'Наш підхід'
        app_label = 'home_page'

    def __str__(self):
        return self.teaser_title


class ApproachCardPointHomePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['text']

    card = models.ForeignKey(ApproachCardHomePage, on_delete=models.CASCADE, related_name='points', verbose_name='Картка')

    text = models.CharField(max_length=200, verbose_name='Пункт')
    text_en = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Пункт картки підходу'
        verbose_name_plural = 'Пункти картки підходу'
        app_label = 'home_page'

    def __str__(self):
        return self.text


class IndustriesHomePage(AutoTranslateMixin, SingletonModel):

    TRANSLATABLE_FIELDS = ['flat_position_title', 'flat_positon_text']

    flat_position_title = models.CharField(max_length=100, verbose_name='Заголовок блоку індустрій')
    flat_position_title_en = models.CharField(max_length=100, blank=True)

    flat_positon_text = models.TextField(verbose_name='Текст блоку індустрій')
    flat_positon_text_en = models.TextField(blank=True)

    class Meta:
        verbose_name = 'З ким і над чим ми працюємо'
        verbose_name_plural = 'З ким і над чим ми працюємо'
        app_label = 'home_page'

    def __str__(self):
        return self.flat_position_title


class IndustriesFlatPointHomePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['text']

    card = models.ForeignKey(IndustriesHomePage, on_delete=models.CASCADE, related_name='flat_points', verbose_name='Блок індустрій')

    text = models.CharField(max_length=200, verbose_name='Пункт')
    text_en = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Пункт (позиції)'
        verbose_name_plural = 'Пункти (позиції)'
        app_label = 'home_page'

    def __str__(self):
        return self.text


class IndustriesJobPointHomePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['text']

    card = models.ForeignKey(IndustriesHomePage, on_delete=models.CASCADE, related_name='job_points', verbose_name='Блок індустрій')

    text = models.CharField(max_length=200, verbose_name='Пункт')
    text_en = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Пункт (вакансії)'
        verbose_name_plural = 'Пункти (вакансії)'
        app_label = 'home_page'

    def __str__(self):
        return self.text


class CollaborationHomePage(AutoTranslateMixin, SingletonModel):

    TRANSLATABLE_FIELDS = ['title', 'text']

    title = models.CharField(max_length=300, verbose_name='Заголовок співпраці')
    title_en = models.CharField(max_length=300, blank=True)

    text = models.CharField(max_length=300, verbose_name='Текст співпраці')
    text_en = models.CharField(max_length=300, blank=True)

    class Meta:
        verbose_name = 'Умови співпраці'
        verbose_name_plural = 'Умови співпраці'
        app_label = 'home_page'

    def __str__(self):
        return self.text


class CollaborationPointHomePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['text']

    card = models.ForeignKey(CollaborationHomePage, on_delete=models.CASCADE, related_name='job_points', verbose_name='Блок співпраці')

    text = models.CharField(max_length=200, verbose_name='Пункт')
    text_en = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Пункт (співпраці)'
        verbose_name_plural = 'Пункти (співпраці)'
        app_label = 'home_page'

    def __str__(self):
        return self.text


class AboutPage(AutoTranslateMixin, SingletonModel):

    TRANSLATABLE_FIELDS = ['label', 'title', 'description']

    label = models.CharField(max_length=100, verbose_name='Заголовок')
    label_en = models.CharField(max_length=100, blank=True)

    title = models.CharField(max_length=300, verbose_name='Початок текста')
    title_en = models.CharField(max_length=300, blank=True)

    description = models.TextField(verbose_name='Основний опис')
    description_en = models.TextField(blank=True)

    img = models.ImageField(upload_to='about/', verbose_name='Зображення', blank=True, null=True)

    class Meta:
        verbose_name = 'Хто ми'
        verbose_name_plural = 'Хто ми'
        app_label = 'about_page'

    def __str__(self):
        return self.title


class OurTeamAboutPage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['profession', 'begin_text', 'description']
    # name_surname не переводим - имена собственные

    img = models.ImageField(upload_to='team/', verbose_name='Фото', blank=True, null=True)

    name_surname = models.CharField(max_length=200, verbose_name="Ім'я та прізвище")

    profession = models.CharField(max_length=200, verbose_name='Посада')
    profession_en = models.CharField(max_length=200, blank=True)

    begin_text = models.TextField(verbose_name='Короткий опис (видно одразу)')
    begin_text_en = models.TextField(blank=True)

    description = models.TextField(verbose_name='Повний опис (розкривається по кліку "Дізнатись більше")')
    description_en = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0, verbose_name='Порядок відображення')

    class Meta:
        verbose_name = 'Учасник команди'
        verbose_name_plural = 'Команда'
        ordering = ['order']
        app_label = 'about_page'

    def __str__(self):
        return f'{self.name_surname} — {self.profession}'


class ServicePage(AutoTranslateMixin, SingletonModel):

    TRANSLATABLE_FIELDS = ['title', 'text']

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    title_en = models.CharField(max_length=200, blank=True)

    text = models.TextField(max_length=500, verbose_name='Текст')
    text_en = models.TextField(max_length=500, blank=True)

    class Meta:
        verbose_name = 'Послуги'
        verbose_name_plural = 'Послуги'
        app_label = 'service_page'


class PointServicePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['text']

    card = models.ForeignKey(ServicePage, on_delete=models.CASCADE, related_name='job_points', verbose_name='Блок співпраці')

    text = models.CharField(max_length=200, verbose_name='Пункт')
    text_en = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'Пункт (Послуги)'
        verbose_name_plural = 'Пункти (Послуги)'
        app_label = 'service_page'

    def __str__(self):
        return self.text


class SpecialistsServicePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['title', 'text_begin', 'conditions', 'description']

    img = models.ImageField(upload_to='about/', verbose_name='Зображення', blank=True, null=True)

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    title_en = models.CharField(max_length=200, blank=True)

    text_begin = models.TextField(verbose_name='Короткий опис (видно одразу)')
    text_begin_en = models.TextField(blank=True)

    conditions = models.CharField(max_length=300, verbose_name='Умови (наприклад "15-20% від пакета, не більше $3000")')
    conditions_en = models.CharField(max_length=300, blank=True)

    description = models.TextField(verbose_name='Розгорнутий опис (розкривається по кліку)')
    description_en = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0, verbose_name='Порядок відображення')

    class Meta:
        verbose_name = 'Рекрутинг'
        verbose_name_plural = 'Рекрутинг'
        ordering = ['order']
        app_label = 'service_page'

    def __str__(self):
        return self.title


class SpecialistsPointServicePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['text']

    card = models.ForeignKey(
        SpecialistsServicePage,
        on_delete=models.CASCADE,
        related_name='job_points',
        verbose_name='Блок послуг'
    )

    text = models.CharField(max_length=200, verbose_name='Пункт')
    text_en = models.CharField(max_length=200, blank=True)

    order = models.PositiveIntegerField(default=0, verbose_name='Порядок відображення')

    class Meta:
        verbose_name = 'Пункт (послуг)'
        verbose_name_plural = 'Пункти (послуг)'
        ordering = ['order']
        app_label = 'service_page'

    def __str__(self):
        return self.text


class ServiceProposalServicePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = [
        'position', 'title', 'title_text', 'price',
        'text_begin', 'text_end', 'title_main', 'text_main',
    ]

    img = models.ImageField(upload_to='service_proposal/', verbose_name='Зображення', blank=True, null=True)

    position = models.CharField(max_length=100, verbose_name='Мітка (наприклад "Оренда HR-менеджера")')
    position_en = models.CharField(max_length=100, blank=True)

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    title_en = models.CharField(max_length=200, blank=True)

    title_text = models.TextField(verbose_name='Опис під заголовком')
    title_text_en = models.TextField(blank=True)

    price = models.CharField(max_length=200, blank=True, verbose_name='Умови/ціна')
    price_en = models.CharField(max_length=200, blank=True)

    text_begin = models.TextField(blank=True, verbose_name='Розгорнутий текст (початок, "Що ви отримуєте")')
    text_begin_en = models.TextField(blank=True)

    text_end = models.TextField(blank=True, verbose_name='Розгорнутий текст (кінець)')
    text_end_en = models.TextField(blank=True)

    title_main = models.CharField(max_length=200, verbose_name='Заголовок (для головної сторінки)')
    title_main_en = models.CharField(max_length=200, blank=True)

    text_main = models.TextField(verbose_name='Текст під заголовком (для головної сторінки)')
    text_main_en = models.TextField(blank=True)

    order = models.PositiveIntegerField(default=0, verbose_name='Порядок відображення')

    class Meta:
        verbose_name = 'Пропозиція послуги'
        verbose_name_plural = 'Пропозиції послуг'
        ordering = ['order']
        app_label = 'service_page'

    def __str__(self):
        return self.title


class ServiceProposalPointServicePage(AutoTranslateMixin, models.Model):

    TRANSLATABLE_FIELDS = ['text']

    card = models.ForeignKey(
        ServiceProposalServicePage,
        on_delete=models.CASCADE,
        related_name='job_points',
        verbose_name='Пропозиція послуги'
    )

    text = models.CharField(max_length=200, verbose_name='Пункт')
    text_en = models.CharField(max_length=200, blank=True)

    order = models.PositiveIntegerField(default=0, verbose_name='Порядок відображення')

    class Meta:
        verbose_name = 'Пункт (Послуги)'
        verbose_name_plural = 'Пункти (Послуги)'
        ordering = ['order']
        app_label = 'service_page'

    def __str__(self):
        return self.text


class ContactPage(AutoTranslateMixin, SingletonModel):

    TRANSLATABLE_FIELDS = ['title', 'text', 'adress', 'text_under_logo']
    # number, email, linkedin - не переводим

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    title_en = models.CharField(max_length=200, blank=True)

    text = models.TextField(verbose_name='Текст')
    text_en = models.TextField(blank=True)

    number = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Електронна пошта')

    adress = models.TextField(verbose_name='Адреса')
    adress_en = models.TextField(blank=True)

    linkedin = models.URLField(blank=True, verbose_name='Посилання на LinkedIn')

    text_under_logo = models.TextField(blank=True, verbose_name='Текст під лого в футере')
    text_under_logo_en = models.TextField(blank=True)

    text_slogan = models.TextField(blank=True, verbose_name='Текст слоган')
    text_slogan_en = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Контакти'
        verbose_name_plural = 'Контакти'
        app_label = 'contact_page'

    def __str__(self):
        return self.title


class Contact(models.Model):
    # Заявки от посетителей сайта - перевод не нужен, это входящие данные, а не контент сайта
    created_at = models.DateTimeField(auto_now_add=True)

    name_surname = models.CharField(max_length=100, verbose_name="Ім'я Прізвище")
    email = models.EmailField(verbose_name='Електронна адреса')
    country = models.CharField(max_length=100, verbose_name="Країна")
    city = models.CharField(max_length=100, verbose_name="Місто")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")

    ip_address = models.GenericIPAddressField(verbose_name="IP", null=True, blank=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Запити'
        verbose_name_plural = 'Запити'
        app_label = 'contact_page'

    def __str__(self):
        return f'{self.name_surname} ({self.created_at:%d.%m.%Y})'


class partners(models.Model):
    # Только ссылка и картинка - перевода не требуется
    link = models.URLField(verbose_name="посилання на партнера (не обов'язково)", blank=True, null=True)
    img = models.ImageField(upload_to='service_proposal/', verbose_name='Зображення', blank=True, null=True)

    class Meta:
        verbose_name = 'Партнери'
        verbose_name_plural = 'Партнери'
        app_label = 'contact_page'