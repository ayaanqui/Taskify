import React from 'react';
import classes from './AddTask.module.css';

const addTask = (props) => {
  let task = "";

  const checkInput = (event) => {
    task = event.target.value;
  };

  const submit = (event) => {
    event.preventDefault();
    if (task !== "" && task !== " ") {
      props.addTask(task);
      task = "";
    }
  };

  return (
    <div className={ classes.newTaskBoard }>
      <form className={ classes.newTaskBoardContainer } onSubmit={submit}>
        <div className={ classes.task }>
          <input onChange={checkInput} className={ classes.taskInputController } name="task" type="text" placeholder="Add a task..." required autoFocus autoComplete="off" />
        </div>

        <div className={ classes.createTask }>
          <button className={ `${classes.addTaskButton} ${classes.active}` } type="submit"><span className="icon-add-plus-button"></span></button>
        </div>
      </form>
    </div>
  );
};

export default addTask;