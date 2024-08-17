from .models import Settings

def get_context_data(request):
    data=Settings.objects.last()
    return {'context_data':data}