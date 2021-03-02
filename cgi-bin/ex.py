import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index1.html', title='Домашняя страница',
                           username=user)


@app.route('/index1')
def index1():
    param = set()
    param = {
        'username': "lepexey",
        'title': 'Домашняя страница'}
    return render_template('index1.html', **param)


@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)
    # {% if условие_1 %}
    #        ветка 1
    #  {% elif условие_2 %} (не обязательно)
    #        ветка 1
    # {% else %} (не обязательно)
    #       ветка 2
    # {% endif %}


@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    # print(news_list)
    return render_template('news.html', news=news_list)
    # {% for переменная цикла in набор значений %}
    #     код
    # {% endfor %}


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
