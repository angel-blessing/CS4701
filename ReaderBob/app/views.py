from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import QueryDict
from . import xyproject3
import json

def index(request):
	return render(request, 'index.html')

def splitDoc(request):
	doc = request.GET['data']
	rawParagraphs = doc.split('\n')
	paragraphs = []
	for paragraph in rawParagraphs:
		if paragraph != "":
			paragraphs.append(paragraph)
	response = JsonResponse({'paragraphs': paragraphs})
	return response

def getAnswer(request):
	paragraph = json.loads(request.POST['paragraphs'])
	pack = {"title": "", "paragraphs": paragraph}
	data = []
	data.append(pack)
	print({"data": data})
	result = xyproject3.init({"data": data})
	response = JsonResponse({'status': 0, "result": result})
	return response
