from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgfh78@#5?>gfhf89dx,v06k'

menu = [{"name": "Установка", "url": "install-flask"},
        {"name": "Первое приложение", "url": "first-app"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
def index():
    return render_template('index.html', title="Про Flask.", menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title="О сайте.", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')

    return render_template('contact.html', title="Обратная связь.", menu=menu)


@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username="CryptoLis"))


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404


if __name__ == "__main__":
    app.run(debug=True)
