from flask import Flask, render_template


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Заготовка')


@app.route('/training/<string:prof>')
def training(prof):
    profs = {
        'engineer_prof': [
            'инженер-исследователь',
            'пилот',
            'строитель',
            'иженер по терраформированию',
            'инженер жизнеобеспечения',
            'оператор марсохода',
            'киберинженер',
            'штурман',
            'пилот дронов'
        ],
        'science_prof': [
            'экзобиолог',
            'врач',
            'климатолог',
            'специалист по радиационной защите',
            'астрогеолог',
            'гляциолог',
            'метеоролог'
        ]
    }

    images = {
        "engineer_prof": 'engineer.jpg',
        "science_prof": 'science.jpg'
    }

    if prof in profs['engineer_prof']:
        return render_template('training.html', img=images['engineer_prof'], title='Инженерные тренажеры')
    else:
        return render_template('training.html', img=images['science_prof'], title='Научные симуляторы')


@app.route('/list_prof/<string:typeOfList>')
def list_prof(typeOfList):
    listProf = ['инженер-исследователь',
                'пилот',
                'строитель',
                'экзобиолог',
                'врач',
                'иженер по терраформированию',
                'климатолог',
                'специалист по радиационной защите',
                'астрогеолог',
                'гляциолог',
                'инженер жизнеобеспечения',
                'метеоролог',
                'оператор марсохода',
                'киберинженер',
                'штурман',
                'пилот дронов']
    return render_template('list.html', typeOfList=typeOfList, listProf=listProf)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    information = {
        'title': 'И на Марсе будут яблони цвести!',
        'surname': 'Wathy',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True',
    }
    return render_template('auto_answer.html', information=information)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
