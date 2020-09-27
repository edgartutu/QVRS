# set up  db in __init__.py under my projects folder

from project import db, login_manager,app,login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,current_user,login_user,logout_user
from flask_admin.contrib.sqla import ModelView
from wtforms import form, fields, validators
from flask_admin import Admin

# from flask_admin import AdminIndexView

import os
from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

import flask_admin as admins
import flask_login as login
from flask_admin.contrib import sqla
from flask_admin import helpers, expose
from werkzeug.security import generate_password_hash, check_password_hash
        
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    def __init__(self,first_name,last_name,login,email, password):
        self.first_name = first_name
        self.last_name=last_name
        self.login=login
        self.email=email
        self.password = password

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        # if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(form.Form):
    first_name = fields.StringField()
    last_name = fields.StringField()
    login = fields.StringField(validators=[validators.required()])
    email = fields.StringField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise validators.ValidationError('Duplicate username')


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


# Create customized model view class
class MyModelView(sqla.ModelView):

    def is_accessible(self):
        return login.current_user.is_authenticated


# Create customized index view class that handles login & registration
class MyAdminIndexView(admins.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login.login_user(user)

        if login.current_user.is_authenticated:
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User(first_name=form.first_name.data,last_name=form.last_name.data,login=form.login.data,email=form.email.data,password=form.password.data)

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login.login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        login.logout_user()
        return redirect(url_for('.index'))


# Flask views
@app.route('/')
def index():
    return render_template('index.html')


# Initialize flask-login
init_login()

# Create admin
# admin = admin.Admin(app)
admin=Admin(app, 'EC-ADMIN', index_view=MyAdminIndexView(), base_template='my_master.html')
# Add view
# admin.add_view(MyModelView(User, db.session))




class Admin_Headquaters(db.Model, UserMixin):
    admin_email = db.Column(db.String(64), primary_key=True, unique=True, index=True)
    admin_Name= db.Column(db.String(100))
    publicID = db.Column(db.String(100))
    password = db.Column(db.String(128))


    def __init__(self, admin_email,admin_Name, password):
        self.admin_email = admin_email
        self.admin_Name=admin_Name
        self.password = password

    def json(self):
        return {'admin_email':self.admin_email,'admin_name':self.admin_Name,'password':self.password}

    def check_password(self,password):     
        return check_password_hash(self.password,password)





class District(db.Model,UserMixin):
    __tablename__ = "District"
    id = db.Column(db.Integer,primary_key=True)
    DistrictName = db.Column(db.String(100))

    def __init__(self,DistrictName):
        self.DistrictName = DistrictName
        #self.id = id

    def json(self):
        return {'DistrictName':self.DistrictName,'id':id}

class Subcounty(db.Model,UserMixin):
    __tablename__ = "Subcounty"
    id = db.Column(db.Integer,primary_key=True)
    SubCountyName = db.Column(db.String(100))
    DistrictID = db.Column(db.String(100))

    def __init__(self,SubCountyName,DistrictID):
        self.SubCountyName = SubCountyName
        self.DistrictID = DistrictID

    def json(self):
        return {'SubCountyName':self.SubCountyName,'DistrictID':self.DistrictID}

class Parish(db.Model,UserMixin):
    __tablename__ = "Parish"
    id = db.Column(db.Integer,primary_key=True)
    ParishName = db.Column(db.String(100))
    SubCountyID = db.Column(db.String(100))
    DistrictID = db.Column(db.String(100))

    def __init__(self,ParishName,SubCountyID,DistrictID):
        self.ParishName = ParishName
        self.SubCountyID = SubCountyID
        self.DistrictID = DistrictID

    def json(self):
        return {'ParishName':self.ParishName,'SubCountyID':self.SubCountyID,'DistrictID':self.DistrictID,'id':id}

class PollingStation(db.Model,UserMixin):
    __tablename__ = "Polling Station"
    id = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(100))
    ParishID = db.Column(db.String(100))
    SubCountyID = db.Column(db.String(100))
    DistrictID = db.Column(db.String(100))
    file=db.Column(db.String(100))

    def __init__(self,Name,ParishID,SubCountyID,DistrictID,file):
        self.Name = Name
        self.ParishID = ParishID
        self.SubCountyID = SubCountyID
        self.DistrictID = DistrictID
        self.file=file

    def json(self):
        return {'PollingStationName':self.Name,'ParishID':self.ParishID,'SubCountyID':self.SubCountyID,'DistrictID':self.DistrictID,'file':self.file}

class PollingCategory(db.Model,UserMixin):
    __tablename__ = "Polling Category"
    id = db.Column(db.Integer,primary_key=True)
    Category = db.Column(db.String(100))

    def __init__(self,Category):
        self.Category = Category

    def json(self):
        return {'Category':self.Category,'id':id}

class Candidate(db.Model,UserMixin):
    __tablename__ = "Candidate"
    id = db.Column(db.Integer,primary_key=True)
    Name = db.Column(db.String(100))
    Photo = db.Column(db.String(100))
    Category = db.Column(db.String(100))
    LocationID = db.Column(db.String(100))

    def __init__(self,Name,Photo,Category,LocationID):
        self.Name = Name
        self.Photo = Photo
        self.Category = Category
        self.LocationID = LocationID

    def json(self):
        return {'Name':self.Name,'Photo':self.Photo,'Category':self.Category,'LocationID':self.LocationID}

