import React from 'react';
import classes from './Task.module.css';

const task = (props) => {
  return (
    <div className={ classes.taskView }>
      <div className={ classes.checklist }>
        <span className={ classes.checkNotComplete }></span>
        {/* <span v-else @click="$emit('complete-task', task.id)" class="check-complete"></span> */}
      </div>

      <div className={ classes.taskDetails }>
        <span>{ props.task.task }</span>
      </div>

      <div className={ classes.taskControls }><span className={ `icon-rubbish-bin-delete-button ${ classes.deleteTask }` }></span></div>
    </div>
  );
};

export default task;