$(document).ready(function () {
    show_sy();
});

function show_sy() {
    $.ajax({
        type: "GET",
        url: "/sy_bucket",
        data: {},
        success: function (response) {
                let rows = response['sy_buckets']
            for(let i=0; i<rows.length; i++){

                let bucket = rows[i]['bucket']
                let num = rows[i]['num']
                let done = rows[i]['done']

               let temp_html = ``
                if( done == 0 ){
                      temp_html = `<li>
                                 <h2 id="undone">🤍${bucket}</h2>
                             <button onclick="done_sy(${num})" type="button" class="btn btn-success">완료!</button>
                              <button onclick="delete_sy(${num})" style="margin-left: 5px" type="button" class="btn btn-outline-secondary">삭제</button>
                                </li>`
                }else{

                temp_html = ` <li>
                                    <h2 class="done">💖${bucket}</h2>
                              <button onclick="undone_sy(${num})" type="button" class="btn btn-outline-danger">완료취소!</button>
                               <button onclick="delete_sy(${num})" style="margin-left: 5px" type="button" class="btn btn-outline-secondary">삭제</button>

                               </li>`

                }
                $('#bucket-list').append(temp_html)
            }
        }
    })
}

function save_sy() {

    let bucket = $('#bucket').val()

    $.ajax({
        type: "POST",
        url: "/sy_bucket",
        data: {bucket_give: bucket},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}

function done_sy(num) {


    $.ajax({
        type: "POST",
        url: "/sy_bucket/done",
        data: {num_give: num},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}



function undone_sy(num) {


    $.ajax({
        type: "POST",
        url: "/sy_bucket/undone",
        data: {num_give: num},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}



function delete_sy(num) {


    $.ajax({
        type: "POST",
        url: "/sy_bucket/delete",
        data: {num_give: num},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}