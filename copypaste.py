class BreakfastForm(FlaskForm):
    burger = SelectField('Quantity',
                             choices=[('cpp', 'C++')],default=0)
    cheese = SelectField('Quantity',
                             choices=[(0,1,2,3,4,5,6,7,8,9)],default=0)
    bacon = SelectField('Quantity',
                             choices=[(0,1,2,3,4,5,6,7,8,9)],default=0)
    hashbrown = SelectField('Quantity',
                             choices=[(0,1,2,3,4,5,6,7,8,9)],default=0)
#automatically log the user email and name into the form as well
    submit = SubmitField("Submit")

form.group_id.choices = [(g.id, g.name) for g in Group.query.order_by('name')]


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

@app.route('/')
def home():
    return render_template("index.html")

    <div class="container-login100-form-btn m-t-32">
        <button type="submit" class="login100-form-btn"><a href="={{ url_for('oauth_authorize', provider='google')}}" style="color:white">
            Log in with Google Account</a>
        </button>
    </div>

<a href= "/welcome" }}><img src="{{ url_for('static', filename='img/signinwithgoogle.png') }}" /></a>