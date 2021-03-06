"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework.authtoken import views as auth_views

from playit import api
from playit.api import views

router = routers.DefaultRouter()
#todo example delete me
# router.register(r'game', api.views.GameViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),

    url(r'^api/token-auth/', auth_views.obtain_auth_token),
    url(r'^api/game/', api.views.get_game_by_pincode),
    url(r'^api/create_game/',  api.views.create_game),
    url(r'^api/join_game/', api.views.join_game),
    url(r'^api/start_game/', api.views.start_game),
    url(r'^api/get_next_question/', api.views.get_next_question),
    url(r'^api/get_players/', api.views.get_players),
    url(r'^api/get_session_object/', api.views.get_session_object),
    url(r'^api/save_answer/', api.views.save_answer),
    url(r'^api/get_score_board/', api.views.get_score_board),
    url(r'^api/get_round_summary/', api.views.get_round_summary),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+[url(r'', TemplateView.as_view(template_name='index.html'))]





