from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView



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


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie
    paginate_by = 2

# extra_context = {'object_list': Movie.objects.all()}

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


def hello(request):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s1, 'beautiful', 'wonderful', 'great'],
                 'title': s1}
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
