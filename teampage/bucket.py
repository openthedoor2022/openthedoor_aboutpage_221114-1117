from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import certifi

ca = certifi.where()
from pymongo import MongoClient

client = MongoClient('mongodb+srv://OPD:2022@clusteropd.h21fmkf.mongodb.net/myFirstDatabase',
                     tlsCAFile=ca)
db = client.jungmin


@app.route('/')
def home():
    return render_template('bucket.html')


# 버킷 추가 기능
@app.route("/bucket", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']

    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list) + 1

    doc = {
        'num': count,
        'bucket': bucket_receive,
        'done': 0,
        'delete': 0
    }

    db.bucket.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})


# 버킷 완료 기능
@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷 완료!'})


# 버킷 체크해제 기능
@app.route("/bucket/undone", methods=["POST"])
def bucket_undone():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
    return jsonify({'msg': '체크 해제!'})


# 버킷 조회 기능
@app.route("/bucket", methods=["GET"])
def bucket_get():
    bucket_list = list(db.bucket.find({}, {'_id': False}))

    return jsonify({'buckets': bucket_list})


# 버킷 삭제 기능
@app.route("/bucket/delete", methods=["POST"])
def bucket_delete():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'delete': 1}})
    return jsonify({'msg': '삭제 완료!'})


# 버킷 수정 기능
@app.route("/bucket/update", methods=["POST"])
def bucket_update():
    num_receive = request.form['num_give']
    bucket_receive = request.form['bucket_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'bucket': bucket_receive}})
    return jsonify({'msg': '수정 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)