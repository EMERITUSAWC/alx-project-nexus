from django.http import HttpResponse

def index(request):
    """
    Basic view for the Orders app.
    Returns a simple response to confirm the app is working.
    """
    return HttpResponse("✅ Orders app is working!")
