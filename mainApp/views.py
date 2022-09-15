from django.shortcuts import render

# Create your views here.
def Home(request):
  return render(request=request, template_name='mainApp/Home.html')


def UploadImage(request):
  return render(request=request, template_name='mainApp/UploadImage.html')

def AboutUs(request):
  return render(request=request, template_name='mainApp/AboutUs.html')