import axios from "axios";

function createInstance() {
  const instance = axios.create({
    baseURL: "http://j5c203.p.ssafy.io/api",

    headers: {
      "Content-Type": "application/json"
    },
  });
  return instance;
}
function createInstance2() {
  const token =  localStorage.getItem('token')
  const instance = axios.create({
    baseURL: "http://j5c203.p.ssafy.io/api",

    headers: {
      Authorization: `JWT ${token}`
    },
  });
  return instance;
}
function createInstance3() {
  const instance = axios.create({
    baseURL: "http://j5c203.p.ssafy.io/api",

  });
  return instance;
}
export { createInstance };
export { createInstance2 };
export { createInstance3 };


