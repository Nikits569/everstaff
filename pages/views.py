from django.utils import timezone
from datetime import timedelta

from django.contrib import messages
from TelegramBot.notifications import send_message
import asyncio
from .forms import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
import logging
from django.core.mail import send_mail
 
logger = logging.getLogger(__name__)

# Create your views here.
def main(request):

    contact_info = ContactPage.get_solo()
    partners_info = partners.objects.all()

    home_page = HomePage.get_solo()

    approach_card_home_page = ApproachCardHomePage.objects.all()
    approach_card_point_home_page = ApproachCardPointHomePage.objects.all()

    industries_home_page = IndustriesHomePage.get_solo()
    industries_flat_point_home_page = IndustriesFlatPointHomePage.objects.all()
    industries_job_point_home_page = IndustriesJobPointHomePage.objects.all()

    collaboration_home_page = CollaborationHomePage.get_solo()
    collaboration_point_home_page = CollaborationPointHomePage.objects.all()

    service_proposal_service_page = ServiceProposalServicePage.objects.prefetch_related('job_points').all()

    context = {
        'HomePage': home_page,
        'ApproachCardHomePage': approach_card_home_page,
        'ApproachCardPointHomePage': approach_card_point_home_page,
        'IndustriesHomePage': industries_home_page,
        'IndustriesFlatPointHomePage': industries_flat_point_home_page,
        'IndustriesJobPointHomePage': industries_job_point_home_page,
        'CollaborationHomePage': collaboration_home_page,
        'CollaborationPointHomePage': collaboration_point_home_page,
        'ServiceProposalServicePage': service_proposal_service_page,

        'contact': contact_info,
        'partner': partners_info,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    about_page = AboutPage.get_solo()
    our_team_about_page = OurTeamAboutPage.objects.all()

    contact_info = ContactPage.get_solo()
    partners_info = partners.objects.all()

    context = {'AboutPage': about_page, 'OurTeamAboutPage': our_team_about_page,
               'contact': contact_info, 'partner': partners_info,
               }

    return render(request, 'pages/about.html', context)

def contact(request):
    # raise Exception("CONTACT VIEW EXECUTED")
    print("METHOD:", request.method)
    contact_info = ContactPage.get_solo()
    partners_info = partners.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        IP = request.META.get('REMOTE_ADDR')

        if form.is_valid():

            if Contact.objects.filter(ip_address=IP, created_at__gte=timezone.now() - timedelta(days=1)).count() >= 3:
                messages.error(request, 'Вибачаємось але за цим IP було занадто багато спроб відправки форми')
                return redirect('home')

            form = form.save(commit=False)
            form.ip_address = IP
            form.save()
            try:
                logger.info("Начинаю отправку письма на user@example.com")
                print("=== ДО ОТПРАВКИ ===")
                count = send_mail(
                    subject=f'Нова заявка з сайту: {form.title}',
                    message=f"Ім'я: {form.name_surname}\n"
                            f"Email: {form.email}\n"
                            f"Країна: {form.country}\n"
                            f"Місто: {form.city}\n\n"
                            f"Текст:\n{form.text}",
                    from_email=None,
                    recipient_list=['everstaff@ukr.net'],
                    fail_silently=False,
                )
                logger.info(f"Письмо успешно отправлено. send_mail вернул {count}")
                print("=== ПОСЛЕ ОТПРАВКИ ===", count)
            except Exception as e:
                logger.info('Error', e)
                logger.exception("Ошибка при отправке письма")

            asyncio.run(send_message(form.name_surname, form.email, form.title, form.text, form.country, form.city))

            messages.success(request, 'Дякуємо! Ми зв\'яжемось з вами найближчим часом.')
            return redirect('home')

    else:
        form = ContactForm()

    context = {'form': form,'contact_page': ContactPage.get_solo(),
               'contact': contact_info, 'partner': partners_info,
               }

    return render(request, 'pages/contacts.html', context)

def service(request):

    service_page = ServicePage.get_solo()
    point_service_page = PointServicePage.objects.all()

    contact_info = ContactPage.get_solo()
    partners_info = partners.objects.all()

    specialists_service_page = SpecialistsServicePage.objects.all()
    specialists_point_service_page = SpecialistsPointServicePage.objects.all()

    service_proposal_service_page = ServiceProposalServicePage.objects.prefetch_related('job_points').all()
    service_proposal_point_service_page = ServiceProposalPointServicePage.objects.all()


    context = {'service_page': service_page, 'point_service_page': point_service_page,
               'specialists_service_page': specialists_service_page, 'specialists_point_service_page': specialists_point_service_page,
               'service_proposal_service_page': service_proposal_service_page, 'service_proposal_point_service_page': service_proposal_point_service_page,
               'contact': contact_info, 'partner': partners_info
               }

    return render(request, 'pages/services.html', context)
