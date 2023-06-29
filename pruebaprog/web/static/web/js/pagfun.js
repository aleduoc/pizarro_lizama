
// Variable global para almacenar la imagen de la obra de arte seleccionada
let selectedArtwork = null;

// Función para seleccionar una obra de arte
function selectArtwork(img) {
  // Obtener la imagen seleccionada y actualizar la variable global
  selectedArtwork = img;
  
  // Actualizar el elemento de texto para indicar la selección actual
  const selectedText = document.getElementById("selected-artwork");
  selectedText.textContent = "Obra de arte seleccionada: " + img.alt;
}

// Función para superponer la imagen de la obra de arte en la foto de la pared
function overlayImages() {
  // Verificar que se haya seleccionado una obra de arte
  if (!selectedArtwork) {
    alert("Seleccione una obra de arte antes de continuar.");
    return;
  }

  // Obtener la foto de la pared del usuario y la imagen de la obra de arte seleccionada
  const userWall = document.getElementById("user-wall");
  const artwork = selectedArtwork;

  // Crear un elemento div para la superposición
  const overlayDiv = document.createElement("div");
  overlayDiv.style.position = "absolute";
  overlayDiv.style.top = userWall.offsetTop + "px";
  overlayDiv.style.left = userWall.offsetLeft + "px";
  overlayDiv.style.width = userWall.offsetWidth + "px";
  overlayDiv.style.height = userWall.offsetHeight + "px";

  // Agregar la superposición al DOM
  document.body.appendChild(overlayDiv);

  // Crear un elemento img para la superposición de la obra de arte
  const overlayImg = document.createElement("img");
  overlayImg.src = artwork.src;
  overlayImg.alt = artwork.alt;
  overlayImg.style.position = "absolute";
  overlayImg.style.top = "13vw";
  overlayImg.style.left = "37vw ";
  overlayImg.style.width = "15vw";
  overlayImg.style.height = "15vw";
  overlayImg.style.border='solid black 8px';
  overlayImg.style.boxShadow='0.1vw 0.2vw 0.3vw';

  // Agregar la imagen de la obra de arte a la superposición
  overlayDiv.appendChild(overlayImg);
}







  