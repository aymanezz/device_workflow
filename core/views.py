from django.http import HttpResponse

def home(request):
    return HttpResponse("Device Workflow is running ✅")
