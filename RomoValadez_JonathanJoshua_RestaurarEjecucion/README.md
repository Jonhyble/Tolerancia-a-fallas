# Restaurar ejecución de programa
_Romo Valadez Jonathan Joshua_

_Computación tolerante a fallas_

_Universidad de Guadalajara_

_CUCEI_

_Departamento de ciencias computacionales_

---

## Introducción
Cuando estamos realizando un formulario o incluso escribiendo un documento en Word, suele suceder que algo nos provoque un cierre inesperado, y que esos datos se pierdan, con el tiempo se han ido creando métodos que nos permiten la persistencia de datos, y en esta actividad se verá uno de ellos.

---

## Desarrollo
En esta práctica se usará el localStorage para poder recuperar la información, el cual tiene otra opción para usar, que es el sessionStorage, pero el localStorage tiene la posibilidad de recuperar la información incluso si se cierra la pestaña, cosa que el sessionStorage recupera solo si se recarga la página.

_Cuando inicia la página intenta recuperar información de localStorage, si no la encuentra, los datos se quedarán vacios_

~~~JavaScript
useEffect(() => {
  setData({
    'Codigo' : localStorage.getItem("Codigo") || "", 'Nombre' : localStorage.getItem("Nombre") || "", 'Apellidos' : localStorage.getItem("Apellidos") || "", 'Carrera' : localStorage.getItem("Carrera") || "", 'Materia' : localStorage.getItem("Materia") || ""
  })
}, [])
~~~

_Los datos de localStorage se van llenando conforme se llena el formulario, llenando tambien los datos dentro del código_

~~~JavaScript
const changeData = (event) => {
  setData({
    ...data,
    [event.target.name] : event.target.value
  });
  localStorage.setItem(event.target.name, event.target.value);
}
~~~

_Para fines demostrativos, al presionar el botón de "Limpiar datos" se limpia localStorage y se recarga la página_

~~~JavaScript
const sendData = (event) => {
  event.preventDefault();
  alert("Limpiando datos");
  localStorage.clear();
  window.location.reload(false);
}
~~~

---

## Conclusión
Esta actividad nos permitió encontrar maneras de recuperar información, incluso cuando se cierra un programa de forma inesperada, en este caso un navegador, que nos permitirá recuperar datos por medio del localStorage.

También en este caso se logró ver la utilidad de localStorage y sessionStorage para la persistencia de datos.
