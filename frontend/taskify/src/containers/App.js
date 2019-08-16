import React, { Component } from 'react';
import './App.css';
import Navbar from '../components/Navbar/Navbar';
import Tasks from '../components/Tasks/Tasks';

class App extends Component {
  createTask = (task, completed) => {
    return (
      {
        task: task,
        completed: completed,
        date: null,
        detail: ""
      }
    );
  };
  
  state = {
    taskList: [
      this.createTask("Laudry", false),
      this.createTask("Fire puff bois", true)
    ]
  };

  addTask = task => {
    if (task && task !== "") {
      let newTaskList = [...this.state.taskList];
      newTaskList.push(this.createTask(task));

      this.setState({
        taskList: newTaskList
      });
    }
  };

  changeCompleteStatus = id => {
    let newTaskList = [...this.state.taskList];
    const myTask = newTaskList[id];
    myTask.completed = !myTask.completed;
    this.setState({
      taskList: newTaskList
    });
  };

  removeTask = id => {
    let newTaskList = [...this.state.taskList];
    newTaskList.splice(id, 1);
    this.setState({
      taskList: newTaskList
    });
  };

  render = () => {
    return (
      <div>
        <Navbar />

        <div className="main-content content-body">
          <Tasks
            tasks={this.state.taskList}
            addTask={this.addTask}
            changeCompleteStatus={this.changeCompleteStatus}
            removeTask={this.removeTask}
          />
        </div>
      </div>
    );
  };
}

export default App;
