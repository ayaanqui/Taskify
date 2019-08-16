import React from 'react';
import classes from './Navbar.module.css';

const navbar = () => {
  return (
    <div className={ classes.header }>
      <div className={ classes.headerInner }>
        <button className={ classes.logo }></button>

        <div className={ classes.menuItems }>
          <button className={ `btn btn-default btn-sm ${ classes.menuItem }` }>@awesomeuser</button>

          <button style={{color: '#fff'}} className={ `btn btn-secondary btn-sm ${ classes.menuItem }` }>Logout</button>
        </div>
      </div>
    </div>
  );
};

export default navbar;