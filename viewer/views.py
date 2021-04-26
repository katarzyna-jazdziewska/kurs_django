from logging import getLogger

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import (TemplateView,
                                  ListView,
                                  CreateView,
                                  DetailView,
                                  FormView,
                                  UpdateView,
                                  DeleteView
                                  )
from viewer.forms import MovieForm

'''
Pierwszy sposób przekazywania parametru s, wtedy trzeba w urlsach w ścieżce dać 'hello/<s>'
def hello(request, s):
    return HttpResponse(f'Hello, {s} world!')
    
def hello(request):
    s = request.GET.get('s', '')
    # w = request.GET.get('w', 'nie ma W')
    tekst = f"<b> Hello, {s} world! </b><br>" \
    #        f"{request.headers}"
            f"{request.META['REMOTE_ADDR']}"
    return HttpResponse(tekst)
    
    
    
    
def hello(request):
    try:
        s = int(request.GET.get('s', '')) + 10
    except Exception as ex:
        return HttpResponse(f"Coś poszło nie tak! Błąd: {ex}")

    tekst = f"Wartość o 10 większa: {s}"
    return HttpResponse(tekst)
    
'''

LOGGER = getLogger()


class IndexView(TemplateView):
    template_name = 'index.html'


class MovieDetailsView(DetailView):
    template_name = 'detail.html'
    model = Movie
    extra_context = {'lista': ['Dramat', 'Komedia', 'Sci-Fi', 'Historyczny', 'Thriller', 'Horror']}


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('viewer:movie')
    permission_required = 'viewer.delete_movie'


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('viewer:movie')
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a movie.')
        return super().form_invalid(form)


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie
    paginate_by = 200   # w adresie strony ?page=2 przerzuca na drugą stronę

# extra_context = {'object_list': list(Movie.objects.all())}    -> to się dzieje w tle


# FormView -> CreateView i wtedy można usunąć def form_valid
class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('viewer:movie_create')
    permission_required = 'viewer.add_movie'

    # def form_valid(self, form):
    #     result = super().form_valid(form)
    #     cleaned_data = form.cleaned_data
    #     Movie.objects.create(
    #         title=cleaned_data['title'],
    #         genre=cleaned_data['genre'],
    #         rating=cleaned_data['rating'],
    #         released=cleaned_data['released'],
    #         description=cleaned_data['description']
    #     )
    #     return result

    def form_invalid(self, form):
        LOGGER.warning('User provided an invalid data!')
        return super().form_invalid(form)

#
# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all().order_by('-released'),
#                      'title': "Wynik TemplateView"}



# class MoviesView(View):
#
#     def get(self, request):
#         return render(
#             request, template_name="movies.html",
#             context={'movies': Movie.objects.all().order_by('-released')}
#         )


# w context można też dać np. filter(genre__name=gatunek)


def movies(request):
    gatunek = request.GET.get('gatunek', '')
    return render(
        request, template_name="movies.html",
        context={'movies': Movie.objects.all().order_by('-released')}
    )


@login_required
def hello(request):
    s1 = request.GET.get('s1', '')
    user = request.user
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s1, 'beautiful', 'wonderful', 'great'],
                 'title': s1,
                 'user': user}
        )



    # try:
    #     s = int(request.GET.get('s', ''))
    # except Exception as ex:
    #     return HttpResponse(f"Coś poszło nie tak! Błąd: {ex}")
    #
    # tekst = f"<b>Wartość s={s}</b><br>" \
    #         f"<a href='/hello/?s={s+1}'>link zwiększający o 1</a><br>" \
    #         f"<a href='/hello/?s={s-1}'>link zmniejszający o 1</a>"
    # return HttpResponse(tekst)
