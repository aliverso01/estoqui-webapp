var tabeleitores;

function tabEleitores(){
    tabeleitores=$('#TBeleitores').DataTable({
            "ajax": "/eleitores/lista/json",
            "stateSave": true,
            "scrollY": "500px",
            "scrollCollapse": true,
            "aoColumns": [
                  {"data": "foto",
                  "render": function (data){
                    return '<img src="'+data+'" alt="Foto" style="max-width: 50px; max-height: 50px;"></td>';
                  }
                  },
                  {"data": "nome"},
                  {"data": "botao",
                  "render": function (data) {
                      return '<a href="/eleitores/detalhes/'+data['pk']+'"><i class="fas fa-info-circle" title="Detalhes"></i></a>' +
                          '<a href="https://api.whatsapp.com/send?phone=55'+data['telefone']+'" target="_blank"><i class="" title="Contato via WhatsApp"></i></a>' +
                          '<a href="/eleitores/detalhes/'+data['pk']+'"><i class="fas fa-edit" title="Editar"></i></a>'
                  }
                  },
            ],
            "responsive": true,
            "aaSorting": [],
            "pageLength": 50,
            "searching": false,
            "language": {
                "decimal": "",
                "emptyTable": "Sem registros disponíveis",
                "info": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
                "infoEmpty": "Mostrando de 0 até 0 de 0 registros",
                "infoFiltered": "(filtrado de _MAX_ registros no total)",
                "infoPostFix": "",
                "thousands": ",",
                "lengthMenu": "Mostrar _MENU_ registos",
                "loadingRecords": "A carregar dados...",
                "processing": "A processar...",
                "search": "Filtrar:",
                "zeroRecords": "Não foram encontrados resultados",
                "paginate": {
                    "first": "Primeiro",
                    "last": "Último",
                    "next": "Seguinte",
                    "previous": "Anterior"
                },
                "aria": {
                    "sortAscending": ": ordem crescente",
                    "sortDescending": ": ordem decrescente"
                }

            },

        });

    setInterval( function () {
        tabeleitores.ajax.reload();
    }, 60000 );

}



$(document).ready(function (){

    tabEleitores();

    $('#TBeleitores tbody').on('dblclick','tr', function () {
    var data = tabeleitores.row(this).data();
    location.href='/eleitores/detalhes/'+data['pk'];
   });
})