import React from 'react';
import classes from './Navbar.module.css';

const navbar = () => {
  return (
    <div className={ classes.header }>
      <div className={ classes.headerInner }>
        <a className={ classes.logo }></a>

        <div className={ classes.menuItems }>
          <a className={ `btn btn-default btn-sm ${ classes.menuItem }` }>@awesomeuser</a>

          <a style={{color: '#fff'}} className={ `btn btn-secondary btn-sm ${ classes.menuItem }` }>Logout</a>
        </div>
      </div>
    </div>
  );
};

export default navbar;