from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://OPD:2022@clusteropd.h21fmkf.mongodb.net/?retryWrites=true&w=majority')
db = client.bolee


@app.route('/')
def home():
    return render_template('bolee_team_guestbook.html')


@app.route("/teamguestbook", methods=["GET"])
def bolee_get():
    comment_list = list(db.teamguestbook.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


@app.route("/teamguestbook", methods=["POST"])
def bolee_post():
    usrname_receive = request.form['usrname_give']
    cntcomment_receive = request.form['cntcomment_give']

    comment_list = list(db.teamguestbook.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'usrname': usrname_receive,
        'cntcomment': cntcomment_receive
    }
    db.teamguestbook.insert_one(doc)
    return jsonify({'msg': '방명록이 등록되었습니다.'})

@app.route("/teamguestbook/update", methods=["POST"])
def bolee_update():
    num_receive = request.form['num_give']
    usrname_receive = request.form['usrname_give']
    cntcomment_receive = request.form['cntcomment_give']
    db.teamguestbook.update_one({'num': int(num_receive)}, {'$set': {'name': usrname_receive}})
    db.teamguestbook.update_one({'num': int(num_receive)}, {'$set': {'cntcomment': cntcomment_receive}})
    return jsonify({'msg': '방명록이 수정되었습니다.'})

@app.route("/teamguestbook/delete", methods=["POST"])
def bolee_delete():
    num_receive = request.form['num_give']
    db.teamguestbook.delete_one({'num':int(num_receive)})
    return jsonify({'msg': '방명록이 삭제되었습니다.'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5001, debug=True)
