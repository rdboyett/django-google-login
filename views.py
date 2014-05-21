import os
ROOT_PATH = os.path.dirname(__file__)

import json
import logging
import httplib2
from datetime import datetime, timedelta

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.utils import simplejson
from django.core.mail import send_mail
from django.utils import timezone

from google_login.models import CredentialsModel, GoogleUserInfo, ForgottenPassword
from google_login import settings
from forms import ContactForm

from apiclient.discovery import build
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

from oauth2client.client import OAuth2WebServerFlow

from apiclient import errors


# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret, which are found
# on the API Access tab on the Google APIs
# Console <http://code.google.com/apis/console>
CLIENT_SECRETS = settings.CLIENT_SECRETS

SCOPES = settings.SCOPES

FLOW = flow_from_clientsecrets(
    CLIENT_SECRETS,
    scope= ' '.join(SCOPES),
    redirect_uri= settings.redirect_uri)



def index(request):
    if 'user_id' in request.session:
        user_id = request.session['user_id']
        if User.objects.filter(id=user_id):
            user = User.objects.get(id=user_id)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            return HttpResponseRedirect(settings.LOGIN_SUCCESS)
        
        else:
            user_id = False
    else:
        user_id = False
    
    if not user_id:
        args = {}
        args.update(csrf(request))
        #redirect to user login page
        return render_to_response('google_login/login.html', args)

    
def auth(request):
    
    credential = None
        
    if credential is None or credential.invalid == True:
        FLOW.params['access_type'] = 'offline'
        FLOW.params['state'] = xsrfutil.generate_token(settings.SECRET_KEY,
                                                        request.user)
        authorize_url = FLOW.step1_get_authorize_url()
        return HttpResponseRedirect(authorize_url)


def auth_return(request):
    
    if not xsrfutil.validate_token(settings.SECRET_KEY, request.REQUEST['state'],
                                   request.user):
      return  HttpResponseBadRequest()
    credential = FLOW.step2_exchange(request.REQUEST)

    user_info = get_user_info(credential)
    google_email = user_info.get('email')
    firstName = user_info.get('given_name')
    lastName = user_info.get('family_name')
    google_id = user_info.get('id')
    googlePlus = user_info.get('link')
    language = user_info.get('locale')
    googleAvatar = user_info.get('picture')
    gender = user_info.get('gender')
        
    emailEnding = google_email.split("@")[1]
    userName = "@"+google_email.split("@")[0]
    
    if User.objects.filter(username=userName):
        # Make sure that the e-mail is unique.
        user = User.objects.get(username=userName)
        #userInfo = UserInfo.objects.get(user=user)
    elif User.objects.filter(email=google_email):
        user = User.objects.get(email=google_email)
    else:
        user = User.objects.create(
            username = userName,
            first_name = firstName,
            last_name = lastName,
            email = google_email,
            password = userName+google_id[:5],
        )

    #Update the User model with changes in google
    user.first_name = firstName
    user.last_name = lastName
    user.save()

    #Check to see if a google account has been setup yet
    if not GoogleUserInfo.objects.filter(google_id=google_id):
        newGoogleUser = GoogleUserInfo.objects.create(
            user = user,
            google_id = google_id,
            googlePlus = googlePlus,
            language = language,
            googleAvatar = googleAvatar,
            gender = gender,
        )
            
    
    #check to see if user is logged in
    if user:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        
    request.session['user_id'] = user.id
    request.session.set_expiry(604800)
    storage = Storage(CredentialsModel, 'id', user, 'credential')
    storage.put(credential)
    return HttpResponseRedirect(settings.LOGIN_SUCCESS)



def get_user_info(credentials):
  """Send a request to the UserInfo API to retrieve the user's information.

  Args:
    credentials: oauth2client.client.OAuth2Credentials instance to authorize the
                 request.
  Returns:
    User information as a dict.
  """
  user_info_service = build(
      serviceName='oauth2', version='v2',
      http=credentials.authorize(httplib2.Http()))
  user_info = None
  try:
    user_info = user_info_service.userinfo().get().execute()
  except errors.HttpError, e:
    logging.error('An error occurred: %s', e)
  if user_info and user_info.get('id'):
    return user_info
  else:
    raise NoUserIdException()



