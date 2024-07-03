// Procedimiento para traer los datos del registro a editar
// Ej: "id=9&nombre=bulbasaur"
let cadena = location.search; // Cadena con los símbolos & y =

// Crear un objeto URLSearchParams con la cadena
// El objeto URLSearchParams en JavaScript es una
// interfaz que proporciona métodos y propiedades para
// trabajar con las cadenas de consulta (query strings) en URLs.
// Facilitando la obtención de parámetros y valores individuales
let datos = new URLSearchParams(cadena);

// Crear un objeto para almacenar los nombres de las variables y sus valores
let resultado = {};

// Iterar sobre los parámetros y guardar los nombres y valores en el objeto resultado
for (const [nombre, valor] of datos) {
    resultado[nombre] = valor;
    resultado[imagen] = valor;
    resultado[descripcion] = valor;
    resultado[categoria] = valor;
    resultado[precio] = valor;
    // resultado[stock] = valor
}

// Imprimir el resultado
// console.log(resultado); // Esto mostrará un objeto con las variables y sus valores


// Procedimiento para mostrar los datos a editar en el formulario de edición
document.getElementById("id").value = resultado["id"]
document.getElementById("producto").value = resultado["producto"]
document.getElementById("imagen").value = resultado["imagen"]
document.getElementById("descripcion").value = resultado["descripcion"]
document.getElementById("categoria").value = resultado["categoria"]
document.getElementById("precio").value = resultado["precio"]
// document.getElementById("stock").value = resultado["stock"]
