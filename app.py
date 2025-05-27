from flask import Flask, render_template, jsonify, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'electrosharma874@gmail.com'
app.config['MAIL_PASSWORD'] = 'lpna gtyj sgna vimh'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# @app.route("/Contact", methods=["GET", "POST"])

partners = [
    {
        "partnerName": "BloggingSharma",
        "partnerLink": "https://bloggingsharma.com",
    },
    {
        "partnerName": "AgentSharma",
        "partnerLink": "https://Agentsharma.com",
    },
    {
        "partnerName": "MultiSharma",
        "partnerLink": "https://Multisharma.com",
    },
    {
        "partnerName": "HackerSharma",
        "partnerLink": "https://Hackersharma.com",
    },
]

print(partners)


@app.route("/")
def hello_world():
    return render_template("home.html",
                           webName="BloggingSharma",
                           partner=partners)


@app.route("/python")
def python_page():
    return render_template("python_nav.html",
                           webName="BloggingSharma",
                           partner=partners,
                           name="python")


@app.route("/flask")
def flask_page():
    return render_template("flask_nav.html",
                           webName="BloggingSharma",
                           partner=partners,
                           name="flask")


@app.route("/c")
def c_page():
    return render_template("C_nav.html",
                           webName="BloggingSharma",
                           partner=partners,
                           name="C")


@app.route("/webDev")
def webDev_page():
    return render_template("webDev_nav.html",
                           webName="BloggingSharma",
                           partner=partners,
                           name="WebDev")


@app.route("/Sign In")
def Sign():
    return render_template("login_sign.html",
                           webName="BloggingSharma",
                           partner=partners,
                           name="WebDev")


@app.route("/Contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("FirstName")
        email = request.form.get("Email")
        phone = request.form.get("PhoneNumber")
        message = request.form.get("Query")

        msg = Message(
            subject=f"Mail from {name}",
            body=
            f"Name: {name}\nE-mail: {email}\nPhone: {phone}\n\n\n{message}",
            sender=email,
            recipients=['electrosharma874@gmail.com'])
        mail.send(msg)

        return render_template("contact.html",
                               webName="BloggingSharma",
                               partner=partners,
                               name="WebDev",
                               success=True)

    return render_template("contact.html",
                           webName="BloggingSharma",
                           partner=partners,
                           name="WebDev")


@app.route("/partners")
def partner():
    return jsonify(partners)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8010)
