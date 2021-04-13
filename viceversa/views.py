from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	text = request.GET['message']
	reversed_text = text[::-1]
	n = len(text.split())
	return render(request, 'reverse.html', {'text':text, 'reversedtext':reversed_text, 'words':n})