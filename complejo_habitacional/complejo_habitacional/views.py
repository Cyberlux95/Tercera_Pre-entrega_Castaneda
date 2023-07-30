from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto,
    )
    return http_response
