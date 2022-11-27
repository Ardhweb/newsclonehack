from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView
from links.models import LinkU

def home(request):
    return render(request,'home.html')


class NewLinkView(CreateView):
    model = LinkU
    fields = ('title', 'url')
    template_name = 'new_submission.html'


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewLinkView, self).dispatch(*args,**kwargs)
    

    def form_valid(self, form):
        new_link = form.save(commit=False)
        new_link.submit_from = self.request.user
        new_link.save()
        self.object = new_link
        return HttpResponseRedirect(self.get_success_url())
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.pk})
        
    # def get_success_url(self):
    #     return reverse('home')


class LinkDetailView(DetailView):
    model = LinkU
    template_name =  "link_detail.html"


    