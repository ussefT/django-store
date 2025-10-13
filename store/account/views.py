from django.shortcuts import render
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django import views
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from . import models
from django.shortcuts import get_object_or_404

# use default token generator django
from django.contrib.auth.tokens import PasswordResetTokenGenerator
class TokenGenrator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return str(user.pk)+str(timestamp)+"0"

activation_token_generator=TokenGenrator()

from . import form
#class base
#  views.View
#  Generic [TemplateView, ListView, DetailView .....] write by default django
class SignUpView(views.View):
    def get(self,request):
        """show sign up form"""
        form_=form.SignUpForm()
        return render(request
                      ,'account/signUp.html'
                      ,{'form':form_})

    def post(self,request):
        """create new user from form """
        form_=form.SignUpForm(request.POST)
        if form_.is_valid():
            # obj=form_.save() # save it to database
            obj=form_.save(commit=False) # onyl create object but do not create in db
            obj.is_active=False # user can not login
            obj.save()

            # generate id user to byte -> base64
            uid=urlsafe_base64_encode(force_bytes(str(obj.pk)))

            #
            hash=activation_token_generator.make_token(obj)

            # dynamic url enter uid, hash
            url=reverse('account:activate',kwargs={'uid':uid,'hash':hash})


            domain=get_current_site(request)

            link=f'http://{domain}{url}/****'

            subject="Please activate your account"
            body=render_to_string('account/signup_email.html',{"obj":obj,'link':link})
            to=obj.email

            # define email func
            email=EmailMessage(subject
                               ,body,
                               ''
                               ,to)
            # send email
            email.send()
            return render(request,'account/signUp_done.html',{'obj':obj})
        return render(request,'account/signUp.html',{'form':form_})

    #     #  we can use this manually but is wrong
    #     # print(
    #     #     request.POST.get("name")
    #     #       )
    #
    #     # Correct
    #     form_=form.SignupForm(request.POST)
    #     if form_.is_valid(): # if true form is fill
    #     #     for use data form.clean_data['mail']
    #     # when fill form
    #     return render(request,'account/signUp.html',{'form':form_})


class ActivateView(views.View):
    def get(self,request,uid,hash):
        # find user
        id=force_str(urlsafe_base64_decode(uid))

        #  handle manual error
        # try:
        #     user=models.User.objects.get(id=id)
        #     if user.is_active:
        #         return render(request,'account/activate_error.html')
        # except models.User.DoesNotExist:
        #     # out error
        #     return render(request,'account/activate_error.html')
        # ####################################

        # automate error 404
        user = get_object_or_404(models.User,id=id)
        if user.is_active:
            return render(request, 'account/activate_error.html')

        # check hash
        if activation_token_generator.check_token(user,hash):
            # activate user
            user.is_active=True
            user.save()
            # say thanks
            return render(request,'account/activate_done.html')
        return render(request,'account/activate_error.html')



