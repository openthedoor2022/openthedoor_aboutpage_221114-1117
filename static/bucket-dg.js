$(document).ready(function () {
    show_bucket();
});

// 버킷 조회 기능
function show_bucket() {
    $.ajax({
        type: "GET",
        url: "/bucket",
        data: {},
        success: function (response) {
            let rows = response["buckets"];
            for (let i = 0; i < rows.length; i++) {
                let bucket = rows[i]["bucket"];
                let num = rows[i]["num"];
                let done = rows[i]["done"];
                let del = rows[i]["delete"];

                let temp_html = ``;
                if (done === 0 && del === 0) {
                    temp_html = `<li>
                                            <h2>🚪 ${bucket}</h2>
                                            <button onclick="done_bucket(${num})" type="button" class="btn-3">완료</button>
                                            <button onclick="update_bucket(${num})" type="button" class="btn-3">수정</button>
                                        </li>`;
                } else if (done === 1 && del === 0) {
                    temp_html = `<li>
                                            <h2 class="done">🎊 ${bucket}</h2>
                                            <button onclick="undone_bucket(${num})" type="button" class="btn-3">체크해제</button>
                                            <button onclick="delete_bucket(${num})" type="button" class="btn-3">삭제</button>
                                        </li>`;
                }else if ( del === 1){
                    temp_html = ``;
                }
                $("#bucket-list").append(temp_html);
            }
        },
    });
}

// 버킷 추가 기능
function save_bucket() {
    let bucket = $(`#bucket`).val();

    if (bucket === "") {
        alert("내용을 작성해주세요.")
    } else {
        $.ajax({
            type: "POST",
            url: "/bucket",
            data: {bucket_give: bucket},
            success: function (response) {
                alert(response["msg"]);
                window.location.reload();
            },
        });
    }
}

// 버킷 완료 기능
function done_bucket(num) {
    $.ajax({
        type: "POST",
        url: "/bucket/done",
        data: {num_give: num},
        success: function (response) {
            alert(response["msg"]);
            window.location.reload();
        },
    });
}

// 버킷 해제 기능
function undone_bucket(num) {
    $.ajax({
        type: "POST",
        url: "/bucket/undone",
        data: {num_give: num},
        success: function (response) {
            alert(response["msg"]);
            window.location.reload();
        },
    });
}

// 버킷 삭제 기능
function delete_bucket(num) {
    $.ajax({
        type: "DELETE",
        url: "/bucket",
        data: {
            num_give: num
        },
        success: function (response) {
             if (confirm("정말 삭제하시겠습니까?") === true){
                 alert(response["msg"])
                 window.location.reload()
     document.delete_bucket.submit();

 }else{   //취소

     return false;

 }
        }
    });
}

// 버킷 수정 기능
function update_bucket(num) {
    let bucket = $('#bucket').val()

    $.ajax({
        type: "PUT",
        url: "/bucket",
        data: {
            num_give: num,
            bucket_give: bucket
        },
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    })
}