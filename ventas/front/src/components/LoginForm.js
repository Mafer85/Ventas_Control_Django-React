import React from 'react';
import { render } from "react-dom"
import PropTypes from 'prop-types';

class LoginForm extends React.Component {
  state = {
    username: '',
    password: ''
  };

  handle_change = e => {
    const name = e.target.name;
    const value = e.target.value;
    this.setState(prevstate => {
      const newState = { ...prevstate };
      newState[name] = value;
      return newState;
    });
  };

  render(){
    return (
      <form onSubmit ={e=> this.props.handle_login(e, this.state)}>
      <h4>iniciar sesion</h4>
      <label htmlFor="username">Usuario</label>
      <input
      type="text"
      name="username"
      value={this.state.username}
      onChange= {this.handle_change}/>
      <label htmlFor="password">Contraseña</label>
      <input type="password" name="password" value={this,state.password} onChange={this.handle_change}/>
      <input type="submit"/>
      </form>
    );
  }
}
export default LoginForm;
LoginForm.propTypes ={
    handle_login: PropTypes.func.isRequired
  };
