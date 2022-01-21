from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def post_list(request, id):
    posts=Post.objects.filter(pk=id)
    post_list = serializers.serialize('json', posts)
    print(request)    
    return HttpResponse(post_list, content_type="text/json-comment-filtered; charset=utf-8")
    #return render(request, 'exhibition/post_list.html',{'posts':post_list})