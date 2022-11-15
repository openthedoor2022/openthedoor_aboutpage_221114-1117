from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import certifi

ca = certifi.where()
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@Cluster0.p5ctwmd.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('jm_index.html')

# 댓글 추가 기능
@app.route("/jungmin", methods=["POST"])
def jungmin_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    comment_list = list(db.jungmin.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'name':name_receive,
        'comment':comment_receive,
        'num':count,
        'done':0
    }
    db.jungmin.insert_one(doc)

    return jsonify({'msg': '댓글 달기 완료!'})

# 댓글 조회 기능
@app.route("/jungmin", methods=["GET"])
def jungmin_get():
    comment_list = list(db.jungmin.find({}, {'_id': False}))
    return jsonify({'jmguestbook': comment_list})

# 댓글 삭제 기능
@app.route("/jungmin/done", methods=["POST"])
def delete_comment():
    num_receive = request.form['num_give']
    db.jungmin.update_one({'num':int(num_receive)},{'$set':{'done':1}})
    return jsonify({'msg': '댓글 삭제 완료'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)