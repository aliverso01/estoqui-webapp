var tabprocessos;

function tabProcessos(){
    tabprocessos=$('#TBprocessos').DataTable({
            "ajax": "/processos/protocolo/json",
            "stateSave": true,
            "scrollY": "500px",
            "scrollCollapse": true,
            "aoColumns": [
                  {"data": "pk"},
                  {"data": "numero"},
                  {"data": "dataleitura"},
                  {"data": "status"},
                  {"data": "datacadastro"},
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


}



$(document).ready(function (){

    tabProcessos();

    $('#TBprocessos tbody').on('dblclick','tr', function () {
    var data = tabprocessos.row(this).data();
    location.href='/processos/comissao/cadastrar/'+data['pk'];
   });
})