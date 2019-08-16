import React from 'react';
import classes from './Task.module.css';

const task = (props) => {
  const checkButton = () => {
    if (props.task.completed) {
      return <span className={ classes.checkComplete }></span>;
    }
    return <span className={ classes.checkNotComplete }></span>;
  };

  const strikeThroughTask = () => {
    if (props.task.completed) {
      return <span className={ classes.taskCompleted }>{ props.task.task }</span>;
    }
    return <span>{ props.task.task }</span>;
  };

  return (
    <div className={ classes.taskView }>
      <div className={ classes.checklist } onClick={() => props.changeCompleteStatus(props.id)}>
        { checkButton() }
      </div>

      <div className={ classes.taskDetails }>
        { strikeThroughTask() }
      </div>

      <div className={ classes.taskControls } onClick={() => props.removeTask(props.id)}><span className={ `icon-rubbish-bin-delete-button ${ classes.deleteTask }` }></span></div>
    </div>
  );
};

export default task;