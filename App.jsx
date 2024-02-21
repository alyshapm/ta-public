import { useState } from "react";
import "./App.css";

function App() {
  return (
    <>
      <form className="new-item-form">
        <div className="form-row">
          <label htmlFor="item">New item</label>
          <input type="text" id="item"></input>
        </div>

        <button className="btn">Add</button>
      </form>

      <h1 className="header">Todo List</h1>
      <ul className="list">
        <li>
          <input type="checkbox" />
          <label>Clean kitchen</label>
          <button className="btn btn-danger">Delete</button>
        </li>
        <li>
          <input type="checkbox" />
          <label>Do WADS homework</label>
          <button className="btn btn-danger">Delete</button>
        </li>
        <li>
          <input type="checkbox" />
          <label>Pray to god</label>
          <button className="btn btn-danger">Delete</button>
        </li>
      </ul>
    </>
  );
}

export default App;
