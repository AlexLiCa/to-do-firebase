
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

cred = credentials.Certificate("firebase-key.json")
fire = firebase_admin.initialize_app(cred)

db = firestore.client() #comunicacion con la base de datos 

tasks_ref = db.collection('tasks') #referencia a la colleccion de firebase

docs = tasks_ref.stream() #este objeto es una especie de lista  se puede mantener un tunel con mi aplicacion 
#docs = tasks_ref.get()  este objeto es una especie de lista  hace un snapshot en el momento y se tiene que refrescar para actualizar 
def read_tasks():
    for task in docs:
        print(f"ID{task.id}")

def read_task(id):
    task = tasks_ref.document(id).get() #leer una solo un documento de firebase 
    print(task.to_dict())

def create_task(name):
    task = {
    'name': name,
    'check': False,
    'date':datetime.datetime.now()
}
    tasks_ref.document().set(task)

def update_task(id):
    tasks_ref.document(id).update({'check': True})

def delete_task(id):
    tasks_ref.document(id).delete()

def get_completed():
    completed = tasks_ref.where('check','==', True).get()


# create_task(new_task)
# update_task('3r8zqTLD2o2AJWLNMOFs')
# delete_task('3r8zqTLD2o2AJWLNMOFs')

name = input('Ingrese el nombre de la tarea: ')

create_task(name) 

