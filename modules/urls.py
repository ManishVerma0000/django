from django.urls import path

from .views.contact_views import create_contactUs,get_all_contacts,get_contact_by_id,update_contact_details_using_id
from .views.testimonial import upload_user_photo,get_testimonials,get_testimonials_using_user_id,delete_testimonial
from .views.user_views import create_user,login_user
from .views.menu_views import create_menu
from .views.carasoul_views import add_carasoul_image,delete_carasoul_image,getCarasoulList,upload_carousel_images,getCarasoulListPerUser


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
    path('user/testimonial', get_testimonials_using_user_id, name='get_testimonials_using_user_id'),
    path('delete/testimonial', delete_testimonial, name='get_testimonials_using_user_id'),
    path('add/carasoul', add_carasoul_image, name='add_carasoul_image'),
    path('delete/carasoul', delete_carasoul_image, name='delete_carasoul_image'),
    path('list/carasoul', getCarasoulList, name='getCarasoulList'),
    path('upload-carousel-images', upload_carousel_images, name='upload_carousel_images'),
    path('user/carasoul', getCarasoulListPerUser, name='getCarasoulListPerUser'),
]
