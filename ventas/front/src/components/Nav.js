import React from 'react';
import { render } from "react-dom"
import PropTypes from 'prop-types';

function Nav(props){
  const logged_out_nav = (
    <ul>
      <li onClick={()=>props.display_form('login')}>Iniciar sesion</li>
      <li onClick={()=>props.display_form('singup')}>Cerrar sesion</li>
    </ul>
  );

  const logged_in_nav = (
    <ul>
    <li onClick={props.handle_logout}>salir</li>
    </ul>
  );
  return <div>{props.logged_in ? logged_in_nav : logged_out_nav}</div>;
}

export default Nav;

Nav.propTypes = {
  logged_in: PropTypes.bool.isRequired,
  display_form: PropTypes.func.isRequired,
  handle_logout: PropTypes.func.isRequired
};
