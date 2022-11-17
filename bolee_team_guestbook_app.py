# 팀 소개 페이지용 방명록(포스트잇)
# 2022.11.16. 구현 시작일 (코드 작성자 : 이보형) / 버전 2022.11.17.

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://OPD:2022@clusteropd.h21fmkf.mongodb.net/?retryWrites=true&w=majority')
db = client.bolee


@app.route('/')
def home():
    return render_template('teamintro.html')


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
        'usrname': usrname_receive,
        'cntcomment': cntcomment_receive
    }
    db.teamguestbook.insert_one(doc)
    return jsonify({'msg': '똑똑똑! 당신의 소중한 이야기가 도착했습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)