from django.urls import path
from .views import home, calculator, sign_in, sign_up, sign_out, calculated_panels,calculator2, fetch_solar_components
urlpatterns = [
    path('', home, name='home'),
    path('components/', fetch_solar_components, name='fetch_solar_components'),
    path('calculator/', calculator, name='calculator'),
    path('calculator2/', calculator2, name='calculator2'),
    path('calculated-panels/', calculated_panels, name='calculated-panels'),
    path('sign-in/', sign_in, name='sign-in'),
    path('sign-up/', sign_up, name='sign-up'),
    path('sign-out/', sign_out, name='sign-out'),
]
