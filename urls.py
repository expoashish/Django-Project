from django.urls import path

from . import views
app_name = 'contact_book'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.new_contact, name='new_contact'),
    path('submit-form',views.submit_contact, name='submit_contact'),
    path('upload/', views.image_upload_view),
    path('delete_contact/<int:id>', views.delete_contact, name='delete_contact'),
    path('detail/<int:id>', views.detail_contact, name='detail_contact'),
    path('edit/<int:id>', views.edit_contact, name='edit_contact'),
]