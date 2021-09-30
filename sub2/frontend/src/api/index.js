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

function roadInstance(token) {
  const instance = axios.create({
    baseURL: "http://j5c203.p.ssafy.io/api",

    headers: {
      "Authorization": "JWT " + token,
      "Content-Type": "application/json"
    },
  });
  return instance;
}


function imageInstance() {
  const instance = axios.create({
    baseURL: "https://dapi.kakao.com/v2",

    headers: {
      "Authorization": "KakaoAK " + "81c18060700638a5bd2763e645639108",
      //"Content-Type": "application/json"
    },
  });
  return instance;
}

export { createInstance, roadInstance, imageInstance};
