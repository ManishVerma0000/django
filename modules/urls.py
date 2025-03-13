from django.urls import path

from .views.contact_views import create_contactUs,get_all_contacts,get_contact_by_id,update_contact_details_using_id
from .views.add_testimonial import upload_user_photo,get_testimonials
from .views.user_views import create_user,login_user
from .views.menu_views import create_menu


urlpatterns = [
    path('create-contact-us',create_contactUs,name='create_user'),
    path('contact/all/', get_all_contacts, name='contact-all'),
    path('contact/<int:id>/', get_contact_by_id, name='contact-detail'),
    path('create-testimonial',upload_user_photo,name='create-testimonial'),
    path('update-contact-us/<int:id>',update_contact_details_using_id,name='update-contact'),
    path('create-user',create_user, name='create-user'),
    path('login-user', login_user , name='login-user'),
    path('create-menu', create_menu, name='create-menu'),
    path('get_testimonials', get_testimonials, name='get_testimonials'),
]
