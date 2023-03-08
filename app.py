from flask import Flask, render_template


app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Заготовка')


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
