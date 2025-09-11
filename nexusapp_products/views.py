from django.http import HttpResponse

def index(request):
    """
    Basic view for the Products app.
    Returns a simple response to confirm the app is working.
    """
    return HttpResponse("✅ Products app is working!")
