/*guest book*/
$(document).ready(function () {
    show_comment()
});

/*댓글 추가 기능*/
function save_comment() {
    let name = $('#name').val()
    let comment = $('#comment').val()

    if (name === "" || comment === "") {
        alert("이름 또는 내용을 작성해주세요.")
    } else {
        $.ajax({
            type: 'POST',
            url: '/jungmin',
            data: {name_give: name, comment_give: comment},
            success: function (response) {
                alert(response['msg'])
                window.location.reload()
            }
        })
    }
}

/*댓글 조회 기능*/
function show_comment() {
    $.ajax({
        type: "GET",
        url: "/jungmin",
        data: {},
        success: function (response) {
            let rows = response['jmguestbook']
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let comment = rows[i]['comment']
                let num = rows[i]['num']
                let done = rows[i]['done']

                let temp_html = ``
                if (done === 0) {
                    temp_html = `<div class="guest-book-card">
                                            <div class="card-body">
                                                <blockquote class="blockquote mb-0">
                                                    <p>${comment}</p>
                                                    <footer class="blockquote-footer">${name}</footer>
                                                    <button type="button" onclick="delete_comment(${num})" class="jm_btn btn-secondary btn-sm">삭제</button>
                                                    <button type="button" class="jm_btn btn-secondary btn-sm">수정</button>
                                                </blockquote>
                                            </div>
                                        </div>`
                } else {
                    temp_html = ``
                }
                $('#comment-list').append(temp_html)
            }
        }
    });
}

/*댓글 삭제 기능*/
function delete_comment(num) {
    $.ajax({
        type: "POST", url: "/jungmin/done", data: {num_give: num}, success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}