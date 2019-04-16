from flask import Flask, render_template, request, jsonify

from app.grandpy_bot import GrandPyBot


app = Flask(__name__)


@app.route('/')
def page():
    return render_template('page.html')


@app.route('/answer')
def generate_answer():
    bot = GrandPyBot(request.args.get('question'))
    return jsonify(bot.return_data())


if __name__ == "__main__":
    app.run()

