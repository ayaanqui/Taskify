import React from 'react';
import classes from './AddTask.module.css';

const addTask = (props) => {
  return (
    <div className={ classes.newTaskBoard }>
      <form className={ classes.newTaskBoardContainer }>
        <div className={ classes.task }>
          <input className={ classes.taskInputController } name="task" type="text" placeholder="Add a task..." required autoFocus autoComplete="off" />
        </div>

        <div className={ classes.createTask }>
          <button className={ classes.addTaskButton } type="submit"><span className="icon-add-plus-button"></span></button>
        </div>
      </form>
    </div>
  );
};

export default addTask;