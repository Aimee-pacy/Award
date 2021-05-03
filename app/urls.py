from django.urls import path, include
from .views import home,signup,profile, edit_profile, project, search_projects,ProjectList,ProfileList


urlpatterns = [
    path('', home, name = 'home'),
    path('signup/', signup, name='signup'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('profile/<username>/', profile, name='profile'),
    path('profile/<username>/', edit_profile, name='edit_Profile'),
    path('project/<id>',project, name='project'),
    path('search/', search_projects, name='search'),
    path('api/projects/', ProjectList.as_view()),
    path('api/profiles/', ProfileList.as_view())
]
