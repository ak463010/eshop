from django.urls import path
from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.oders import Oders
from .middlewares.auth import auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='store'),
    path('sighup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('logout/', logout, name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('check-out/', CheckOut.as_view(), name='checkout'),
    path('oders/', auth_middleware(Oders.as_view()), name='oders'),
]
