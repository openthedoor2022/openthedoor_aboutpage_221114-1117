from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import certifi

ca = certifi.where()
from pymongo import MongoClient

client = MongoClient('mongodb+srv://OPD:2022@clusteropd.h21fmkf.mongodb.net/myFirstDatabase',
                     tlsCAFile=ca)
db = client.openthedoor


# HTML 링크
# 메인 페이지
@app.route('/')
def home():
    return render_template('teamintro.html')

# 팀 멤버 소개
@app.route('/teammember')
def teammember():
    return render_template('team_index.html')

# 팀 프로젝트
@app.route('/teamproject')
def teamproject():
    return render_template('teamproject.html')

# 전규렬
@app.route('/gyuryeol')
def gyuryeol():
    return render_template('gr_index.html')

# 장동규
@app.route('/dongkyu')
def dongkyu():
    return render_template('dongkyu_index.html')

# 김정민
@app.route('/jungmin')
def jungmin():
    return render_template('jm_index.html')

# 이보형
@app.route('/bolee')
def bolee():
    return render_template('bolee_aboutpage.html')

@app.route('/bolee_guestbook')
def boleeguest():
    return render_template('bolee_guestbook.html')

# 장승윤
@app.route('/sy')
def sy():
   return render_template('sy_index.html')


# 팀 소개 페이지용 방명록(포스트잇)
@app.route("/teamguestbook", methods=["GET"])
def team_get():
    comment_list = list(db.teamguestbook.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


@app.route("/teamguestbook", methods=["POST"])
def team_post():
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

# 팀원 소개 페이지용 방명록(포스트잇)
# 2022.11.16. 구현 시작일 (코드 작성자 : 이보형) / 버전 2022.11.17.

@app.route("/teammemberguestbook", methods=["GET"])
def teammember_get():
    comment_list = list(db.teammemberguestbook.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


@app.route("/teammemberguestbook", methods=["POST"])
def teammember_post():
    usrname_receive = request.form['usrname_give']
    cntcomment_receive = request.form['cntcomment_give']

    comment_list = list(db.teammemberguestbook.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'usrname': usrname_receive,
        'cntcomment': cntcomment_receive
    }
    db.teammemberguestbook.insert_one(doc)
    return jsonify({'msg': '똑똑똑! 소중한 말씀 감사합니다.'})



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
@app.route("/bucket", methods=["DELETE"])
def bucket_delete():
    num_receive = request.form['num_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'delete': 1}})
    return jsonify({'msg': '삭제 완료!'})


# 버킷 수정 기능
@app.route("/bucket", methods=["PUT"])
def bucket_update():
    num_receive = request.form['num_give']
    bucket_receive = request.form['bucket_give']
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'bucket': bucket_receive}})
    return jsonify({'msg': '수정 완료!'})


#---------------------------------------------------개인 페이지---------------------------#

# 전규렬
@app.route("/gyuryeol", methods=["POST"])
def gyuryeol_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.gyuryeol.insert_one(doc)
    return jsonify({'msg': '방명록 작성완료'})


