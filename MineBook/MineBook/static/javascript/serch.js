// $(document).ready(function(){  
//     $(document).on('click',".src_button",function(){
//         var _vm=$(this);
//         var _id=_vm.attr('data-index')
//         var _bt=$(".s-"+_id).val(); 
//     });
//     $.ajax({
//         url:'/serch-server',
//         data:{
//             'id':_bt,
//         },
//         dataType:'json',
//         beforeSend:function(){
//             _vm.attr('disabled',true);
//         }
//     });
// });

function copyIP(htmlElement){
    if (!htmlElement){
        return;
    }
    let elementText = htmlElement.innerText;
    
    let inputElement= document.createElement('input');
    inputElement.setAttribute('value',elementText);
    document.body.appendChild(inputElement)
    inputElement.focus();
    inputElement.setSelectionRange(19, inputElement.value.length);
    document.execCommand('copy');
    inputElement.parentNode.removeChild(inputElement);
}


function sortTable() {
    var table, rows, switching, i, x, y, shouldSwitch,counter;
    counter=document.getElementById('clicks');
    counterint=parseInt(counter.value);
    counterint=counterint+1;
    counter.value= `${counterint}`;
    table = document.getElementById("table");
    switching = true;
    while (switching) {
      switching = false;
      rows = table.rows;
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = rows[i].getElementsByTagName("TD")[3];
        y = rows[i + 1].getElementsByTagName("TD")[3];
        if (parseInt(y.innerHTML)==0){
            shouldSwitch = false;
            continue;
        }
        if (parseInt(x.innerHTML) ==0){
            if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {
                shouldSwitch = true;
                break;
            }
        }
        if (counterint%2==0){
            if (parseInt(x.innerHTML) < parseInt(y.innerHTML)) {
                shouldSwitch = true;
                break;
            }
        }
        if (counterint%2!=0){
            if (parseInt(x.innerHTML) > parseInt(y.innerHTML)) {
                shouldSwitch = true;
                break;
            }
        }
    }
    if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
      }
    }
}

// $(document).ready(function(){  
//     $('#table thaed tr')
//         .clone(true)
//         .addClass('filters')
//         .appendTo('#table thaed');
//     var table =$('#table').DataTable({
//         paging: true,
//         pageLength:10,
//         lengthChange:true,
//         autoWidht:true,
//         searching:true,
//         binfo:true,
//         bspot:true,
    
//     initComplete:function(){
//         var api = this.api();
        
//         api
//             .columns([0,1,2,3,4])
//             .eq(0)
//             each(function(colIdx){
//                 var cell = $('.filters th').eq()
//                 $(api.column(colIdx).header()).index()
//             });
//             var title = $(cell).text();
//             $(cell).html('<input type="text" placeholder="'+ title + '"/>');

//             $(
//                 'input',
//                 $('.filters th').eq($(api.column(colIdx).header()).index())
//             )
//             .off('keyip change')
//             .on('keyup change',function(e) {
//                 e.stopPropagation();

//                 $(this).atte('title', $(this).val());
//                 var regexr = '({search})';
//                 var cursorPosition = this.selectionStart;

//                 api
//                     .column(colIdx)
//                     .search(
//                         this.value != ''
//                             ? regexr.replace('{search}','((('+this.value+')))')
//                             :'',
//                         this.value !='',
//                         this.value == ''
//                     )
//                 .drew();

//                 $(this)
//                     .focus()[0]
//                     .setSelectionRange(cursorPosition,cursorPosition);
//                 });
//             });
//         },

//     })
    
// })
