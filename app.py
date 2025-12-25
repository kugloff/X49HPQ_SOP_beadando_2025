from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sajatlista.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = "titkos"

db = SQLAlchemy(app)
jwt = JWTManager(app)

swagger = Swagger(app, template_file='swagger.yaml')

class Film(db.Model):
    __tablename__ = "filmek"
    film_id = db.Column(db.String, primary_key=True)
    film_title = db.Column(db.String, nullable=False)
    genre = db.Column(db.String, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    premiere = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    series_movie = db.Column(db.String, nullable=False)
    picture = db.Column(db.String, nullable=False)
    in_my_list = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            "film_id": self.film_id,
            "film_title": self.film_title,
            "genre": self.genre,
            "length": self.length,
            "premiere": self.premiere,
            "date": self.date,
            "series_movie": self.series_movie,
            "picture": self.picture,
            "in_my_list": self.in_my_list
        }

@app.route("/")
def index():
    return jsonify({"message": "API fut. Dokumentáció: /apidocs"})

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if data.get("username") == "admin" and data.get("password") == "admin":
        token = create_access_token(identity="admin")
        return jsonify({"access_token": token}), 200
    return jsonify({"msg": "Hibás adatok"}), 401

@app.route("/sajatlista", methods=["GET"])
def get_sajatlista():
    filmek = Film.query.all()
    result = []
    for film in filmek:
        result.append(film.to_dict())
    return jsonify(result), 200

@app.route("/sajatlista", methods=["POST"])
@jwt_required()
def create_film():
    data = request.get_json()
    if Film.query.get(data.get("film_id")):
        return jsonify({"message": "ID már létezik"}), 400
    try:
        new_film = Film(
            film_id=data.get("film_id"),
            film_title=data.get("film_title"),
            genre=data.get("genre"),
            length=data.get("length"),
            premiere=data.get("premiere"),
            date=data.get("date"),
            series_movie=data.get("series_movie"),
            picture=data.get("picture"),
            in_my_list=data.get("in_my_list", False)
        )
        db.session.add(new_film)
        db.session.commit()
        return jsonify({"message": "Hozzáadva"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 400

@app.route("/sajatlista/<film_id>", methods=["PUT"])
@jwt_required()
def update_film(film_id):
    data = request.get_json()
    film = Film.query.get(film_id)
    if not film: 
        return jsonify({"message": "Nincs ilyen film"}), 404

    if "film_title" in data: film.film_title = data["film_title"]
    if "genre" in data: film.genre = data["genre"]
    if "length" in data: film.length = data["length"]
    if "premiere" in data: film.premiere = data["premiere"]
    if "date" in data: film.date = data["date"]
    if "series_movie" in data: film.series_movie = data["series_movie"]
    if "picture" in data: film.picture = data["picture"]
    if "in_my_list" in data: film.in_my_list = data["in_my_list"]
    
    db.session.commit()
    return jsonify({"message": "Frissítve"}), 200

@app.route("/sajatlista/<film_id>", methods=["DELETE"])
@jwt_required()
def delete_film(film_id):
    film = Film.query.get(film_id)
    if not film: 
        return jsonify({"message": "Nincs ilyen film"}), 404
    db.session.delete(film)
    db.session.commit()
    return jsonify({"message": "Törölve"}), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port=3010, debug=True)