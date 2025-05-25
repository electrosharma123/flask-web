from flask import Flask, json, render_template, jsonify

app = Flask(__name__)

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
                           partner=partners)


@app.route("/flask")
def flask_page():
    return render_template("flask_nav.html",
                           webName="BloggingSharma",
                           partner=partners)


@app.route("/c")
def c_page():
    return render_template("C_nav.html",
                           webName="BloggingSharma",
                           partner=partners)


@app.route("/webDev")
def webDev_page():
    return render_template("webDev_nav.html",
                           webName="BloggingSharma",
                           partner=partners)


@app.route("/partners")
def partner():
    return jsonify(partners)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8010)
