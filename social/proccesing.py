from .models import Social

def dictionary(request):
    social_dict = {}
    for red in Social.objects.all():
        social_dict[red.key] = red.url
    return social_dict
