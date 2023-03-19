from django.shortcuts import render
from .models import Response

# Create your views here.
openai_key = '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'

def chatbot(reqeust):
    question = (str)(reqeust.POST.get('user_input'))
    response = "No idea sorry !!"
    for each in Response.objects.all():
        if (question.lower() == each.question):
            response = each.answer

    if question == "":
        response = ""

    return render(reqeust,'chatbot.html',{"answer" : response})