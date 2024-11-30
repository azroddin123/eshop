# email_utils.py
import threading
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.template import Template

def send_html_email(subject, template_name, context, recipient_list):
    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    send_mail(
        subject,
        plain_message,
        from_email,
        recipient_list,
        fail_silently=False,
        html_message=html_message
    )
    
    
class HTMLEmailThread(threading.Thread):
    def __init__(self, subject, template_name, context, recipient_list):
        self.subject = subject
        self.template_name = template_name
        self.context = context
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)

    def run(self):
        send_html_email(self.subject, self.template_name, self.context, self.recipient_list)



def send_email_async(subject, template_name, context, recipient_list):
    HTMLEmailThread(subject, template_name, context, recipient_list).start()
    
    