@login_required
def success(request):
    return HttpResponse("You've logged in with success!")




def error(request):
    return HttpResponse("There was an error during login!")



def test(request):
    return HttpResponse("Hello, You're in!")


def forgotPassword(request, forgotID=False):
    if forgotID:
        #check that it has been less than 5 minutes since forgotID was created.
        if ForgottenPassword.objects.filter(id=forgotID):
            forgot = ForgottenPassword.objects.get(id=forgotID)

            now = timezone.now()
            tdelta = now - forgot.dateTime
            seconds = tdelta.total_seconds()

            if not seconds:# > 300 or forgot.used:
                return HttpResponse('You reached this link in error.'+str(seconds))
            else:
                forgot.used = True
                forgot.save()

                args = {}
                args.update(csrf(request))
                args['passwordForm'] = ContactForm()
                return render_to_response('google_login/change_password.html', args)
        else:
            return HttpResponse('You reached this link in error.')

        #Set the dateTime to 0 so that this link will only work once.
    else:
        return HttpResponse('You reached this link in error.')


def passwordReset(request):
    return HttpResponse('You reached this link.')












#-------------------------- Ajax calls -------------------------------------------

def ajaxAuth(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        user = authenticate(username=username, password=password)

        if user is None and User.objects.filter(email=username):
            userEmail = User.objects.get(email=username)
            user = authenticate(username=userEmail.username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = user.id
                request.session.set_expiry(604800)
                data = {'success':'success'}
            else:
                data = {'error':'<div class="google-login-error">incorrect username or password</div>'}
        else:
			data = {'error':'<div class="google-login-error">incorrect username or password</div>'}
    
    return HttpResponse(json.dumps(data))
    
    
    


def checkUsername(request):
    if request.method == 'POST':
        username = request.POST['username']
        if User.objects.filter(username=username):
            data = {'exists':'true'}
        else:
            data = {'exists':'false'}
    else:
        data = {'error':'Did not post correctly'}
    return HttpResponse(json.dumps(data))




def submitRegistration(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()

        if User.objects.filter(username=username):
            data = {'error':'This username is already taken.'}
        elif User.objects.filter(email=email):
            data = {'error':'This email is already used with another account.'}
        else:
            user = User.objects.create_user(username, email, password)
            
            #check to see if user is logged in
            if user:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
                
            request.session['user_id'] = user.id
            request.session.set_expiry(604800)
            data = {'success':'success'}

    else:
        data = {'error':'Did not post correctly'}
    return HttpResponse(json.dumps(data))



def doesEmailExist(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email):
            data = {'exists':'true'}
        else:
            data = {'exists':'false'}
    else:
        data = {'error':'Did not post correctly'}
    return HttpResponse(json.dumps(data))




def submitPasswordForgot(request):
    if request.method == 'POST':
        email = request.POST['email']
        if User.objects.filter(email=email):
            user = User.objects.get(email=email)
            forgotLink = ForgottenPassword.objects.create()
            try:
                send_mail(
                    'Alert from '+ settings.WEBSITENAME,
                    'To reset your password please follow this link:\n\n'+
                    settings.ROOT_WEBSITE_LINK+'/google/forgot/'+ str(forgotLink.id) + '\n\n'+
                    'If you feel this message reached you in error, please disregard or you can email '+ settings.WEBMASTER_EMAIL +' for any questions.',
                    settings.WEBMASTER_EMAIL,
                    [email],
                    fail_silently=False
                )
                data = {'exists':'true'}
            except:
                data = {'error':'Your server email settings have not been set.  Please read the requirements text.'}
        else:
            data = {'exists':'false'}
    else:
        data = {'error':'Did not post correctly'}
    return HttpResponse(json.dumps(data))
















