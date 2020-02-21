from django.views.generic import TemplateView


# Create your views here.
class FrontView(TemplateView):
    template_name = "front.html"

    def get_context_data(self, **kwargs):
        context = super(FrontView, self).get_context_data(**kwargs)
        return context
