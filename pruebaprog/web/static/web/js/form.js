document.addEventListener('DOMContentLoaded', () => {
  const formulario = document.querySelector('#formulario');

  formulario.addEventListener('submit', (evento) => {
    evento.preventDefault(); // prevenir comportamiento por defecto de recargar la página

    // seleccionar cada elemento de entrada de datos del formulario
    const nombre = document.querySelector('#itNombre').value;
    const apellidoPaterno = document.querySelector('#itApellido').value;
    const apellidoMaterno = document.querySelector('#itApellidom').value;
    const email = document.querySelector('#itMail').value;
    const nombreObra = document.querySelector('#itObra').value;
    const descripcionObra = document.querySelector('#itDescripcion').value;

    // mostrar los valores en la consola
    console.log('Nombre:', nombre);
    console.log('Apellido Paterno:', apellidoPaterno);
    console.log('Apellido Materno:', apellidoMaterno);
    console.log('Email:', email);
    console.log('Nombre de la Obra:', nombreObra);
    console.log('Descripcion de la Obra:', descripcionObra);
  });
});


// Validaciones
  var expr = /^[a-zA-Z0-9_\.\-]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/;

  $(document).ready(function(){
    $("#bEnviar").click(function(){
      var nombre = $("#itNombre").val();
      var apellido = $("#itApellido").val();
      var apellidom = $("#itApellidom").val();
      var correo = $("#itMail").val();
      var obra = $("#itObra").val();
      var descripcion = $("#itDescripcion").val();

      if(nombre == ""){
        $("#mensaje1").fadeIn();
        return false;
      }else{
        $("#mensaje1").fadeOut();
        if(apellido == "") {
          $("#mensaje2").fadeIn();
          return false;
        }else{
          if(apellidom == "") {
          $("#mensajem").fadeIn();
          return false;
        }else{
          $("#mensaje2").fadeOut();
          if(correo == "" || !expr.test(correo)) {
            $("#mensaje3").fadeIn();
            return false;
          }else{
            $("#mensaje3").fadeOut();
            if(obra == "") {
              $("#mensaje4").fadeIn();
              return false;
            }else{
              $("#mensaje4").fadeOut();
              if(descripcion == "") {
                $("#mensaje5").fadeIn();
                return false;
              }
            }
          }
          
        }
      }
    }  
    
  });

  });

var botonEnviar = document.getElementById("bEnviar");
		var mensaje = document.getElementById("mensaje");

		botonEnviar.addEventListener("click", function() {
			mensaje.style.display = "block";

  // Muestra el mensaje durante 3 segundos
  setTimeout(() => {
    mensaje.remove();
  }, 3000);
});