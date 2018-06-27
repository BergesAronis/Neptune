from .models import Navigation

def navigation_apps(request):
    navigation_apps = Navigation.objects.values()
    return {'navigation_apps': navigation_apps}
