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


@app.route("/partners")
def partner():
    return jsonify(partners)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8010)
