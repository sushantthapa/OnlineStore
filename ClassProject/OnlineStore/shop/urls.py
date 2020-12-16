from . import views
from django.urls import path

urlpatterns = [
    path("",views.index, name="ShopHome"),
    path("about/",views.about, name="About Us"),
    path("contact/",views.contact, name="Contact Us"),
    path("search/",views.search, name="Search"),
    path("products/<int:myid>",views.productview, name="ProductView"),
    path("signup/",views.signup, name="Signup")

]
