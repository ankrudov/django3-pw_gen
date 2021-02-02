from django.shortcuts import render
from django.http import HttpResponse # importing an http will allow the return string to print onto the website
import random

# Create your views here.
def home(request):
    return render(request,'pw_gen/home.html') #return template 


def password(request):
    
    character= list('abcdefghijklmnopqrstuvwxyz')
    upper_char = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    special_char = list('!@#$%')
    random_num = list('1234567890')

    length = int(request.GET.get('length',13)) #this pulls the int from the HTML data form 'length' the number 13 is the default value for the generated password

    #If the user chooses uppercase,number or special radio button then character will extend with another list
    if request.GET.get('uppercase'):
        character.extend(upper_char)
    if request.GET.get('numbers'):
        character.extend(random_num)
    if request.GET.get('special'):
        character.extend(special_char) 

    random_password = ''
    for i in range(length):
        random_password += random.choice(character)
    return render(request,'pw_gen/password.html', {'password':random_password})


def about(request):
    return render(request,'pw_gen/about.html') #return about page

