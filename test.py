from Scrapping import *





f = FilmList(2018)
#f.download_html()
id = f.get_films_ids()

f1 = Film(id)
print(type(f1))


f1.download_html()
f1.download_actors_html()
f1.get_actors_url()

#film.download_actors_html()
#actor_url = film.get_actors_url()

#film.scrap()
#actors = film.get_actors()
#film.get_amount()


