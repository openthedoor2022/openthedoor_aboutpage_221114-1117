$(document).ready(function () {
    show_comment()
});

function save_comment() {
    let name = $('#name').val()
    let comment = $('#comment').val()

    $.ajax({
        type: "POST",
        url: "/team",
        data: {'name_give': name, 'comment_give': comment},
        success: function (response) {
            alert(response["msg"])
            window.location.reload()
        }
    });
}

function show_comment() {
    $('#comment-list').empty()
    $.ajax({
        type: "GET",
        url: "/team",
        data: {},
        success: function (response) {
            let rows = response['comments']
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let comment = rows[i]['comment']

                let temp_html = `<div class="card">
                                            <div class="card-body">
                                                <blockquote class="blockquote mb-0">
                                                    <p>${comment}</p>
                                                    <footer class="blockquote-footer">${name}</footer>
                                                </blockquote>
                                            </div>
                                        </div>`
                $('#comment-list').append(temp_html)
            }
        }
    });
}
