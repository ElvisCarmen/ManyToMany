from src.modelo.Actor import Actor
from src.modelo.Movie import Movie
from sqlalchemy.exc import SQLAlchemyError
from src.modelo.base import session

class PersistenciaActor():
    def agregarActor(self, titulo):
        busqueda = session.query(Actor).filter(Actor.titulo == titulo).all()
        if len(busqueda) == 0:
            actor = Actor(titulo=titulo)
            session.add(actor)
            session.commit()
            return True
        else:
            return False

    def VerFilas(self):
        actores = session.query(Actor).all()
        print('\n### actores:')
        for actor in actores:
            print(f'id: {Actor.id} Título: {Actor.titulo}')
        print('')

    def eliminarFilaAFila(self):
        actores = session.query(Actor).all()
        for actor in actores:
            session.delete(actor)
        session.commit()

    def eliminarFilaSQL(self):
        sentencia = "DELETE  from articles"
        try:
            data_source = session.execute(sentencia)
            session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
        else:
            print("Tabla actores")
            print("Nro de registros borrados : ", data_source.rowcount)


    def dar_id(self, id):
        return session.query(Actor).get(id)