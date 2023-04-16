from flask import Flask, render_template, redirect
from data import db_session, jobs_api
from data.jobs import Jobs
from data.users import User
from data.departaments import Department
from flask_login import LoginManager, login_user
from forms.login_form import LoginForm
from forms.add_job_form import JobForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


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


@app.route('/distribution')
def distribution():
    list_users = [
        'Ридли Скотт',
        'Энди Уир',
        'Марк Уотни',
        'Венката Капур',
        'Тедди Сандерс',
        'Шон Бин'
    ]
    return render_template('distribution.html', list_users=list_users)


@app.route('/')
def index():
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
    return render_template('index.html', listProf=listProf, title="Главная")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/add_job', methods=['GET', 'POST'])
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = Jobs(
            team_leader=form.team_leader.data,
            job=form.job.data,
            work_size=form.work_size.data,
            collaborators=form.collaborators.data,
            is_finished=form.is_finished.data)
        db_sess.add(job)
    return render_template('job.html', title='Добавление работы', form=form)


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    app.register_blueprint(jobs_api.blueprint)
    app.run()


if __name__ == '__main__':
    main()
