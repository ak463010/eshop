from django.shortcuts import redirect


def auth_middleware(get_response):
    def middleware(request):
        if not request.session.get('customer_id'):
            return_url = request.META['PATH_INFO']
            return redirect(f'/login?return_url={ return_url }')
        return get_response(request)
    return middleware
