# Blogs/views.py
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.shortcuts import render

def blog(requests):
    blog_posts = BlogPost.objects.all()
    return render(requests, 'blog.html', {'blog_posts': blog_posts})

@api_view(['GET'])
def blog_list(request):
    posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])  # Enables file upload
def blog_add(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Blog post created!', 'data': serializer.data}, status=201)
    return Response(serializer.errors, status=400)