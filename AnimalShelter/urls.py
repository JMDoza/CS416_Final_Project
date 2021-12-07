from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('find', views.find, name='find'),
    path('search/dogs', views.dog_search, name='dog_search'),
    path('search/cats', views.cat_search, name='cat_search'),
    path('profile/cat/<int:id>', views.profile_cat, name='cat_profile'),
    path('profile/dog/<int:id>', views.profile_dog, name='dog_profile'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboard/create/cat', views.create_cat, name='create_cat'),
    path('dashboard/create/dog', views.create_dog, name='create_dog'),
    path('dashboard/create/cat/breed', views.create_cbreed, name='create_cbreed'),
    path('dashboard/create/dog/breed', views.create_dbreed, name='create_dbreed'),
    path('dashboard/update/cat/<int:id>', views.update_cat, name='update_cat'),
    path('dashboard/update/dog/<int:id>', views.update_dog, name='update_dog'),
    path('dashboard/update/cat/breed/<int:id>', views.update_cbreed, name='update_cbreed'),
    path('dashboard/update/dog/breed/<int:id>', views.update_dbreed, name='update_dbreed'),
    path('dashboard/delete/cat/<int:id>', views.delete_cat, name='delete_cat'),
    path('dashboard/delete/dog/<int:id>', views.delete_dog, name='delete_dog'),
    path('dashboard/delete/cat/breed/<int:id>', views.delete_cbreed, name='delete_cbreed'),
    path('dashboard/delete/dog/breed/<int:id>', views.delete_dbreed, name='delete_dbreed'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
