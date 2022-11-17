   $(document).ready(function(){
            show_comment()

        });
        // function set_temp(){
        //     $.ajax({
        //         type: "GET",
        //         url: "http://spartacodingclub.shop/sparta_api/weather/seoul",
        //         data: {},
        //         success: function (response) {
        //             $('#temp').text(response['temp'])
        //         }
        //     })
        // }
        function save_comment(){

            let name = $('#name').val()
            let comment = $('#comment').val()

            $.ajax({
                type: 'POST',
                url: '/sy_guestbook',
                data: { name_give:name, comment_give: comment},
                success: function (response) {
                    alert(response['msg'])

                    window.location.reload()
                }
            })
        }


        function delete_comment (num) {

                  if(confirm("정말 삭제하시겠습니까?") == true){
                $.ajax({
                    type: 'POST',
                    url: '/sy_guestbook/delete',
                    data: {num_give: num},
                    success: function (response) {
                        alert(response['msg']);
                        window.location.reload()
                    }
                });
                    }else {
                      return false
                  }
            }


        function update_comment (num) {

            let name = $('#name').val()
            let comment = $('#comment').val()

                  prompt('수정내용을 입력해주세요!')
                $.ajax({
                    type: 'POST',
                    url: '/sy_guestbook/update',
                    data: {num_give: num, name_give: name, comment_give: comment},
                    success: function (response) {
                        alert(response['msg']);
                        window.location.reload()
                    }
                });

            }


        function show_comment( ){
            $.ajax({
                type: "GET",
                url: "/sy_guestbook",
                data: {},
                success: function (response) {

                    let rows = response['guestbooks']
                    for (let i=0; i<rows.length; i++){

                        let name =  rows[i]['name']
                        let num = rows[i]['num']
                        let comment = rows[i]['comment']
                        let temp_html = `<div class="card border mb-3" style=" margin : 20px 20px">
                                                    
                     <div class="card-body">

                        <div class="d-grid gap-2 d-md-block" style="float:right">
                          <button onclick="update_comment(${num})" class="btn btn-outline-secondary" type="button">수정하기</button>
                          <button onclick="delete_comment(${num})" class="btn btn-outline-secondary" type="button">     <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3" viewBox="0 0 16 16">
  <path d="M6.5 1h3a.5.5 0 0 1 .5.5v1H6v-1a.5.5 0 0 1 .5-.5ZM11 2.5v-1A1.5 1.5 0 0 0 9.5 0h-3A1.5 1.5 0 0 0 5 1.5v1H2.506a.58.58 0 0 0-.01 0H1.5a.5.5 0 0 0 0 1h.538l.853 10.66A2 2 0 0 0 4.885 16h6.23a2 2 0 0 0 1.994-1.84l.853-10.66h.538a.5.5 0 0 0 0-1h-.995a.59.59 0 0 0-.01 0H11Zm1.958 1-.846 10.58a1 1 0 0 1-.997.92h-6.23a1 1 0 0 1-.997-.92L3.042 3.5h9.916Zm-7.487 1a.5.5 0 0 1 .528.47l.5 8.5a.5.5 0 0 1-.998.06L5 5.03a.5.5 0 0 1 .47-.53Zm5.058 0a.5.5 0 0 1 .47.53l-.5 8.5a.5.5 0 1 1-.998-.06l.5-8.5a.5.5 0 0 1 .528-.47ZM8 4.5a.5.5 0 0 1 .5.5v8.5a.5.5 0 0 1-1 0V5a.5.5 0 0 1 .5-.5Z"/>
</svg>
</button>
                        </div>

                
                                                        <h5 class="card-title">${name}</h5>
                                                        <p class="card-text">${comment}</p>

                                                    </div>


                                                </div>`


                        $('#comment-list').append(temp_html)

                    }




                        }
            });
        }













