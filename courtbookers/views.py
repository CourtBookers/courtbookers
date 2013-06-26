from django.shortcuts import redirect, render_to_response


def root_view(request):
    return redirect("home")


def home_view(request):
    return render_to_response("home.html")
