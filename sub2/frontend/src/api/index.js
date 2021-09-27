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

export { createInstance };
