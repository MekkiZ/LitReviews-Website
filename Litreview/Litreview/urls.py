"""Litreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import authentication.views
from flux import views as flux_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', authentication.views.login_user, name='login'),
    path('signup/', authentication.views.signup_user, name='signup'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('flux/', flux_views.flux, name='flux'),
    path('create_ticket/', flux_views.create_ticket, name='create-ticket'),
    path('posts/', flux_views.posts, name='posts'),
    path('create/critique/', flux_views.create_critic_no_answer, name='critique_rating'),
    path('review_update/<int:p_id>/', flux_views.update_review, name='update_review'),
    path('ticket_only/<int:p_id>/', flux_views.ticket_only, name='ticket_only'),
    path('delete_posts/<int:p_id>/', flux_views.delete_posts, name='delete_posts'),
    path('reviews/ticket-posts/<int:p_id>/', flux_views.create_review_for_post, name='reviews-ticket'),
    path('search/', flux_views.search, name='search'),



]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
