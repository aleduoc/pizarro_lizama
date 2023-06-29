

$(document).ready(function() {
    function generarImagen() {
      $.ajax({
        url: "https://api.pexels.com/v1/search?query=art&per_page=1&page=" + Math.floor(Math.random() * 50) + 1,
        beforeSend: function(xhr) {
          xhr.setRequestHeader("Authorization", "9qa9q5JUlUgp3U7QEbirNikEeicFWBqZDUgwQ2n9TPubN6uKaXMRSXj0");
          xhr.setRequestHeader("Accept", "application/json");
        },
        success: function(data) {
          var imagen = data["photos"][0]["src"]["landscape"];
          $("#imagen").html("<img src='" + imagen + "' alt='Imagen de Pexels' class='ajuste'>");
        }
      });
    }
    
    $("#generar-imagen").click(function() {
      generarImagen();
    });
    
  
  });

  