class PollingData(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    CandidateID = db.Column(db.String(100))
    CategoryID = db.Column(db.String(100))
    PollingStationID = db.Column(db.String(100))
    PollingResults = db.Column(db.String(100))

    def __init__(self,CandidateID,CategoryID,PollingStationID,PollingResults):
        self.CandidateID = CandidateID
        self.CategoryID = CategoryID
        self.PollingStationID = PollingStationID
        self.PollingResults = PollingResults

    def json(self):
        return {'CandidateID':self.CandidateID,'CategoryID':self.CategoryID,'PollingStationID':self.PollingStationID,'PollingResults':self.PollingResults}

class Results (db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    DISTRICT_CODE= db.Column(db.String(100))
    DISTRICT_NAME = db.Column(db.String(100))
    EA_CODE= db.Column(db.Integer)
    EA_NAME = db.Column(db.String(100))
    SCOUNTY_CODE = db.Column(db.Integer)
    SCOUNTY_NAME = db.Column(db.String(100))
    PARISH_CODE = db.Column(db.Integer)
    PARISH_NAME = db.Column(db.String(100))
    PS_CODE = db.Column(db.Integer)
    PS_NAME=db.Column(db.String(100))
    KT = db.Column(db.Integer)
    cand1 = db.Column(db.Integer)
    cand2 = db.Column(db.Integer)
    cand3 = db.Column(db.Integer)
    cand4 = db.Column(db.Integer)
    cand5 = db.Column(db.Integer)
    cand6 = db.Column(db.Integer)
    cand7 = db.Column(db.Integer)
    cand8 = db.Column(db.Integer)
    VALID_VOTE = db.Column(db.Integer)
    SPOILT_BALLOT = db.Column(db.Integer)
    INVALID_VOTE = db.Column(db.Integer)
    TOTAL_VOTE = db.Column(db.Integer)
                         
                        

    def __init__(self,DISTRICT_CODE,DISTRICT_NAME,EA_CODE,EA_NAME,SCOUNTY_CODE,SCOUNTY_NAME
                 ,PARISH_CODE,PARISH_NAME,PS_CODE,PS_NAME,KT,cand1,cand2,cand3,cand4,cand5,cand6,cand7,cand8,VALID_VOTE,SPOILT_BALLOT,INVALID_VOTE,TOTAL_VOTE):
        self.DISTRICT_CODE= DISTRICT_CODE
        self.DISTRICT_NAME= DISTRICT_NAME
        self.EA_CODE= EA_CODE
        self.EA_NAME = EA_NAME
        self.SCOUNTY_CODE = SCOUNTY_CODE
        self.SCOUNTY_NAME = SCOUNTY_NAME
        self.PARISH_CODE = PARISH_CODE
        self.PARISH_NAME = PARISH_NAME
        self.PS_CODE = PS_CODE
        self.PS_NAME=PS_NAME
        self.KT = KT
        self.cand1 = cand1
        self.cand2 = cand2
        self.cand3 = cand3
        self.cand4 = cand4
        self.cand5 = cand5
        self.cand6 = cand6
        self.cand7 = cand7
        self.cand8 = cand8
        self.VALID_VOTE = VALID_VOTE
        self.SPOILT_BALLOT = SPOILT_BALLOT
        self.INVALID_VOTE = INVALID_VOTE
        self.TOTAL_VOTE = TOTAL_VOTE
        
        

    def json(self):
        return {'DISTRICT_CODE': self.DISTRICT_CODE,'DISTRICT_NAME':self.DISTRICT_NAME,'EA_CODE':self.EA_CODE,'EA_NAME':self.EA_NAME,"SCOUNTY_CODE":self.SCOUNTY_CODE
                ,"SCOUNTY_NAME":self.SCOUNTY_NAME,"PARISH_CODE":self.PARISH_CODE,"PARISH_NAME":self.PARISH_NAME,"PS_CODE":self.PS_CODE,"PS_NAME":self.PS_NAME,"KT":self.KT,"cand1":self.cand1,"cand2":self.cand2,"cand3":self.cand3,
                "cand4":self.cand4,"cand5":self.cand5,"cand6":self.cand6,"cand7":self.cand7,"cand8":self.cand8,"VALID_VOTE":self.VALID_VOTE,"SPOILT_BALLOT":self.SPOILT_BALLOT,"INVALID_VOTE":self.INVALID_VOTE,
                "TOTAL_VOTE":self.TOTAL_VOTE}

class PresidentialTable(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    Key=db.Column(db.String(100))
    DISTRICT_NAME = db.Column(db.String(100))
    candate1 = db.Column(db.Integer)
    candate2 = db.Column(db.Integer)
    candate3 = db.Column(db.Integer)
    candate4 = db.Column(db.Integer)
    candate5 = db.Column(db.Integer)
    candate6 = db.Column(db.Integer)
    candate7 = db.Column(db.Integer)
    candate8 = db.Column(db.Integer)
    winner=db.Column(db.String(100))
    margin=db.Column(db.Integer)

    def __init__(self,Key,DISTRICT_NAME,candate1,candate2,candate3,candate4,candate5,candate6,candate7,candate8,winner,margin):
        self.Key=Key
        self.DISTRICT_NAME= DISTRICT_NAME
        self.candate1 = candate1
        self.candate2 = candate2
        self.candate3 = candate3
        self.candate4 = candate4
        self.candate5 = candate5
        self.candate6 = candate6
        self.candate7 = candate7
        self.candate8 = candate8
        self.winner = winner
        self.margin = margin

    def json(self):
        return {'name':self.DISTRICT_NAME,'hc-key':self.Key,"cand1":self.candate1,"cand2":self.candate2,"cand3":self.candate3,
                "cand4":self.candate4,"cand5":self.candate5,"cand6":self.candate6,"cand7":self.candate7,"cand8":self.candate8,"winner":self.winner,"value":self.margin}

       


admin.add_view(MyModelView(Admin_Headquaters,db.session))
admin.add_view(MyModelView(Results,db.session))
admin.add_view(MyModelView(PresidentialTable,db.session))  
admin.add_view(MyModelView(User,db.session))   



db.create_all()
