from django.urls import path

from .views.contact_views import create_contactUs,get_all_contacts,get_contact_by_id,update_contact_details_using_id
from .views.testimonial import upload_user_photo,get_testimonials,get_testimonials_using_user_id,delete_testimonial
from .views.user_views import create_user,login_user
from .views.menu_views import create_menu
from .views.carasoul_views import add_carasoul_image,delete_carasoul_image,getCarasoulList,upload_carousel_images,getCarasoulListPerUser
from .views.pop_up_views import upload_pop_Up_images,get_pop_up_images,upload_popup_images,get_pop_up_image_user,delete_pop_up_image
from .views.vision_mission_views import create_vision_mission,get_vision_mission_per_user,delete_vision_mission
from .views.facilities_views import create_facilities,get_facilities_per_user,delete_facilities

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
    path('user/uploadimages', upload_pop_Up_images, name='upload_pop_Up_images'),
    path('user/popup/image', get_pop_up_images, name='get_pop_up_images'),
    path('popup/images', upload_popup_images, name='upload_popup_images'),
    path('delete/popup', delete_pop_up_image, name='delete_pop_up_image'),
    path('user/popup', get_pop_up_image_user, name='get_pop_up_image_user'),
    path('create-vision-mission',create_vision_mission, name='create_vision_mission'),
    path('get-vision-mission',get_vision_mission_per_user, name='get_vision_mission_per_user'),
    path('delete-vision-mission',delete_vision_mission, name='delete_vision_mission'),
    path('create-facilities',create_facilities, name='create_facilities'),
    path('get-facilities',get_facilities_per_user, name='get_facilities_per_user'),
    path('delete-facilities',delete_facilities, name='delete_facilities'),
    
]
