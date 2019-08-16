import React from 'react';
import classes from './AddTask.module.css';

const addTask = (props) => {
  const submit = (event) => {
    event.preventDefault();
    let task = event.target.task.value;
    if (task !== "" && task !== " ") {
      props.addTask(task);
      event.target.task.value = "";
    }
  };

  return (
    <div className={ classes.newTaskBoard }>
      <form className={ classes.newTaskBoardContainer } onSubmit={submit}>
        <div className={ classes.task }>
          <input className={ classes.taskInputController } name="task" type="text" placeholder="Add a task..." required autoFocus autoComplete="off" />
        </div>

        <div className={ classes.createTask }>
          <button className={ `${classes.addTaskButton} ${classes.active}` } type="submit"><span className="icon-add-plus-button"></span></button>
        </div>
      </form>
    </div>
  );
};

export default addTask;