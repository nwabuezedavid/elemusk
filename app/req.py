from django.shortcuts import redirect
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Account

def account_enabled_required(view_func):
    @wraps(view_func)
    @login_required
    def wrapper(request, *args, **kwargs):
        try:
            account = Account.objects.get(user=request.user)
            if account.disable:
                # Redirect to a page or raise an error if the account is disabled
                return redirect('block')  # or raise PermissionDenied
        except Account.DoesNotExist:
            raise PermissionDenied("Account does not exist.")

        return view_func(request, *args, **kwargs)
    
    return wrapper




def superuser_required(view_func):
    @wraps(view_func)
    @login_required  # Ensures that the user is logged in first
    def wrapper(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied("You do not have permission to view this page.")
            # Alternatively, you could redirect to a "not authorized" page:
            # return redirect('not_authorized')
    
    return wrapper
