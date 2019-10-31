# from django.conf.urls import url
#
# # This syntax imports all of the functions and classes
# # inside the views.py in the same folder.
# from . import views
#
# urlpatterns = [
#     url(r'^now/$', views.show_the_time),
# ]

from django.conf.urls import url

from . import views

urlpatterns = [
    # Change how we reference the new view.
    url(r'^now/$', views.ShowTimeView.as_view()),
]
