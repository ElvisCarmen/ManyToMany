from src.modelo.base import Base, engine, session
from src.modelo.Actor import Actor
from src.modelo.Movie import Movie
from src.modelo.base import session
from src.logica.PersistenciaActor import PersistenciaActor
from src.logica.PersistenciaMovie import PersistenciaMovie

def almacenar():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaActor = PersistenciaActor()
    persistenciaMovie = PersistenciaMovie()

    # crear Article
    actor1 = Actor(titulo="Nombre del Actor")
    actor2 = Actor(titulo="Elvis Carmen")
    session.add(actor1)
    session.add(actor2)
    session.commit()

    # crear Comment
    movie1 = Movie(comentario="Pedro Cardenas")
    movie2 = Movie(comentario="Buen Tipo")
    session.add(movie1)
    session.add(movie2)
    session.commit()

    # Relacionar articulos con commentarios
    actor1.comments = [movie2]
    actor2.comments = [movie1]
    session.commit()

    persistenciaActor.VerFilas()
    persistenciaMovie.VerFilas()

    session.close()

def almacenarPersitencia():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    persistenciaActor = PersistenciaActor()
    persistenciaMovie = PersistenciaMovie()

    # crear Article
    persistenciaActor.agregarActor(titulo="Aplicaciones de ML en medicina")
    persistenciaActor.agregarActor(titulo="Ingeniería de software ágil")
    actor1 = persistenciaActor.dar_id(1)
    actor2 = persistenciaActor.dar_id(2)

    # crear Comment
    persistenciaMovie.agregarMovie(comentario="Es un artículo de revisión")
    persistenciaMovie.agregarMovie(comentario="Buen artículo")
    movie1 = persistenciaMovie.dar_id(1)
    movie2 = persistenciaMovie.dar_id(2)

    # Relacionar articulos con commentarios
    actor1.comments = [movie2]
    actor2.comments = [movie1]
    session.commit()

    persistenciaActor.VerFilas()
    persistenciaMovie.VerFilas()

    session.close()

if __name__ == '__main__':
   #almacenar()
   almacenarPersitencia()