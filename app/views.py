from flask import Flask, render_template, request, jsonify

from app.grandpy_bot import GrandpyBot


app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def page():
    return render_template('page.html')


@app.route('/', methods=['POST'])
def generate_answer():
    bot = GrandpyBot()
    return jsonify({'answer': bot.answer(request.form['question'])})


if __name__ == "__main__":
    app.run()

