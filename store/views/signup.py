from django.shortcuts import redirect, render
from store.models.customer import Customer
from django.contrib.auth.hashers import make_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'store/signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer(first_name=first_name, last_name=last_name,
                            phone=phone, email=email, password=password)

        def validateCustomer(self, customer):
            error_message = None
            if not customer.first_name:
                error_message = 'Please entet First name'
            elif len(customer.first_name) <= 4 or len(customer.first_name) > 20:
                error_message = 'Please enter First name atlis 4 and smaller than 20'
            elif not customer.last_name:
                error_message = 'Please enter Last name'
            elif len(customer.last_name) <= 4 or len(customer.last_name) > 20:
                error_message = 'Please enter last name atlis 4 and smaller than 20'
            elif not customer.phone:
                error_message = 'Please enter phone number'
            elif len(customer.phone) < 10 or len(customer.phone) > 14:
                error_message = 'Please enter phone number atlis 10 or 13 not 13+'
            elif not customer.password:
                error_message = 'Please enter password'
            elif len(customer.password) < 8 or len(customer.password) > 21:
                error_message = 'Please enter passwrd atlis 8 or 20 not 21'
            elif customer.isExists():
                error_message = 'Email Address already Registered...'
            return error_message

        error_message = None
        error_message = validateCustomer(self, customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('store')
        else:
            values = {'first_name': first_name,
                      'last_name': last_name, 'email': email, 'phone': phone}
            data = {'error': error_message, 'values': values}
            return render(request, 'store/signup.html', data)
