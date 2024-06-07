// script.js

function eliminarDelCarrito(id) {
    fetch('/eliminar-del-carro', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id_Can: id
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Muestra un mensaje de confirmación al usuario
        window.location.reload(); // Recarga la página para reflejar los cambios en el carrito
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
