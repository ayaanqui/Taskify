import React from 'react';
import Task from './Task/Task';
import AddTask from '../AddTask/AddTask';
import classes from './Tasks.module.css';

const tasks = (props) => {
  return (
    <div className={ classes.tasksBoard }>
      <div className={ classes.myTasks }>
        <div>
          {
            props.tasks.map((task, index) => {
              return (
                <Task
                  task={task}
                  key={index}
                />
              );
            })
          }
        </div>

        <div className={ classes.emptyList }>
          <h3>Empty List</h3>
          <p>Start adding stuff in here to get more productive!</p>
        </div>
      </div>

      <AddTask
        addTask={ props.addTask }
      />
    </div>
  );
};

export default tasks;