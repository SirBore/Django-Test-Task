$(document).ready(function(){
  var dataTable = $('#book-table th').DataTable({
    'processing': true,
    'serverSide': true,
    'serverMethod': 'post',
    'searching': false,
    'data':{Category:Category,sort:sort}, 
    'ajax': {
       'url':'/books/',
       'data': function(data){
          // Read values
          var category = $('#searchByCategory').val();
          

          // Append to data
          data.searchByCategory = Category;
          
       }
    },
    'columns': [
       { data: 'Name' },
       { data: 'Category' },
       { data: 'Price' },
       
    ]
  });

  $('#searchByCategory').keyup(function(){
    dataTable.draw();
  });

  
});
$(document).ready(function () {
$('#book-table').DataTable();
$('.dataTables_length').addClass('bs-select');
});
