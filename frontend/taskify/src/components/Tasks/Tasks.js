import React from 'react';
import Task from './Task/Task';
import AddTask from '../AddTask/AddTask';
import classes from './Tasks.module.css';

const tasks = (props) => {
  const showTasksOrEmpty = () => {
    let output = null;
    if (props.tasks.length !== 0) {
      output = (
        <div>
          {
            props.tasks.map((task, index) => {
              return (
                <Task
                  task={task}
                  key={index}
                  id={index}
                  changeCompleteStatus={props.changeCompleteStatus}
                  removeTask={props.removeTask}
                />
              );
            })
          }
        </div>
      );
    } else {
      output = (
        <div className={ classes.emptyList }>
          <h3>Empty List</h3>
          <p>Start adding stuff in here to get more productive!</p>
        </div>
      );
    }

    return output;
  };

  return (
    <div className={ classes.tasksBoard }>
      <div className={ classes.myTasks }>
        { showTasksOrEmpty() }
      </div>

      <AddTask
        addTask={ props.addTask }
      />
    </div>
  );
};

export default tasks;