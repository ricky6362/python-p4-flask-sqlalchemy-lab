from flask import Flask, make_response
from flask_migrate import Migrate
from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.get(id)
    if animal:
        response = f"Animal ID: {animal.id}<br>"
        response += f"Name: {animal.name}<br>"
        response += f"Species: {animal.species}<br>"
        response += f"Zookeeper ID: {animal.zookeeper_id}<br>"
        response += f"Enclosure ID: {animal.enclosure_id}"
        return make_response(response)
    return "Animal not found", 404

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.get(id)
    if zookeeper:
        response = f"Zookeeper ID: {zookeeper.id}<br>"
        response += f"Name: {zookeeper.name}<br>"
        response += f"Birthday: {zookeeper.birthday}<br>"
        response += "Animals they take care of:<br>"
        for animal in zookeeper.animals:
            response += f"- {animal.name}<br>"
        return make_response(response)
    else:
        return "Zookeeper not found", 404

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.get(id)
    if enclosure:
        response = f"Enclosure ID: {enclosure.id}<br>"
        response += f"Environment: {enclosure.environment}<br>"
        response += f"Open to Visitors: {enclosure.open_to_visitors}<br>"
        response += "Animals in the enclosure:<br>"
        for animal in enclosure.animals:
            response += f"- {animal.name}<br>"
        return make_response(response)
    else:
        return "Enclosure not found", 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
