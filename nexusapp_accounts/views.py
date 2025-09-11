from django.http import HttpResponse

def index(request):
    """
    Basic view for the Accounts app.
    Returns a simple response to confirm the app is working.
    """
    return HttpResponse("✅ Accounts app is working!")
