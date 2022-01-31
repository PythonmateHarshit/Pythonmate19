from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.utils.translation import ugettext as _
from .models import Contact
import time

class home_view(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            name = request.POST.get('clientname')
            from_email = request.POST.get('clientemail')
            subject = request.POST.get('clientsubject')
            message = request.POST.get('clientmessage')
        message = message+'\n'+ name +',\n'+'Contact us at:-'+subject
        subject_pythonmate = 'Hello PythonMate!'
        context = {}
        if subject and message and from_email:
            for i in range(5):
                try:
                    time.sleep(2)
                    mail_status = send_mail(subject_pythonmate, message, from_email, ['pythonmatedivyesh@gmail.com'])
                    if mail_status == 1:
                        context['message'] = 'Thanks for contacting us. We will reach you soon.'
                        break
                    else:
                        send_mail('Mail Failed','Please Check Database', 'pythonmatepawas@gmail.com', ['pythonmatedivyesh@gmail.com'])
                        Contact.objects.create(name=name,email=from_email,social_id=subject,message=message + str(e),mail_status=True if mail_status==1 else False, mail_status_discription=str(mail_status))
                except Exception as e:
                        Contact.objects.create(name=name,email=from_email,social_id=subject,message=message + str(e),mail_status=False,mail_status_discription = str(e))
                        context['message'] = 'Thanks. But seem we are unable to get this email, Please try once again. Or contact us at pythonmatedivyesh@gmail.com'
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            context['message'] = 'Make sure all fields are entered and valid.'
        return render(request, 'index.html', context)
