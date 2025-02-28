from flask import Flask , request , render_template , redirect , jsonify

from forms import PatientForm,Search
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


DATABASE_URL = 'sqlite:///lab.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# database model

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer , primary_key=True, autoincrement=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(30))
    password = db.Column(db.String(6))
    confirm_password =db.Column(db.String(6))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    uniqe_id = db.Column(db.Integer)
    birth_day = db.Column(db.Date)

    def __repr__(self):
        return f'Patient {self.username}'


with app.app_context():
    db.create_all()




# ===================================

users = []

@app.route('/commoninfo' , methods = ['GET'])
def welcom():
    return f'Welcom' 




@app.route('/commoninfo/add' , methods = ['GET' , 'POST'])
def signup():
    form = PatientForm()
    if request.method == 'GET':
        return render_template('signup.html' , form=form)
    
    elif request.method == 'POST' and form.validate_on_submit() :
        username = form.username.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        uniqe_id = form.uniqe_id.data
        birth_day = form.birth_day.data
        
        user = Patient(username=username, email=email, password=password, confirm_password=confirm_password, first_name=first_name, last_name=last_name , uniqe_id=uniqe_id, birth_day=birth_day)
        
        
        uid = Patient.query.filter_by(uniqe_id=uniqe_id).first()

        if uid:
            return f'That Uniqe ID already exists. Please choose a different one.'
        else:
    
            db.session.add(user)
            db.session.commit()
            
            users.append({
                'username': username,
                'email': email,
                'password': password,
                'confirm_password': confirm_password,
                'first_name': first_name,
                'last_name': last_name,
                'uniqe_id': uniqe_id,
                'birth_day': birth_day
            })
    
        return redirect('/commoninfo/fetch')
         
            
            
            
@app.route('/all', methods=['GET', 'POST'])
def mypatient():
    form = PatientForm()
    if request.method == 'GET':
        
        user = Patient.query.all()
        return jsonify({"user": users})
    
    elif request.method == 'POST':
        
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        confirm_password = request.json.get('confirm_password')
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        uniqe_id = request.json.get('uniqe_id')
        birth_day = request.json.get('birth_day')
                
        user = Patient(username=username, email=email, password=password, confirm_password=confirm_password, first_name=first_name, last_name=last_name, uniqe_id=uniqe_id, birth_day=birth_day)
        db.session.add(user)
        db.session.commit()
        
        users.append({
            'username': username,
            'email': email,
            'password': password,
            'confirm_password': confirm_password,
            'first_name': first_name,
            'last_name': last_name,
            'uniqe_id': uniqe_id,
            'birth_day': birth_day
        })

        
        return jsonify({'message': 'Employee Added Successfully', 'Users': users})







@app.route('/commoninfo/fetch', methods=['GET'  , 'POST'])       
def search():
    form = Search()
    if request.method == 'GET':
        return render_template('login.html' , form=form)
    if request.method == 'POST':
        uniqe_id = request.form['uniqe_id']
        
        user = Patient.query.filter_by(uniqe_id=uniqe_id).first()
        if user:
            return f'User Name: {user.username}  Uniqe ID: {user.uniqe_id} BirthDay: {user.birth_day}'
        else:
            return f'this user not found'


if __name__ == '__main__':    
    app.run(debug=True)








