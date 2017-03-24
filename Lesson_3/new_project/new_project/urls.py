from django.conf.urls  import include, url
from django.contrib    import admin

from base              import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'new_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^say_hello$', views.say_hello),
    url(r'^status$', views.status),
    url(r'^django_info$', views.django_info),

    url(r'^players_list$', views.players_list),
    url(r'^players_table$', views.players_table),
    url(r'^players_info/([0-9]+)/$', views.verbose_player_info),
    url(r'^players_money/([0-9]+)/$', views.player_money),
    url(r'^filter_player_name/$', views.player_name),

]
