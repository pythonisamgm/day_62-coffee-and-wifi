# Project Name

This project is a Flask web application utilizing Flask-WTF extension and WTForms for form handling. It provides an easy form of validation, requires less code, and includes built-in CSRF protection.

## Requirements

- Python 3.x
- Bootstrap_Flask 2.2.0
- Flask 2.3.2
- WTForms 3.1.2
- Flask-WTF 1.2.1
- Werkzeug 3.0.1

## Installation

1. Create a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

2. Install requirements:
    ```bash
    pip install bootstrap-flask==2.2.0 Flask==2.3.2 WTForms==3.1.2 Flask-WTF==1.2.1 Werkzeug==3.0.1
    ```

## Usage

1. Create a class with FlaskForm in `main.py`.
2. Create the form in an HTML file. Include `NOVALIDATE` to prevent automatic responses in the explorer. Here's an example of how to manually add the form:

    ```html
    <form method="post" action="">
        {{ form.csrf_token }}
        {{ form.email.label }}
        {{ form.email(size=30) }}
    </form>
    ```

3. Add validation to forms:
   - Add Validator objects inside the `FlaskForm` class. For example:
     ```python
     email = StringField(label='Email', validators=[DataRequired(), Email(message="That's not an email address")])
     ```
   - In the HTML file, display form errors:
     ```html
     {% for err in form.email.errors %}
         {{ err }}
     {% endfor %}
     ```

4. In `main.py`, add `validate_on_submit` to handle form submission.

5. Use Jinja2 to inherit templates. Parent HTML style (`base.html`) is inherited by child HTML using `{% extends "base.html" %}`.

To use Bootstrap Flask as an inherited template:
1. Install Bootstrap Flask:
    ```bash
    pip install bootstrap-flask
    ```
2. Initialize Bootstrap Flask in `main.py`:
    ```python
    from flask_bootstrap import Bootstrap5
    bootstrap = Bootstrap5()
    ```
3. In the parent HTML:
    ```html
    {{ bootstrap.load_css() }}
    <!-- inside block styles (head) -->
    {{ bootstrap.load_js() }}
    <!-- inside block scripts (body) -->
    ```

## Contributing

Feel free to contribute to this project by reporting issues, suggesting enhancements, or submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
