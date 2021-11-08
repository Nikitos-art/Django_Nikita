// window.onload = function () {
//     $('.categories').on('click', 'input[type="number"]', function () {
//         let t_href = event.target;
//         console.log(t_href.name)
//         console.log(t_href.value)
//
//         $.ajax({
//             url: '/mainapp/category/' + t_href.name + '/' + t_href.value,
//             success: function (data) {
//                 $('.categories').html(data.result)
//             }
//         })
//         event.preventDefault()
//     })
// }