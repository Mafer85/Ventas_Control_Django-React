import React, {Component} from "react";
import {render} from "react-dom";
import { Button, Table, Navbar } from 'react-bootstrap';
import Popper from 'popper.js';
import 'bootstrap/dist/js/bootstrap.bundle.min';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loaded: false,
      placeholder: "Loading"
    }
  };

  componentDidMount() {
    fetch("http://127.0.0.1:8000/api/producto/")
     .then(response => {
       if (response.status > 400){
         return this.setState(() => {
           return {placeholder: "Algo salio mal!"};
         });
       }
       return response.json();
     })
     .then(data => {
       this.setState(() => {
         return {
           data,
           loaded: true
         };
       });
     });
  }

  render (){
    return (

      <div>

      <Table striped bordered hover variant="dark">
        <thead>
        <tr>
        <th>ID</th>
        <th>nombre</th>
        <th>precio</th>
        </tr>
        </thead>
        <tbody>
        {this.state.data.map(Producto => (
          <tr key={Producto.id}>
          <td>{Producto.id}</td>
          <td>{Producto.nombre}</td>
          <td><b>Q.{Producto.precio}</b></td>
          <td>
          <Button variant="success">Crear</Button>
           &nbsp;
          <Button variant="warning">Editar</Button>
           &nbsp;
          <Button variant="danger">Eliminar</Button>
          </td>
          </tr>
        ))}
        </tbody>
      </Table>
      </div>

    );
  }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
