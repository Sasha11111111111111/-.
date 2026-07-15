from flask import Flask
import random
app = Flask(__name__)
films = ["Я учусь на платформе котлант, и выполняю дз на тему мои любимые фильмы и снриалы.",
         "На западном фронте без перемен, CCCP забытые вожди, я люблю сериалы и фильмы на тему истоии, политики или войны.",
         "Также мне заходят проекты от дс и марвел но я их смотрю редко.",]
@app.route("/film")
def hello_worldd():
    return films
if __name__ == "__main__":
    app.run(debug=True)
