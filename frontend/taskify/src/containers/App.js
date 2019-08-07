import React, { Component } from 'react';
import './App.css';
import Navbar from '../components/Navbar/Navbar';
import Tasks from '../components/Tasks/Tasks';

class App extends Component {
  createTask = task => {
    return (
      {
        task: task,
        completed: false,
        date: null,
        detail: ""
      }
    );
  };
  
  state = {
    taskList: [
      this.createTask("Laudry"),
      this.createTask("Fire puff bois")
    ]
  };

  addTask = event => {
    const task = event.data.task;
    if (task && task !== "") {
      let newTaskList = [...this.state.taskList];
      newTaskList.push(this.createTask(task));

      this.setState({
        taskList: newTaskList
      });
    }
  };

  render = () => {
    return (
      <div>
        <Navbar />

        <div className="main-content content-body">
          <Tasks
            tasks={this.state.taskList}
            addTask={this.addTask}
          />
        </div>
      </div>
    );
  };
}

export default App;
