from src.modelo.Actor import Actor
from src.modelo.Movie import Movie
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.base import Session, engine, Base

class PersistenciaMovie():
    def agregarMovie(self, comentario):

        if len(comentario) > 0:
            movie = Movie(comentario=comentario)
            session.add(movie)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        movies = session.query(Movie).all()
        print('\n### Movies:')
        for movie in movies:
            print(f'id: {movie.id} Comentario: {movie.comentario}, del artículo: {comment.article_id}')
        print('')

    def eliminarFilaAFila(self):
        movies = session.query(Movie).all()
        for movie in movies:
            session.delete(movies)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from movies"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla movies")
            print("Nro de registros borrados : ", data_source.rowcount)

    def dar_id(self, id):
        return session.query(Movie).get(id)