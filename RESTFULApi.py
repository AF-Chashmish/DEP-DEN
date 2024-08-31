from flask import Flask, request
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

data = [
    {'id': 1, 'name': 'User 1', 'age': 42},
    {'id': 2, 'name': 'User 2', 'age': 74}
]

def find_person(person_id):
    for person in data:
        if person['id'] == person_id:
            return person
        else:
            return None

# Get, post, put/patch, delete
class PeopleResource(Resource):
    def get(self):
        return data
    def post(self):
        new_person = {
            'id': len(data)+1,
            'name': 'User 3',
            'age': 39
        }
        data.append(new_person)
        return new_person, 201

class PersonResource(Resource):
    def get(self, person_id):
        person = find_person(person_id)
        if person:
            return person
        return {"message": "Person not found."}, 404

    def put(self, person_id):
        person = find_person(person_id)
        if person:
            person['name'] = request.json['name']
            person['age'] = request.json['age']
            return person
        return {"message": "Person not found."}, 404
    def delete(self, person_id):
        global data
        data = [person for person in data if person['id'] != person_id]
        return {"messsage": "Person deleted successfully."}, 200

api.add_resource(PeopleResource, '/people')
api.add_resource(PersonResource, '/people/<int:person_id>')

if __name__ == '__main__':
    app.run(debug = True)
