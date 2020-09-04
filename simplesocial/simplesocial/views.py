from django.views.generic import TemplateView

# will go here after logging in.. since did not create model.. so settig where to go after loggin here
class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'    

class HomePage(TemplateView):
    template_name = 'index.html'
