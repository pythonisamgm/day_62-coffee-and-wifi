from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm
import csv

app = Flask(__name__)

bootstrap = Bootstrap5(app)
app.secret_key = "some secret key"
#app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

class Form(FlaskForm):
    cafe_name = StringField('Cafe Name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps', validators=[DataRequired()])
    opening = StringField('Opening Time e.g. 8 AM', validators=[DataRequired()])
    closing = StringField('Closing Time e.g. 8 AM', validators=[DataRequired()])
    coffee_rating = (SelectField('Coffee Rating',
                                 choices=['✘','☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️'],
                                 validators=[DataRequired()]))
    wifi_rating = SelectField('Wifi Strength Rating',
                              choices=['✘', '💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'],
                              validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability',
                               choices=['✘','🔌', '🔌🔌', '🔌🔌🔌', '🔌🔌🔌🔌', '🔌🔌🔌🔌🔌'],
                               validators=[DataRequired()])
    submit = SubmitField(label='Submit')


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/cafes")
def cafes():
    with open ("cafe-data.csv", encoding="UTF-8") as file:
        list_of_rows = []

        data = csv.reader(file, delimiter=(","))
        for row in data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template("cafes.html", cafe=list_of_rows)

@app.route('/add', methods=["GET", "POST"])
def add():
    form = Form()
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", newline='', encoding="UTF-8") as file:
            new_cafe = [form.cafe_name.data,
                        form.location.data,
                        form.opening.data,
                        form.closing.data,
                        form.coffee_rating.data,
                        form.wifi_rating.data,
                        form.power_rating.data]
            writer = csv.writer(file)
            writer.writerow(new_cafe)
        return redirect(url_for('cafes'))
    else:
        return render_template("add.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)