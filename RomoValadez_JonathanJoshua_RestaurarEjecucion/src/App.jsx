import { useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState({'Codigo' : '', 'Nombre' : '', 'Apellidos' : '', 'Carrera' : '', 'Materia' : ''});

  const changeData = (event) => {
    setData({
      ...data,
      [event.target.name] : event.target.value
    });
    localStorage.setItem(event.target.name, event.target.value);
  }

  const sendData = (event) => {
    event.preventDefault();
    alert("Limpiando datos");
    localStorage.clear();
    window.location.reload(false);
  }

  useEffect(() => {
    setData({
      'Codigo' : localStorage.getItem("Codigo") || "", 'Nombre' : localStorage.getItem("Nombre") || "", 'Apellidos' : localStorage.getItem("Apellidos") || "", 'Carrera' : localStorage.getItem("Carrera") || "", 'Materia' : localStorage.getItem("Materia") || ""
    })
  }, [])

  return (
    <div className="bg-gray-800 text-white w-screen h-screen p-4 flex flex-col justify-between">
      <div className="justify-center content-center text-center rounded-md bgc-gray-secondary w-full h-full p-4 text-2xl md:flex md:h-screen md:items-center mb-6">
        <div className="bg-gray-900 p-10 rounded-3xl shadow-2xl opacity-75">
          <form className="" onSubmit={sendData}>
            <div className="my-10">
                Código de estudiante: 
                <input className="mx-5 rounded-md text-white" name="Codigo" type="number" onChange={changeData} value={data.Codigo}></input>
            </div>
            <div className="my-10">
                Nombre(s) de estudiante: 
                <input className="mx-5 rounded-md text-white" name="Nombre" type="text" onChange={changeData} value={data.Nombre}></input>
            </div>
            <div className="my-10">
                Apellidos de estudiante: 
                <input className="mx-5 rounded-md text-white" name="Apellidos" type="text" onChange={changeData} value={data.Apellidos}></input>
            </div>
            <div className="my-10">
                Carrera:
                <input className="mx-5 rounded-md text-white" name="Carrera" type="text" onChange={changeData} value={data.Carrera}></input>
            </div>
            <div className="my-10">
                Materia:
                <input className="mx-5 rounded-md text-white" name="Materia" type="text" onChange={changeData} value={data.Materia}></input>
            </div>
            <div>
                <button type="submit" className="rounded-md border-2 px-3">Limpiar datos</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}

export default App
