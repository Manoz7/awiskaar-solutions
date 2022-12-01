from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.utils import timezone

from config import settings
from apps.core.models import Contact


def send_contact_request_mail(contact_id):
    contact = Contact.objects.get(id=contact_id)
    html_template = 'core/contact_request.html'
    context = {
        "contact": contact
    }
    message = render_to_string(template_name=html_template, context=context)
    html_message = render_to_string(html_template, context=context)

    try:
        send_mail("New contact request from Awiskaar Solution",
                  message,
                  from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=['sheamuskhan48@gmail.com', 'manojkhanal936@gmail.com'],
                  html_message=html_message,
                  fail_silently=False)
    except BadHeaderError:
        return 'Invalid Header Found'
    return True
