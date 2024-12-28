from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    """
    Middleware to check if a user is authenticated before allowing access to certain pages.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of paths that do not require authentication
        exempt_urls = [
            reverse('loginuser'),  # Replace with your actual login URL name
            reverse('register'), # Replace with your signup URL name
            reverse('home'), # Replace with your signup URL name
            reverse('about'), # Replace with your signup URL name
            reverse('policy'), # Replace with your signup URL name
            reverse('contact'), # Replace with your signup URL name
            reverse('forgot'), # Replace with your signup URL name
            reverse('verify'), # Replace with your signup URL name
            reverse('admin'), # Replace with your signup URL name
            reverse('loginApi'), # Replace with your signup URL name
            reverse('passwordApi'), # Replace with your signup URL name
        ]

        # If the user is not authenticated and the path is not exempt, redirect to login
        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('loginuser')  # Replace with your login URL name
       
        # Proceed with the request
        response = self.get_response(request)
        return response
