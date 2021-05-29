import pprint
import pprintpp
from omdbapi.movie_search import GetMovie
movie = GetMovie(title='Interstellar', api_key='e26e533a', plot='full')
movie.get_all_data()
pprint.pprint(movie.get_all_data())

