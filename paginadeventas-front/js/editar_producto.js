function modificar() {
    let id = document.getElementById("id").value
    let producto_ingresado = document.getElementById("producto").value //input
    let imagen_ingresada = document.getElementById("imagen").value 
    let descripcion_ingresada = document.getElementById("descripcion").value 
    let categoria_ingresada = document.getElementById("categoria").value 
    let precio_ingresado = document.getElementById("precio").value 
    // let stock_ingresado = document.getElementById("stock").value 

    let datos = {
        producto: producto_ingresado,
        imagen:imagen_ingresada,
        descripcion:descripcion_ingresada,
        categoria:categoria_ingresada,
        precio:precio_ingresado,
        // stock:stock_ingresado  
    }

    console.log(datos);

    let url = "http://localhost:5000/update/"+id
    var options = {
        body: JSON.stringify(datos),
        method: 'PUT',
        
        headers: { 'Content-Type': 'application/json' },
        // el navegador seguirá automáticamente las redirecciones y
        // devolverá el recurso final al que se ha redirigido.
        redirect: 'follow'
    }
    fetch(url, options)
        .then(function () {
            console.log("modificado")
            alert("Registro modificado")

            //Puedes utilizar window.location.href para obtener la URL actual, redirigir a otras páginas
           window.location.href = "../tabla_productos.html";
          
        })
        .catch(err => {
            this.error = true
            console.error(err);
            alert("Error al Modificar")
        })      
}