@app.route("/gyuryeol", methods=["GET"])
def gyuryeol_get():
    comment_list = list(db.gyuryeol.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

# 장동규
@app.route("/dongkyu", methods=["POST"])
def dongkyu_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    doc = {
        'name':name_receive,
        'comment':comment_receive
    }

    db.dongkyu.insert_one(doc)

    return jsonify({'msg': '좋아'})

@app.route("/dongkyu", methods=["GET"])
def dongkyu_get():
    comment_list = list(db.dongkyu.find({}, {'_id': False}))
    return jsonify({'comments':comment_list})

# 김정민
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
@app.route("/jungmin/show", methods=["GET"])
def jungmin_get():
    comment_list = list(db.jungmin.find({}, {'_id': False}))
    return jsonify({'jmguestbook': comment_list})

# 댓글 삭제 기능
@app.route("/jungmin/delete", methods=["DELETE"])
def delete_jungmin():
    num_receive = request.form['num_give']
    db.jungmin.update_one({'num':int(num_receive)},{'$set':{'done':1}})
    return jsonify({'msg': '댓글 삭제 완료'})

# 댓글 수정 기능
@app.route("/jungmin/update", methods=["PUT"])
def jungmin_update():
    num_receive = request.form['num_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    db.jungmin.update_one({'num': int(num_receive)}, {'$set': {'name': name_receive}})
    db.jungmin.update_one({'num': int(num_receive)}, {'$set': {'comment': comment_receive}})
    return jsonify({'msg': '수정 완료!'})


# 이보형
@app.route("/bolee", methods=["GET"])
def bolee_get():
    comment_list = list(db.bolee.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})


@app.route("/bolee", methods=["POST"])
def bolee_post():
    usrname_receive = request.form['usrname_give']
    cntcomment_receive = request.form['cntcomment_give']

    comment_list = list(db.bolee.find({}, {'_id': False}))
    count = len(comment_list) + 1

    doc = {
        'num': count,
        'usrname': usrname_receive,
        'cntcomment': cntcomment_receive
    }
    db.bolee.insert_one(doc)
    return jsonify({'msg': '방명록이 등록되었습니다.'})


@app.route("/bolee/delete", methods=["POST"])
def bolee_delete():
    num_receive = request.form['num_give']
    db.bolee.delete_one({'num':int(num_receive)})
    return jsonify({'msg': '방명록이 삭제되었습니다.'})


# 장승윤
@app.route("/sy_guestbook", methods=["POST"])
def sy_guestbook_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']

    sy_guestbook_list = list(db.sy_guestbooks.find({}, {'_id': False}))
    count = len(sy_guestbook_list) + 1

    doc = {
        'num': count,
        'name': name_receive,
        'comment': comment_receive,
        'done': 0
    }
    db.sy_guestbooks.insert_one(doc)
    return jsonify({'msg':'이름,응원댓글 저장완료!'})

@app.route('/sy_guestbook/delete', methods=['POST'])
def sy_guestbook_delete():
    num_receive = request.form['num_give']
    db.sy_guestbooks.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제 완료!'})



@app.route("/sy_guestbook/update", methods=["POST"])
def member_update():
    num_receive = request.form['num_give']
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']


    return jsonify({'msg': '수정할 수 없습니다. 삭제후 다시 작성해주세요!'})




@app.route("/sy_guestbook", methods=["GET"])
def sy_guestbook_get():
    sy_guestbooks_list  = list(db.sy_guestbooks.find({}, {'_id': False}))

    return jsonify({'guestbooks': sy_guestbooks_list})


# 여기서부터 버킷리스트


@app.route("/sy_bucket", methods=["POST"])
def sy_bucket_post():
    sy_buckets_list = list(db.sy_buckets.find({}, {'_id': False}))
    count = len(sy_buckets_list) + 1

    bucket_receive = request.form['bucket_give']

    doc = {'bucket': bucket_receive, 'num': count, 'done':0}
    db.sy_buckets.insert_one(doc)
    return jsonify({'msg': '버킷리스트가 저장완료 되었습니다!'})


@app.route("/sy_bucket/done", methods=["POST"])
def sy_bucket_done():
    num_receive = request.form['num_give']
    db.sy_buckets.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})

    return jsonify({'msg': '완료!!'})


@app.route("/sy_bucket/undone", methods=["POST"])
def sy_bucket_undone():
    num_receive = request.form['num_give']
    db.sy_buckets.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})

    return jsonify({'msg': '완료가 취소되었습니다!'})

@app.route("/sy_bucket/delete", methods=["POST"])
def sy_bucket_delete():
    num_receive = request.form['num_give']
    db.sy_buckets.delete_one({'num': int(num_receive)})
    return jsonify({'msg': '삭제되었습니다!'})



@app.route("/sy_bucket", methods=["GET"])
def sy_bucket_get():
    sy_buckets_list = list(db.sy_buckets.find({}, {'_id': False}))

    return jsonify({'sy_buckets': sy_buckets_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)