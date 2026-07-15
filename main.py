from flask import Flask
import random
app = Flask(__name__)
my_fakts = ["Я низкий",
            "Я чуть ленивый",
            "Я ненавижу английский",
            "Я не левый",
            "Я не правый"]
@app.route("/")
def hello_world():
    return random.choice(my_fakts)
films = ["Мои фильмы",
         "На западном фронте без перемен",
         "Южный парк",
         "Мистр пиклз",
         "Оно",
         "CCCP забытые вожди"]
@app.route("/film")
def hello_worldd():
    return films
if __name__ == "__main__":
    app.run(debug=True)