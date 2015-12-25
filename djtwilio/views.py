# views.py

# -*- coding: utf-8 -*-
from django_twilio.decorators import twilio_view
from twilio.twiml import Response


@twilio_view
def sms(request):
	name = request.POST.get('Body', '')
	msg = 'Hey %s, how are you today?' % (name)
	r = Response()
	r.message(msg)
	return r
