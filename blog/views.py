from django.shortcuts import render

# Create your views here.


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def register(request):
    # Kayıt işlemleri burada gerçekleştirilecek
    return render(request, 'register.html')

def blog_post(request):
    # Blog gönderisi oluşturma işlemleri burada gerçekleştirilecek
    return render(request, 'blog_post.html')
