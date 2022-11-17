# 개인 소개 페이지용 방명록
# 2022.11.15. 구현 시작일 (코드 작성자 : 이보형) / 버전 2022.11.17.

from flask import Flask, jsonify, render_template, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://OPD:2022@clusteropd.h21fmkf.mongodb.net/?retryWrites=true&w=majority')
db = client.bolee


@app.route('/')
def home():
    return render_template('bolee_guestbook.html')


@app.route("/guestbook", methods=["GET"])
def bolee_get():
    comment_list = list(db.guestbook.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


@app.route("/guestbook", methods=["POST"])
def bolee_post():
    usrname_receive = request.form['usrname_give']
    cntcomment_receive = request.form['cntcomment_give']

    comment_list = list(db.guestbook.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'usrname': usrname_receive,
        'cntcomment': cntcomment_receive
    }
    db.guestbook.insert_one(doc)
    return jsonify({'msg': '방명록이 등록되었습니다.'})


@app.route("/guestbook/delete", methods=["POST"])
def bolee_delete():
    num_receive = request.form['num_give']
    db.guestbook.delete_one({'num':int(num_receive)})
    return jsonify({'msg': '방명록이 삭제되었습니다.'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
