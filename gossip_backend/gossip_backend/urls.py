"""
URL configuration for gossip_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from sources.views import CreateMessageView, GetDiscussionsView, LoginView, ListUsersView, GetSourcesUserIDView, DiscussionSummariesView, DiscussionSourcesView
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/create_message/', CreateMessageView.as_view(), name='send_data'),
    path('api/get_discussions/', GetDiscussionsView.as_view(), name='send_data'),
    path('api/get_sources_user_id/', GetSourcesUserIDView.as_view(), name='send_id'),
    path('api/users/', ListUsersView.as_view(), name='list-users'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/discussions/', DiscussionSummariesView.as_view(), name='discussion-summaries'),
    path('api/discussions/<int:diss_id>/sources/', DiscussionSourcesView.as_view(), name='discussion-sources'),
]
