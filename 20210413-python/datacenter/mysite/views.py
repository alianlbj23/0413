from django.shortcuts import render
from django.http import HttpResponse
import random
def index(request):
	myname = "曾裕翔"
	data = [i for i in range(1,42)]
	random.shuffle(data)
	lotto_number = data[0:7]
	return render(request, 'index.html', locals())