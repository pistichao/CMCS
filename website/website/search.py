# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render
 
# 表单
def search_form(request):
    return render(request,'search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = 'The content you search is: ' + request.GET['q']
    else:
        message = 'Empty from!!!'
    return HttpResponse(message)