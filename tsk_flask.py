from flask import Flask

app = Flask(__name__)


@app.route('/promotion_image')
def bootstrap():
    return f'''<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Меченый!?</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        <link rel="stylesheet" href="static/css/style.css">
    </head>
    <body>
        <h1>Короче, Меченый</h1>
        <img src="/static/img/sidor.jpg" alt="здесь должна была быть картинка, но не нашлась">
        <div class="p-3 mb-2 bg-primary text-white">Я тебя спас и в благородство играть не буду:</div>
        <div class="p-3 mb-2 bg-secondary text-white">Выполнишь для меня пару заданий — и мы в расчете.</div>
        <div class="p-3 mb-2 bg-success text-white">Заодно посмотрим,</div>
        <div class="p-3 mb-2 bg-danger text-white">Как быстро у тебя башка после амнезии прояснится.</div>
        <div class="p-3 mb-2 bg-warning text-dark">А по твоей теме постараюсь разузнать.</div>
        <div class="p-3 mb-2 bg-info text-dark">Хрен его знает, на кой ляд тебе этот Стрелок сдался,</div>
        <div class="p-3 mb-2 bg-dark text-white">Но я в чужие дела не лезу, хочешь убить, значит есть за что...</div>
    </body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
