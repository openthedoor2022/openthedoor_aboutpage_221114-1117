from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://team:sparta@cluster0.clqmmwt.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def team():
    return render_template('index.html')


@app.route("/team", methods=["POST"])
def team_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.team.insert_one(doc)
    return jsonify({'msg': '응원 완료!'})


@app.route("/team", methods=["GET"])
def team_get():
    comment_list = list(db.team.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
