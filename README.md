For this project I used Flask-WTF extension and WTForms. It has an easy form of validation, needs less code and has a built in CSRF Protection. 
Requirements are: 
  Bootstrap_Flask 2.2.0
  Flask 2.3.2
  WTForms 3.1.2
  Flask_WTF 1.2.1
  Werkzeug 3.0.1

1)create a venv environment (1. python -m venv venv; 2. .\venv\Scripts\activate)
2)install requirements. I had experienced some problems with watchdog
3)create a class with FlaskForm in main.py
4)create the form in html file. Its important to include NOVALIDATE, so explorer doesn't automatically give a response. 
Here I include how to add the form manually. In "add.html" I include the short version (render_form(form)).
  <form action= "{{ url_for('function' }} "novalidate" method="POST">
  {{form.csrf_token}}
  <p>{{ form.email.label }} <br> {{ form.email (size=30) }}</p>
5)Add validation to forms. Email validator requires to install an extra package. 
  1. Add Validator objects inside the flaskform class. E.g: email = StringField(label='Email', validators=[DataRequired(), Email(message="That's not an email address")])
  2. html file  form.<field>.errors
    {% for err in form.email.errors%}
    <span style="color-red"> {{ err }}</span>
    {% endfor %}
6) In the main.py file, add "validate_on_submit". To get hold of data you use <form.object>.<form.field>.data
7) I have used jinja2 to inherite templates. So there is a parent html style ("base.html") inherited by child html using {% extends "base.html" %}
To use bootstrap flask as an inherited template
  1) installation: pip install bootstrap-flask
  2)initialization: 
    from flask_bootstrap import Bootstrap5
    bootstrap = Bootstrap5
  3) in parent html:
    {{ bootstrap.load_css() }} ---------->inside block styles (head)
    {{ bootstrap.load_js() }}  ---------->inside block scripts (body)
