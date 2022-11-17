
//버튼0 을 누르면
// 모든 버튼에 붙은 orange 클래스명을 제거한다.
// 버튼0에 orange 클래스명을 추가한다.
// 모든 div에 붙은 show 클래스명을 제거한다.
// div0에 show클래스명을 추가한다.s


// $('.tab-button').eq(0).on('click', function(){
//     $('.tab-button').removeClass('orange');
//     $('.tab-button').eq(0).addClass('orange');
//     $('.tab-content').removeClass('show');
//     $('.tab-content').eq(0).addClass('show');
//   })

//이거 for문안에 변수 넣어줘야 하는 이유?

for( let i=0; i<3; i++){

    let tabButton = $('.tab-button');
    let tabContent = $('.tab-content');

        tabButton.eq(i).on('click',function(){
        tabButton.removeClass('orange');
        tabButton.eq(i).addClass('orange');
        tabContent.removeClass('show');
        tabContent.eq(i).addClass('show');
    });
    

}

