$( document ).on( 'click', '.dropdown-menu a', function(event) {
   if (event.target.hasAttribute('href')) {
       var link = event.target.href + 'ajax/';
       var linkBaseUri = event.target.baseURI;
       var baseUriArray = linkBaseUri.split('/');
       if (baseUriArray[3] == 'projects' && baseUriArray[4]) {
           $.ajax({
               url: link,
               success: function (data) {
                   $('.details').html(data.result);
               },
           });
           event.preventDefault();
       }
   }
});