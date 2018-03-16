from django.views.generic import TemplateView

urlpatterns = []

handler404 = TemplateView.as_view(template_name='jeklog/404.html')
handler500 = TemplateView.as_view(template_name='jeklog/500.html')
handler403 = TemplateView.as_view(template_name='jeklog/403.html')
handler400 = TemplateView.as_view(template_name='jeklog/400.html')
