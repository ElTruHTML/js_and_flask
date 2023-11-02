"use strict";

const URL_INDEX         = "http://127.0.0.1:5500/index.html";
const URL_ONLINECHECK   = "http://127.0.0.1:5000/";
const URL_CREATE        = "http://127.0.0.1:5000/create";

function createTodo(form) {
    event.preventDefault();
    let todo = form.elements.todo.value;
    fetch(URL_CREATE, {
        method: "post",
        headers: {"Content-Type":"text/plain"},
        body: todo,
    })
    .then(res => res.text())
    .then(result => {
        console.log(result);
    });
}

window.addEventListener("DOMContentLoaded", () => {
    fetch(URL_ONLINECHECK)
    .then(res => res.text())
    .then(text => {
        console.log(text);
    });
});