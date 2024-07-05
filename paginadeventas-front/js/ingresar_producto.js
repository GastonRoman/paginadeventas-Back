function guardar() {
    let producto_ingresado = document.getElementById("producto").value //input
    let imagen_ingresada = document.getElementById("imagen").value 
    let descripcion_ingresada = document.getElementById("descripcion").value 
    let categoria_ingresada = document.getElementById("categoria").value 
    let precio_ingresado = document.getElementById("precio").value 
    // let stock_ingresado = document.getElementById("stock").value 
    

    // console.log(nombre_ingresado,imagen_ingresada,descripcion_ingresada,categoria_ingresada,precio_ingresado,stock_ingresado);
    // Se arma el objeto de js 
    let datos = {
        producto: producto_ingresado,
        imagen:imagen_ingresada,
        descripcion:descripcion_ingresada,
        categoria:categoria_ingresada,
        precio:precio_ingresado,
        // stock:stock_ingresado
    }
    console.log(datos);
    
    let url = "http://paginadeventas.pythonanywhere.com/registro"
    var options = {
        body: JSON.stringify(datos),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }
    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "../tabla_productos.html";  
            
        })
        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}