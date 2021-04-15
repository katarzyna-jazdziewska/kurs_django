

model (ORM) ->
    -> python manage.py makemigrations
    -> python manage.py migrate
po tym mamy tabele w DB

1. (Create) Utworzyć rekordy
   # 1 sposób: Movie.objects.create(title="costam",...)
   # 2 sposób: film = Movie.objects.(title=....) -> film.save()
2. (Retrieve) Pobrać (jeden, wiele) rekordów na podstawie np. filtrowania itp.
   # Movies.objects.filter(rating__gte=6).filter(title__icontains="and")
3. (Update) Modyfikacja rekordu
   Model.objects.get(...) -> zwraca nam jeden obiekt!!
   Model.objects.filter(....) -> zwraca QuerySet (specyficzną listę obiektów/rekordów)
   
Movie.objects.filter(id=2).update(rating=9)

4. (Delete) Usuwanie rekordu
# 1 sposób: Movie.objects.get(title="Matrix").delete()
# 2 sposób: filmy = filmy.get(id=6)
# >>> filmy
# <Movie: Movie object (6)>
# >>> filmy.delete()

